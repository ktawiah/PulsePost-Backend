from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="PulsePost API Documentation",
        default_version="v1",
        description="API for PulsePost blog platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            name="Kelvin Tawiah",
            email="kelvintawiah224@gmail.com",
            url="https://kelvintawiahdev.vercel.app/",
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
