from django.shortcuts import render

# Create your views here.

tax_rate = 0.15

def default(request):
    return render(request,'taxcalculator/default.html')
    

def total_price(request, price):
    return render(request,'taxcalculator/total_price.html',{"price":float(price) + (float(price) * tax_rate)})
    

def rate(request):
    return render(request,'taxcalculator/rate.html',{"rate": tax_rate * 100 })
