from django.shortcuts import render, redirect
from online_library.common.forms import ProfileForm, BookForm
from online_library.common.models import Profile, Book


def home_page(request):
    profile = Profile.objects.first()
    books = Book.objects.all()
    context = {
        "profile": profile,
        "books": books,
    }

    if request.method == "GET":
        if profile is None:
            context = {"form": ProfileForm()}
            return render(request, "home-no-profile.html", context)
        return render(request, "home-with-profile.html", context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "home-no-profile.html", context)


def add_book(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {
            "profile": profile,
            "form": BookForm(),
        }
        return render(request, "add-book.html", context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = profile
            book.save()
            return redirect("home")


def edit_book(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    profile = Profile.objects.first()

    if request.method == "GET":
        form = BookForm(initial=book.__dict__)
        context = {
            "profile": profile,
            "form": form,
        }
        return render(request, "edit-book.html", context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("home")


def book_details(request, book_pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=book_pk)

    if request.method == "GET":
        context = {
            "profile": profile,
            "book": book,
        }
        return render(request, "book-details.html", context)


def profile_page(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {
            "profile": profile,
        }
        return render(request, "profile.html", context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = ProfileForm(initial=profile.__dict__)
        context = {
            "profile": profile,
            "form": form,
        }
        return render(request, "edit-profile.html", context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = ProfileForm(initial=profile.__dict__, disable_fields=True)
        context = {"form": form}
        return render(request, "delete-profile.html", context)
    else:
        profile.delete()
        return redirect("home")


def delete_book(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    book.delete()
    return redirect("home")
