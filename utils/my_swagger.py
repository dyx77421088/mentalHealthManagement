from drf_yasg import openapi


def request_body(properties, required=None):
    return openapi.Schema(
        description="python/Django",
        title="大学生心理管理系统",
        type=openapi.TYPE_OBJECT,
        required=required,
        properties=properties
    )


def string_schema(description=None, default=None, title=None, f=None):
    return openapi.Schema(type=openapi.TYPE_STRING, description=description, default=default, title=title, format=f)


def integer_schema(description=None, default=None, title=None):
    return openapi.Schema(type=openapi.TYPE_INTEGER, description=description, default=default, title=title)
