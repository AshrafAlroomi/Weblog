from django.urls import path, include

urlpatterns = [
    path('test/', include("api.v1.test.urls"))
]
