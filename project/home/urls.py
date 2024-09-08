
from django.urls import path, include
from .views import BookListView, BookDetails, ContactView
urlpatterns = [
    path('', BookListView.as_view(), name='home' ),
    path('details/<int:id>/', BookDetails.as_view(), name='details' ),
    path('contact/', ContactView.as_view(), name='contact' ),
]
