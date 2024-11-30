from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enquete/', include('enquete.urls', namespace="enquetes")),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:  # uniquement lorsque DEBUG est True
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
