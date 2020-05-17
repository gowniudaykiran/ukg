from django.http import HttpResponse
from django .shortcuts import redirect
from django.contrib.auth.models import Group

def allowed_users(allowed_roles=[]):
    def decorator(fun):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return fun(request,*args,**kwargs)

            else:
                return HttpResponse('<h1>You are not authorised to view this page</h1>')
            
            return fun(request,*args,**kwargs)
        return wrapper_func
    return decorator
