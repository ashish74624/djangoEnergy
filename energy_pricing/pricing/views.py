from django.shortcuts import render
from .models.ai_model import EnergyPricingModel
from django.http import JsonResponse

# Initialize model instance (in real deployment, load a pre-trained model)
pricing_model = EnergyPricingModel()

def get_price_prediction(request):
    if request.method == 'POST':
        # Get the values from the form
        supply = float(request.POST.get('supply'))
        demand = float(request.POST.get('demand'))
        storage = float(request.POST.get('storage'))
        
        # Make prediction
        price = pricing_model.predict_price(supply, demand, storage)

        # Pass the price to the template
        return render(request, 'pricing_form.html', {'price': price})

    return render(request, 'pricing_form.html')


def pricing_dashboard(request):
    return render(request, 'pricing_form.html', {'initial_price': 50})

def update_price(request):
    supply = int(request.GET.get('supply', 100))
    demand = int(request.GET.get('demand', 100))
    storage = int(request.GET.get('storage', 100))
    
    price = pricing_model.predict_price(supply, demand, storage)
    
    return JsonResponse({'price': price})