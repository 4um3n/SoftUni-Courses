from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import CreatePetForm
from petstagram.pets.models import Pet, Like


# Create your views here.


def render_page_with_form(request, template_name, form):
    context = {"form": form}
    return render(request, template_name, context)


def pet_all(request):
    pets = Pet.objects.all()
    context = {
        "pets": pets
    }
    return render(request, 'pets/pet_list.html', context)


def create_pet(request):
    if request.method == "GET":
        return render_page_with_form(request, "pets/pet_create.html", CreatePetForm())
    else:
        form = CreatePetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pet all")

        return render_page_with_form(request, "pets/pet_create.html", form)


def edit_pet(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk
                          )
    if request.method == "GET":
        form = CreatePetForm(initial=pet.__dict__)
        return render_page_with_form(request, "pets/pet_edit.html", form)
    else:
        form = CreatePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet details")

        return render_page_with_form(request, "pets/pet_edit.html", form)


def delete_pet(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)

    if request.method == "GET":
        context = {"pet": pet}
        return render(request, "pets/pet_delete.html", context)
    else:
        pet.delete()
        return redirect("pet all")


def pet_detail(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)
    comments = Comment.objects.filter(pet=pet)

    if request.method == "GET":
        pet.likes = pet.like_set.count()
        context = {
            "pet": pet,
            "comments": comments,
            "form": CommentForm(),
        }
        return render(request, 'pets/pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pet = pet
            comment.save()
            return redirect("pet details", pet.pk)

        context = {
            "pet": pet,
            "comments": comments,
            "form": form,
        }
        return render(request, "pets/pet_detail.html", context)


def like_pet(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet all')
