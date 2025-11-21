import logging

from django.conf import settings


class CustomHeaderMiddleware:
    """Middleware that adds a custom header"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Custom-Header'] = 'HelloWorld'
        return response


logger = logging.getLogger('custom')


class MetricsMiddleware:
    """Middleware that count requests"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        settings.REQUEST_COUNT += 1
        logger.info(f"Request #{settings.REQUEST_COUNT} to {request.path}")
        response = self.get_response(request)
        return response
