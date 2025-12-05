from django.urls import path
from .views import CreateShortLinkView

urlpatterns = [
    path('create/',CreateShortLinkView.as_view(),name="create_shoort_link"),
]