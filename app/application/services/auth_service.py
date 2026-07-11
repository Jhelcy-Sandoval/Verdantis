from app.infrastructure.auth.supabase_client import supabase

class AuthService:

    def register(
        self,
        email,
        password
    ):

        return supabase.auth.sign_up(
            {
                "email": email,
                "password": password
            }
        )
      
    def login(
        self,
        email,
        password
    ):

        return supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )     

    def logout(self):
        return supabase.auth.sign_out()

