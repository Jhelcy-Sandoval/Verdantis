from functools import wraps

from flask import redirect
from flask import url_for

from app.infrastructure.auth.supabase_client import supabase


def login_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        try:

            user = supabase.auth.get_user()

            if not user or not user.user:

                return redirect(
                    url_for("auth.login")
                )

        except Exception:

            return redirect(
                url_for("auth.login")
            )

        return view(*args, **kwargs)

    return wrapped_view