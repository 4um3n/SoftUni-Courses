from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from petstagram.accounts.models import UserProfile
from petstagram.common.views import render_page_with_form
from petstagram.pets.forms import CommentForm
from petstagram.pets.models import Comment
from petstagram.pets.forms import CreatePetForm
from petstagram.pets.models import Pet, Like
from petstagram.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def pet_all(request):
    pets = Pet.objects.all()
    context = {
        "pets": pets
    }
    return render(request, 'pets/pet_list.html', context)


@login_required(login_url=LOGIN_URL)
def create_pet(request):
    if request.method == "GET":
        return render_page_with_form(request, "pets/pet_create.html", CreatePetForm())
    else:
        form = CreatePetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = UserProfile.objects.get(pk=request.user.pk)
            pet.save()
            return redirect("pet all")

        return render_page_with_form(request, "pets/pet_create.html", form)


@login_required(login_url=LOGIN_URL)
def edit_pet(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)

    if request.method == "GET":
        form = CreatePetForm(initial=pet.__dict__)
        return render_page_with_form(request, "pets/pet_edit.html", form)
    else:
        form = CreatePetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet details", pet.pk)

        return render_page_with_form(request, "pets/pet_edit.html", form)


@login_required(login_url=LOGIN_URL)
def delete_pet(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "GET":
        context = {"pet": pet}
        return render(request, "pets/pet_delete.html", context)
    else:
        pet.delete()
        return redirect("pet all")


@login_required(login_url=LOGIN_URL)
def pet_detail(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)
    comments = Comment.objects.filter(pet=pet)
    user_profile = UserProfile.objects.get(user=request.user)
    users_liked_pet = [like.user for like in pet.like_set.all()]
    is_liked = True if user_profile in users_liked_pet else False

    if request.method == "GET":
        pet.likes = pet.like_set.count()
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pet = pet
            comment.user = UserProfile.objects.get(user=request.user)
            comment.save()
            return redirect("pet details", pet.pk)

    context = {
        "pet": pet,
        "comments": comments,
        "is_liked": is_liked,
        "form": form,
    }
    return render(request, "pets/pet_detail.html", context)


@login_required(login_url=LOGIN_URL)
def like_pet(request, pet_pk):
    pet = Pet.objects.get(pk=pet_pk)
    user_profile = UserProfile.objects.get(user=request.user)

    try:
        like = Like.objects.get(user=user_profile)
        like.delete()
    except ObjectDoesNotExist:
        like = Like(
            pet=pet,
            user=user_profile,
        )
        like.save()

    return redirect('pet details', pet.pk)
