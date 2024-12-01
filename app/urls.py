from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    path(
        "openapi",
        get_schema_view(
            title="Navako", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
