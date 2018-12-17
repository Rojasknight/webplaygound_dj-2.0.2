from django.urls import path
from . import views
from pages.views import PagesListView, PageDetailView, PageCreate, PageUpdate, PageDelete
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'pages'

urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    path('create/', staff_member_required(PageCreate.as_view()), name='create'),
    path('update/<int:pk>/', staff_member_required(PageUpdate.as_view()), name='update'),
    path('delete/<int:pk>/', staff_member_required(PageDelete.as_view()), name='delete'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]
