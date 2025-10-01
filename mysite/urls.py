from django.contrib import admin
from django.urls import path
from acct_management.views import login_view, dashboard, logout_view
from pages.views import page_1, page_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page-1/', page_1, name='page-1'),
    path('page-2/', page_2, name='page-2'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('dashboard/', dashboard, name='dashboard'),
]
