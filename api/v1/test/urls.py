from django.urls import path, include

from api.v1.test.views import *

urlpatterns = [
    path('', test_2, name="test"),
]
