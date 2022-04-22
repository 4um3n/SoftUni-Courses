from django.shortcuts import render, redirect
from recipes.common.forms import RecipeForm
from recipes.common.models import Recipe


def render_page_with_form(request, template_name, form):
    context = {"form": form}
    return render(request, template_name, context)


def home_page(request):
    if request.method == "GET":
        context = {
            "recipes": Recipe.objects.all()
        }
        return render(request, "index.html", context)
    else:
        pass


def create(request):
    if request.method == "GET":
        form = RecipeForm()
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")

    return render_page_with_form(request, "create.html", form)


def edit(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)

    if request.method == "GET":
        form = RecipeForm(initial=recipe.__dict__)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home page")

    return render_page_with_form(request, "edit.html", form)


def delete(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)

    if request.method == "GET":
        form = RecipeForm(disable_fields=True, initial=recipe.__dict__)
        return render_page_with_form(request, "delete.html", form)
    else:
        recipe.delete()
        return redirect("home page")


def details(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)

    if request.method == "GET":
        context = {
            "recipe": recipe,
            "ingredients": recipe.ingredients.split(", "),
        }
        return render(request, "details.html", context)
    else:
        pass
