import logging

from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin

# initialize logger
logger = logging.getLogger(__name__)


class ProtectedPageLoggerMiddleware(MiddlewareMixin):
    """Logs all attempts to access protected page"""

    def process_view(self, request, view_func, view_args, view_kwargs):
        protected_url = ['/']
        if request.path in protected_url and not request.user.is_authenticated:
            logger.warning(f"Unauthorized access attempt to {request.path} from {request.META.get('REMOTE_ADDR')}")
            return redirect("login")


class ErrorHandlerMiddleware(MiddlewareMixin):
    """Logs 404 and 500 errors"""

    def process_exception(self, request, exception):
        logger.error(f"Exception {exception} at {request.path}")
        return render(request, "500.html", status=500)

    def process_response(self, request, response):
        if response.status_code == 404:
            return render(request, "404.html", status=404)
        return response

