from xmlrpc.client import boolean
from django.shortcuts import redirect
from django.http import HttpResponse




def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            bool = False
            if request.user.groups.exists():
                for g in request.user.groups.all():
                    if g.name in allowed_roles:
                        bool = True
                        break
            
            if bool == True:
                return view_func(request, *args, **kwargs)
                        
            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator
