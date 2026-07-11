from uuid import uuid4
from app.infrastructure.auth.supabase_client import supabase

class SupabaseStorage:

    BUCKET = "plantas"

    def upload_image(self, file):

        extension = file.filename.split(".")[-1]

        filename = f"{uuid4()}.{extension}"

        supabase.storage.from_(self.BUCKET).upload(
            filename,
            file.read(),
            {
                "content-type": file.content_type
            }
        )

        return supabase.storage.from_(
            self.BUCKET
        ).get_public_url(filename)