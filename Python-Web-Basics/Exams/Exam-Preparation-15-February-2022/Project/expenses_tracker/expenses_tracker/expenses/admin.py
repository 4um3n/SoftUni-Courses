from django.contrib import admin
from expenses_tracker.expenses.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
