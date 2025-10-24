from django.shortcuts import render
from django.views import View
from datetime import date


def home(request):
    """Display the home page"""

    context = {
        "title": "Головна",
        "today": date.today(),
    }
    return render(request, "home.html", context)


def about(request):
    """Display the about page"""

    context = {
        "title": "Про нас",
        "description": "Слідуй за нами, роби як ми",
        "updated": date.today(),
    }
    return render(request, "about.html", context)


class ContactView(View):
    """Display the contact page"""

    def get(self, request):
        context = {
            "title": "Контакти",
            "email": "info@example.com",
            "phone": "+380 44 123 45 67",
            "address": "м.Одеса, вул.Фонтанська дорога, 10",
        }
        return render(request, "contact.html", context)


class ServiceView(View):
    """Display the services page"""

    def get(self, request):
        services = [
            {"name": "Розробка сайтів", "desc": "Створення сучасних веб-застосунків."},
            {"name": "Підтримка та обслуговування", "desc": "Технічна підтримка вашого сайту."},
            {"name": "SEO-оптимізація", "desc": "Покращення видимості сайту в пошукових системах."},
        ]

        context = {
            "title": "Послуги",
            "services": services,
            "updated": date.today(),
        }
        return render(request, "services.html", context)
