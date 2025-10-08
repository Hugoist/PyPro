import fakeredis
import uuid
from datetime import datetime

# imitate connection to Redis
redis_client = fakeredis.FakeStrictRedis()

# Session Time To Live in seconds (30 mins)
SESSION_TTL = 30 * 60


# Create user session
def create_session(user_id: int) -> str:
    session_token = str(uuid.uuid4())
    login_time = datetime.now().isoformat()

    session_key = f"session:{session_token}"
    session_data = {
        "user_id": user_id,
        "login_time": login_time
    }

    redis_client.hset(session_key, mapping=session_data)
    redis_client.expire(session_key, SESSION_TTL)

    return session_token


# Get user's active session
def get_session(session_token: str):
    session_key = f"session:{session_token}"
    if redis_client.exists(session_key):
        return redis_client.hgetall(session_key)
    return None


# Refresh time for user's last activity
def refresh_session(session_token: str):
    session_key = f"session:{session_token}"
    if redis_client.exists(session_key):
        redis_client.expire(session_key, SESSION_TTL)
        redis_client.hset(session_key, "last_active", datetime.now().isoformat())
        return True
    return False


# Delete user's session
def delete_session(session_token: str):
    session_key = f"session:{session_token}"
    return redis_client.delete(session_key)


# Tests
if __name__ == "__main__":
    token = create_session(1)
    print("Created session:", token)

    session = get_session(token)
    print("Session data:", session)

    refresh_session(token)
    print("Session refreshed:", get_session(token))

    delete_session(token)
    print("Session deleted:", get_session(token))
