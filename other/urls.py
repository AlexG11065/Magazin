from django.urls import path
from .views import CurrentDateView, RandomCountView, HelloWordView, IndexView

# app = 'other'

urlpatterns = [
    path('datatime/', CurrentDateView.as_view()),  # регистрация маршрута представления CurrentDateView
    path('random/', RandomCountView.as_view()),
    path('other/hello/', HelloWordView.as_view()),
    path('', IndexView.as_view()),
]


