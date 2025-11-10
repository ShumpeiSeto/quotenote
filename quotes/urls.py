from django.urls import path
from . import views
from .views import FollowHome, FollowDetail, FollowList, FollowToggle

app_name = "quotes"
urlpatterns = [
    path("", views.index, name="index"),
    path("book/create/", views.create_book, name="createbook"),
    path("quote/<int:pk>", views.detail, name="detail"),
    path("quote/create", views.create, name="create"),
    path("quote/<int:pk>/edit/", views.edit, name="edit"),
    path("quote/<int:pk>/delete/", views.delete, name="delete"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("follow-home/<int:pk>", FollowHome.as_view(), name="follow-home"),
    path("follow-detail/<int:pk>", FollowDetail.as_view(), name="follow-detail"),
    path("follow-list/", FollowList.as_view(), name="follow-list"),
    path("follow-toggle/<int:pk>", FollowToggle.as_view(), name="follow-toggle"),
]
