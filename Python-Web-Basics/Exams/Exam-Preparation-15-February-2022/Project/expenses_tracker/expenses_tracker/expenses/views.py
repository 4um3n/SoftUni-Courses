from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from expenses_tracker.expenses.forms import ExpenseForm
from expenses_tracker.expenses.models import Expense
from expenses_tracker.profiles.form import ProfileForm
from expenses_tracker.profiles.models import Profile


# def home(request):
#     profile = Profile.objects.first()
#
#     if request.method == "GET":
#         if profile:
#             expenses = Expense.objects.all()
#             left_money = profile.budget - sum([expense.price for expense in expenses])
#
#             context = {
#                 "budget": profile.budget,
#                 "expenses": expenses,
#                 "left_money": left_money
#             }
#             return render(request, "expenses/home-with-profile.html", context)
#
#         form = ProfileForm()
#     else:
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#
#     context = {
#         "profile_form": form,
#     }
#     return render(request, "expenses/home-no-profile.html", context)


class HomeView(CreateView):
    form_class = ProfileForm
    model = Profile
    template_name = "expenses/home-no-profile.html"

    def get_object(self, queryset=None):
        return self.model.objects.first()

    def get_success_url(self):
        return reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        if self.object is not None:
            expenses = Expense.objects.all()
            left_money = self.object.budget - sum([expense.price for expense in expenses])

            context["budget"] = self.object.budget
            context["expenses"] = expenses
            context["left_money"] = left_money
            return render(request, "expenses/home-with-profile.html", context)

        context["profile_form"] = ProfileForm()
        return render(request, "expenses/home-no-profile.html", context)


# def create_expense(request):
#     if request.method == "GET":
#         form = ExpenseForm()
#     else:
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#
#     context = {"form": form}
#     return render(request, "expenses/expense-create.html", context)


class CreateExpenseView(CreateView):
    template_name = "expenses/expense-create.html"
    form_class = ExpenseForm

    def get_context_data(self, **kwargs):
        context = super(CreateExpenseView, self).get_context_data(**kwargs)
        context["form"] = self.get_form(self.form_class)
        return context

    def get_success_url(self):
        return reverse_lazy("home")


# def edit_expense(request, expense_id):
#     expense = Expense.objects.get(id=expense_id)
#
#     if request.method == "GET":
#         form = ExpenseForm(initial=expense.__dict__)
#     else:
#         form = ExpenseForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#
#     context = {"form": form}
#     return render(request, "expenses/expense-edit.html", context)


class EditExpenseView(UpdateView):
    template_name = "expenses/expense-edit.html"
    form_class = ExpenseForm

    def get_object(self, queryset=None):
        return get_object_or_404(Expense, id=self.kwargs["expense_id"])

    def get_context_data(self, **kwargs):
        context = super(EditExpenseView, self).get_context_data(**kwargs)
        context["form"] = self.get_form(self.form_class)
        return context

    def get_success_url(self):
        return reverse_lazy("home")


# def delete_expense(request, expense_id):
#     expense = Expense.objects.get(id=expense_id)
#
#     if request.method == "GET":
#         form = ExpenseForm(initial=expense.__dict__, disable_fields=True)
#         context = {"form": form}
#         return render(request, "expenses/expense-delete.html", context)
#     else:
#         expense.delete()
#         return redirect("home")


class DeleteExpenseView(DeleteView):
    template_name = "expenses/expense-delete.html"
    form_class = ExpenseForm

    def get_form(self, form_class=None):
        return self.form_class(
            initial=self.object.__dict__,
            disable_fields=True,
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.form_valid(self.get_form(self.form_class))

    def get_object(self, queryset=None):
        return get_object_or_404(Expense, id=self.kwargs["expense_id"])

    def get_success_url(self):
        return reverse_lazy("home")
