from django.urls import path
from django.conf.urls import url
from .views import login_page, submit_data, router, logout, smiley

app_name = "login"

urlpatterns = [
    url(r'^form/', login_page, name="login_form"),
    url(r'^submit$', submit_data, name="submit" ),
    url(r'^router$', router, name="router" ),
    url(r'^logout$', logout, name="logout" ),
    url(r'^smiley$', smiley, name="smiley" ),
    

]