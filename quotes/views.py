from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Quote, Book, Tag, Connection
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm, BookForm, SignUpForm
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    quotes = Quote.objects.all()
    connection = None
    if request.user.is_authenticated:
        connection = Connection.objects.get_or_create(user=request.user)
    context = {
        "quotes": quotes,
        "connection": connection,
    }
    return render(request, "quotes/index.html", context)


def detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    connection = None
    if request.user.is_authenticated:
        connection = Connection.objects.get_or_create(user=request.user)
    context = {
        "quote": quote,
        "connection": connection,
    }
    return render(request, "quotes/detail.html", context)


# 引用の登録
@login_required
def create(request):
    if request.method == "POST":
        form = QuoteForm(request, request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            messages.success(request, "引用の登録に成功しました")
            return redirect("quotes:index")
    else:
        form = QuoteForm(request.user)
    context = {"form": form}
    return render(request, "quotes/create.html", context)


@login_required
def edit(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        form = QuoteForm(request.user, request.POST, instance=quote)
        if form.is_valid():
            form.save()
            messages.success(request, "引用が編集されました")
            return redirect("quotes:index")
    else:
        form = QuoteForm(request.user, instance=quote)
    context = {"form": form}
    return render(request, "quotes/edit.html", context)


@login_required
def delete(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        quote.delete()
        messages.success(request, "引用が削除されました")
        return redirect("quotes:index")
    # GETの場合はページ削除確認ページ表示
    context = {"quote": quote}
    return render(request, "quotes/delete_confirm.html", context)


# 本の登録
@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            messages.success(request, f"本{book.title}を登録しました")
            return redirect("quotes:index")
    else:
        form = BookForm()
        context = {"form": form}
        return render(request, "quotes/create_book.html", context)


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.username}さん登録ありがとうございます！")
            return redirect("quotes:index")
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, "quotes/signup.html", context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "ログアウトしました")
    return redirect("quotes:index")


# フォロー機能
class FollowBase(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        target_user = Quote.objects.get(pk=pk).user
        my_connection = Connection.objects.get_or_create(user=self.request.user)
        if target_user in my_connection[0].follow.all():
            obj = my_connection[0].follow.remove(target_user)
        else:
            obj = my_connection[0].follow.add(target_user)
        return obj


class FollowHome(FollowBase):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect("quotes:index")


class FollowDetail(FollowBase):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        pk = self.kwargs["pk"]
        return redirect("quotes:detail", pk)


class FollowToggle(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_pk = self.kwargs["pk"]
        target_user = User.objects.get(pk=user_pk)
        my_connection = Connection.objects.get_or_create(user=self.request.user)
        if target_user in my_connection[0].follow.all():
            my_connection[0].follow.remove(target_user)
        else:
            my_connection[0].follow.add(target_user)
        return redirect("quotes:follow-list")


class FollowList(LoginRequiredMixin, ListView):
    # モデル設定
    model = Quote
    # このテンプレートでレンダリングする
    # テンプレート側ではモデルのオブジェクトはobject_listで渡される
    template_name = "quotes/follow_list.html"

    def get_queryset(self):
        my_connection = Connection.objects.get_or_create(user=self.request.user)
        all_follow = my_connection[0].follow.all()
        return Quote.objects.filter(user__in=all_follow)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["connection"] = Connection.objects.get_or_create(user=self.request.user)
        return context
