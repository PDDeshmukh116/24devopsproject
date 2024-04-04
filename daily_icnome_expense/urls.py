
from django.contrib import admin
from django.urls import path,include
from account.views import home
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path("acc-",include(("account.urls",'account'),namespace='account')),
    path("inc-",include(("income.urls",'income'),namespace='income')),
    path("exp-",include(("expense.urls",'expense'),namespace='expense')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
