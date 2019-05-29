import re

from django.conf import settings
from django.shortcuts import redirect

from api.models import User

EXEMPT_URLS = [re.compile(settings.LOGIN_URL)]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # noinspection PyBroadException
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, "user")
        path = request.path_info
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        if url_is_exempt:
            return None
        else:
            try:
                if request.session["user"]:
                    user = User(request.session["user"])
                    if user.is_valid() and user.check_key():
                        return None
                    else:
                        return redirect(settings.LOGIN_URL)
                else:
                    return redirect(settings.LOGIN_URL)
            except:
                return redirect(settings.LOGIN_URL)
