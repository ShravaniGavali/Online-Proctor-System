from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from usersite.views import submit_personalinfo

urlpatterns = [
    # path('',views.home_view),
    path('',views.adm_details),
    path('personal_details/',views.personal_details),
]