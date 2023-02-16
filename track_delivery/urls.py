from django.urls import path

from . import views

app_name = 'track_delivery'

urlpatterns = [
    path(
        route='', 
        view=views.index,
        name='index'
    ),
    path(
        route='contact', 
        view=views.contact,
        name='contact'
    ),
    path(
        route='track/',
        view=views.track_package,
        name='track'
    )
]