from .views import SignupView, IndexView, DetailView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "user_data"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:val>', views.DetailView, name='detail'),
    path('signup/', SignupView.as_view(), name='signup')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
