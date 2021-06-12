from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_offers = {
    "Jan" : "New Model MSI Products Coming Soon!" ,
    "Feb" :  "Zebronic Speaker sales" , 
    "March" : "Iphone deals avilable" ,
    "April" : "MSI Motherboard Offer with ANT Esports mouse kit",
    "May" : "Oneplus headset sales" ,
    "June" : "CASIO watches offer upto 50% discount",
    "July" : "Realme Products offers",
    "Aug" : "Iphone deals avilable" ,
    "Sep" : "VIVO/OPPO best deals" ,
    "Oct" : "Sony music box deals",
    "Nov" : " Offer upto 50-60% Discount on any products",
    "Dec" : "End sale "
}

def cart(request):
    list_items = ""
    months = list(monthly_offers.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-deals", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul><h1>{list_items}</h1></ul>"
    return HttpResponse(response_data)

def monthly_deals_by_number(request, month):
    months = list(monthly_offers.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-deals", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_deals(request, month):
    try:
        product_text = monthly_offers[month]
        data_deals = f"<h1>{product_text}</h1>"
        return HttpResponse(data_deals)

    except:
        return HttpResponseNotFound("<h1>Page Not found Bro!</h1>")

    return HttpResponse(product_text)