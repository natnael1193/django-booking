from django.core.exceptions import PermissionDenied
from account.serializer import RegisterSerializer, UserSerializer, SignupSerializer
from account.models import User
from .response import unAuthorizedResponse


def user_is_admin_or_super_admin(function):
    def wrap(request, *args, **kwargs):
        try:
            user_serializer = UserSerializer(User.objects.get(username=request.user))
        except:
            return unAuthorizedResponse()

        if user_serializer.data['is_superuser'] or user_serializer.data['is_admin']:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
