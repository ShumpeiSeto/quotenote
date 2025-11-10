from django import forms
from .models import Quote, Book, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["content", "book", "page"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "引用を入力",
                }
            ),
            "book": forms.Select(
                attrs={
                    "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                }
            ),
            "page": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                }
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["book"].queryset = Book.objects.all()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "isbn", "url", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "book-title w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "本名を入力",
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "book-author w-full px-4 py-2 border text-gray-900 rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "著者を入力",
                }
            ),
            "isbn": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "isbnを入力(未入力可)",
                }
            ),
            "url": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border text-gray-900 rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "urlを入力(未入力可)",
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "カテゴリーを入力",
                }
            ),
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border text-gray-900 rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                    "placeholder": "ユーザ名",
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                "placeholder": "パスワード",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "w-full px-4 py-2 text-gray-900 border rounded-lg focus:outline-none focus-ring-2 focus:ring-blue-500",
                "placeholder": "パスワード(確認)",
            }
        )
