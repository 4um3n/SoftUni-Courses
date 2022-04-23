from django.http import HttpResponse
from django.shortcuts import render, redirect


def groups_required(*allowed_groups):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect("sign in")
            if allowed_groups and not user.groups.exists():
                return render(request, "errors/error_401.html")

            user_groups_names = [g.name for g in user.groups.all()]
            intersecting_groups = set(user_groups_names).intersection(allowed_groups)

            if allowed_groups and not intersecting_groups:
                return render(request, "errors/error_401.html")

            return function(request, *args, **kwargs)
        return wrapper
    return decorator
