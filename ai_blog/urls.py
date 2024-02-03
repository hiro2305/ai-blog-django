from django.contrib import admin
from django.urls import path, include
from ai_web.views import test_orm

urlpatterns = [
    path('admin/',admin.site.urls),
    path('artykuly/', include('ai_web.urls')),
    path('test-orm/', test_orm)

]
