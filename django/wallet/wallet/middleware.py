import re

from django.conf import settings
from django.shortcuts import redirect

from account.models import User

EXEMPT_URLS = [re.compile(settings.LOGIN_URL)]
if hasattr(settings, 'EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.EXEMPT_URLS]


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # noinspection PyBroadException,PyUnusedLocal
    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        """Checks that the requested view is public or that the user is logged in otherwise,
        redirects the user to the login page.

        :param request: Object containing the web request
        :param view_func: django python function
        :param view_args: list of positional parameters that will be transmitted to the view
        :param view_kwargs: dictionary of named parameters that will be transmitted to the view
        :return: none if the user has the right to access the view otherwise render to the login page
        """
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
