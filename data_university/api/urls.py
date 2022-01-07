from django.urls import path
from .views import session_detail, session_list

app_name = 'api'

urlpatterns = [
    path('<slug>/', session_detail, name="detail"),
    path('list', session_list, name="list")
]