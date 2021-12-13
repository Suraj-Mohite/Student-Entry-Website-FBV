from django.urls import path
from FBV_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.display,name='display'),
    path('<int:id>',views.update_data,name='updatedata'),
    path('delete/<int:id>',views.delete_data,name='deletedata'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)