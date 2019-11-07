# imports module and function to manager URLs for the admin site
from django.contrib import admin
from django.urls import path, include

# defines the urlpatterns variable
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
]

