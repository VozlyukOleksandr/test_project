from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/', login_form),
    url(r'^registration/', registr_form),
    url(r'^index/', Index.as_view()),
]