from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('fbvapp.urls')),
    path('api/',include('fbvapp2.urls')),
    path('api/',include('fbvapp3.urls'))
]
