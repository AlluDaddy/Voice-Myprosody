from django.urls import path
from django.urls.resolvers import URLPattern


from . import views

urlpatterns = [
    path('', view = views.view_for_prosd, name="prosd"),
    path('prosd', view = views.view_for_prosd, name="prosd"),
    path('prosd/out', view = views.out, name="out"),
    path('out', view = views.out, name="out")
]