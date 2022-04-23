from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import groups_required


@login_required()
def index(request):
    pythons = Python.objects.all()
    return render(request, 'pythons_app/index.html', {'pythons': pythons})


@method_decorator(login_required, name="dispatch")
class IndexView(ListView):
    template_name = "pythons_app/index.html"
    model = Python
    context_object_name = "pythons"

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request=request, *args, **kwargs)


@login_required()
@groups_required("User")
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'pythons_app/create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'pythons_app/create.html', {'form': form})


create_required = (
    login_required,
    groups_required("User")
)


@method_decorator(create_required, name="dispatch")
class CreatePythonView(CreateView):
    template_name = "pythons_app/create.html"
    model = Python
    fields = '__all__'
    success_url = reverse_lazy("index")

