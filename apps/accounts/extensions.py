from drf_spectacular.authentication import OpenApiAuthenticationExtension


class CustomJWTAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = "apps.accounts.authentication.CustomJWTAuthentication"
    name = "JWT Auth"

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "name": "Authorization",
            "description": "JWT token",
        }
