from django.shortcuts import render
from .ml_model import HousePricePredictor
from .ml2_model import PostQualityPredictor

def predict_price(request):
    prediction = None
    if request.method == 'POST':
        try:
            size = float(request.POST.get('size'))
            bedrooms = int(request.POST.get('bedrooms'))
            age = float(request.POST.get('age'))
            
            predictor = HousePricePredictor()
            prediction = predictor.predict(size, bedrooms, age)
        except (ValueError, TypeError):
            prediction = "Invalid input"
    
    return render(request, 'predict.html', {'prediction': prediction})
def predict_rep(request):
    prediction = None
    if request.method == 'POST':
        try:
            user_reputation = int(request.POST.get('reputation'))
            mpxr = float(request.POST.get('mpxr'))
            
            predictor = PostQualityPredictor()
            prediction = predictor.reputation_pridict(user_reputation, mpxr)
            return render(request, 'reputation.html', {
                'user_reputation': user_reputation,
                'mpxr':mpxr,
                'prediction': prediction
            })
        except (ValueError, TypeError):
            prediction = "Invalid input"
    
    return render(request, 'reputation.html', {'prediction': prediction})
