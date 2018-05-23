from django.conf.urls import url
from number import views
urlpatterns = [
    url(r'^', views.number, name='number'),
]
