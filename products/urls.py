from django.urls import path
from . import views 


urlpatterns = [
    path("", views.cart),
    path("<int:month>", views.monthly_deals_by_number),
    path("<str:month>", views.monthly_deals, name="monthly-deals")
]
