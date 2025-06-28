"""Security utilities: user extraction."""

from fastapi import Request


# PUBLIC_INTERFACE
def get_current_active_user(request: Request):
    """Extracts current user (from token/session/cookie)."""
    # Placeholder (actual user fetch for endpoints)
    return None
