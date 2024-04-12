from django.urls import path
from login.views import LoginIndexView

urlpatterns = [
    path('', LoginIndexView.as_view()),
]
