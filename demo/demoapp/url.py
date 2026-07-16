from django.urls import path
from.import views

urlpatterns = [
    path('', views.hello_world),
    path('india',views.helloindia.as_view()),
    path('reservation',views.home)
]