from django.urls import path
from . import views

app_name = 'connections'

urlpatterns = [
    path(
        'data-source/',
        views.DataSourceAPIView.as_view(),
        name="data-source"
    ),
]
