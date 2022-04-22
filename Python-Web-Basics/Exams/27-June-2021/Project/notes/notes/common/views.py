from django.shortcuts import render, redirect
from notes.common.forms import ProfileForm, NoteForm
from notes.common.models import Profile, Note


def render_page_with_form(request, template_name, form):
    context = {"form": form}
    return render(request, template_name, context)


def home(request):
    user = Profile.objects.first()

    if request.method == "GET":
        if user is None:
            return render_page_with_form(request, "home-no-profile.html", ProfileForm)
        else:
            context = {"notes": Note.objects.all()}
            return render(request, "home-with-profile.html", context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render_page_with_form(request, "home-no-profile.html", form)


def add_note(request):
    if request.method == "GET":
        return render_page_with_form(request, "note-create.html", NoteForm())
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = Profile.objects.first()
            note.save()
            return redirect("home")
        return render_page_with_form(request, "note-create.html", form)


def edit_note(request, note_pk):
    note = Note.objects.get(pk=note_pk)

    if request.method == "GET":
        return render_page_with_form(request, "note-edit.html", NoteForm(initial=note.__dict__))
    else:
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render_page_with_form(request, "note-edit.html", form)


def delete_note(request, note_pk):
    note = Note.objects.get(pk=note_pk)

    if request.method == "GET":
        form = NoteForm(
            initial=note.__dict__,
            disable_fields=True
        )
        return render_page_with_form(request, "note-delete.html", form)
    else:
        note.delete()
        return redirect("home")


def note_details(request, note_pk):
    note = Note.objects.get(pk=note_pk)

    if request.method == "GET":
        context = {"note": note}
        return render(request, "note-details.html", context)
    else:
        pass


def profile(request):
    if request.method == "GET":
        context = {
            "user": Profile.objects.first(),
            "notes_count": Note.objects.count(),
        }
        return render(request, "profile.html", context)
    else:
        pass


def delete_profile(request):
    user = Profile.objects.first()
    user.delete()
    return redirect("home")
