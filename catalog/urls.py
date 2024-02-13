from django.urls import path

from catalog.views import home, contacts

# указываем контроллеры home и contacts
urlpatterns = [
    path('',home, name='home'),
    path('contacts', contacts, name='contacts')
]