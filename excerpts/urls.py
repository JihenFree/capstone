from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("oldpages/<int:this_page>", views.oldpages, name="oldpages"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newexcerpt", views.new_excerpt, name="newexcerpt"),
    path("find", views.find, name="find"),
    path("bylikes", views.bylikes, name="bylikes"),
    path("sending", views.sending, name="sending"),

    # API Routes
    path("likes/<int:excerpt_id>", views.likes, name="likes"),
    path("edit/<int:excerpt_id>", views.edit, name="edit"),
    path("delete/<int:excerpt_id>", views.delete, name="delete"),
    path("maxday", views.maxday, name="maxday"),
    path("booklist", views.booklist, name="booklist"),
    path("rewardlist", views.rewardlist, name="rewardlist"),
    path("completereward/<int:reward_id>", views.complete_reward, name="completereward"),
    path("reward/", views.reward, name="reward"),
    path("search/<str:word>", views.search, name="search")
]