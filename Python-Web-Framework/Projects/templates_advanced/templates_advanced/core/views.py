from django.shortcuts import render


def render_page_with_form(request, template_name, form):
    context = {"form": form}
    return render(request, template_name, context)
