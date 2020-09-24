from django_multitenant.utils import set_current_tenant

class MultitenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user and not request.user.is_anonymous:
            set_current_tenant(request.user.employee.company)
        return self.get_response(request)
    
    