from django.urls import path
from . import views
from pages.views import PagesListView, PageDetailView, PageCreate, PageUpdate, PageDelete

app_name = 'pages'

urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]
