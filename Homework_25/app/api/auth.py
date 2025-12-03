from django.contrib.auth import authenticate
from ninja import Router
from ninja.security import HttpBearer
from app.models.auth import UserToken

auth_router = Router(tags=["Auth"])

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            user_token = UserToken.objects.get(key=token)
            request.user = user_token.user
            return user_token.user
        except UserToken.DoesNotExist:
            return None

auth = AuthBearer()

@auth_router.post("/login")
def login(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if not user:
        return {"error": "Invalid credentials"}

    token, _ = UserToken.objects.get_or_create(user=user)
    return {"token": token.key}
