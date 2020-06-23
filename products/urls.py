from django.urls import path
from .views import ItemsWithCategoryListView, ItemDetailView, ItemsListView, ItemsWithTopicListView, ItemsWithTagListView
from . import views

urlpatterns = [
    path('', ItemsListView.as_view(), name = 'products-all'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name = 'item-detail'),
    path('category/<str:category>', ItemsWithCategoryListView.as_view(), name = 'products-category'),
    path('tag=<str:tag>', ItemsWithTagListView.as_view(), name = 'products-tag'),
    path('topic/<str:topic>', ItemsWithTopicListView.as_view(), name = 'products-topic'),
]