from django.urls import path
from expenses_tracker.expenses.views import CreateExpenseView, EditExpenseView, DeleteExpenseView, HomeView
from expenses_tracker.expenses import signals

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create/", CreateExpenseView.as_view(), name="create expense"),
    path("edit/<int:expense_id>", EditExpenseView.as_view(), name="edit expense"),
    path("delete/<int:expense_id>", DeleteExpenseView.as_view(), name="delete expense"),
]
