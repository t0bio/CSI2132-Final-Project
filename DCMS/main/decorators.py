from django.shortcuts import redirect
from django.http import HttpResponse


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator


def redirect_view(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'receptionist':
            return redirect('receptionist')

        if group == 'employee':
            return redirect('employee')
        
        if group == 'patient':
            return redirect('patientUI')

    return wrapper_function
