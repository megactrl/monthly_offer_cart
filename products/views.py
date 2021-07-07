from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

monthly_offers = {
    "Jan" : "Model MSI New Products Coming Soon!" ,
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
    "Dec" : None
}

def cart(request):
    months = list(monthly_offers.keys())

    return render(request,"products/index.html",{
        "months": months,
     })

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
        return render(request, "products/offers.html", {
            "text": product_text ,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)



