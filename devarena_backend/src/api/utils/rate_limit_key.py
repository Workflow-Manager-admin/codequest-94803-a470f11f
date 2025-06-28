"""Custom key for rate limiter (by user/IP)."""

from fastapi import Request


# PUBLIC_INTERFACE
def rate_limit_key_func(request: Request):
    """Returns key for rate limiting: use user id or IP."""
    return request.client.host
