from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from shipmentsService.settings import URL_PREFIX


class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super(CustomSchemaGenerator, self).get_schema(request, public)
        schema.host = self.get_host(request)
        schema.schemes = ["http", "https"]
        return schema

    @staticmethod
    def get_host(request):
        return request.META.get("HTTP_ORIGIN") or request.get_host()


schema_view = get_schema_view(
    openapi.Info(title="shipmentsService", default_version="v0.1"),
    generator_class=CustomSchemaGenerator,
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{URL_PREFIX}/', include('shipments.urls')),
    re_path(
        r"swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
