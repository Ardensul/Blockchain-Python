# noinspection PyBroadException
def middleware_login(request):
    try:
        if not request.session["user"].check_key():
            return True
    except:
        return False
