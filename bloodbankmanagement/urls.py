from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from blood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donor/', include('donor.urls')),
    path('patient/', include('patient.urls')),
    path('', views.home_view, name='home'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('availabledonor', views.available_donor, name='available_donor'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('search', views.search, name='search'),
    path('makeRequest/<int:id>/', views.makeRequest, name="makeRequest"),
]