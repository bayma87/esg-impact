from django.shortcuts import redirect


class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/painel-secreto/'):
            if not request.user.is_authenticated or not request.user.is_staff:
                return redirect('home')
        return self.get_response(request)
