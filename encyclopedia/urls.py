from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry_detail, name="entry_detail"),
    path("search/<str:query>", views.search, name="search"),
    path("createNewPage/", views.createNewPage, name="createNewPage"),
    path("edit/<str:title>" , views.entry_edit , name = "entry_edit"),
    path("random/" , views.randomEntry , name = "randomEntry"),

]
