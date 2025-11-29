from django.core.cache import cache


class AnonymousBookListCacheMiddleware:
    """
    Cache book list page for anonymous users
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated or request.path != "/books_list/":
            return self.get_response(request)

        cache_key = f"anon_page:{request.path}"
        response = cache.get(cache_key)
        if response:
            return response

        response = self.get_response(request)
        cache.set(cache_key, response, 60 * 5)
        return response
