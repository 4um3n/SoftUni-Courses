from django.urls import path
from recipes.common.views import home_page, create, edit, delete, details


urlpatterns = [
    path("", home_page, name="home page"),
    path("create/", create, name="create page"),
    path("edit/<int:recipe_pk>", edit, name="edit page"),
    path("delete/<int:recipe_pk>", delete, name="delete page"),
    path("details/<int:recipe_pk>", details, name="details page"),
]
