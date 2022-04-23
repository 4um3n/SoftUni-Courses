from django.shortcuts import render

# Create your views here.


def render_page_with_form(request, template_name, form):
    context = {"form": form}
    return render(request, template_name, context)


def landing_page(request):
    return render(request, 'common/landing_page.html')
