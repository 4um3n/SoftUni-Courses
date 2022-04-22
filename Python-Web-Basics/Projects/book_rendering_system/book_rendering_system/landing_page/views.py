from django.shortcuts import render, redirect
from book_rendering_system.landing_page.models import BookModel
from book_rendering_system.landing_page.forms import BookForm


def show_form(request, template_name, form):
    context = {"form": form}
    return render(request, template_name, context)


def index(request):
    context = {
        "books": BookModel.objects.all(),
    }
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('index')

        return show_form(request, "create.html", form)
    else:
        return show_form(request, "create.html", BookForm())


def edit_book(request, book_id):
    book = BookModel.objects.get(pk=book_id)
    if request.method == "POST":
        form = BookForm(
            request.POST,
            instance=book,
        )
        if form.is_valid():
            form.save()
            return redirect('index')

        return show_form(request, "edit.html", form)
    else:
        form = BookForm(
            initial=book.__dict__,
        )
        return show_form(request, "edit.html", form)

