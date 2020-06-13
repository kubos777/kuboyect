from django.urls import path
from api.views import PublicationList
from api.api import UserAPI

urlpatterns = [
    path('create_user/', UserAPI.as_view(), name="api_create_user"),
    path('publications/', PublicationList.as_view(), name='publication_list'),
    
]