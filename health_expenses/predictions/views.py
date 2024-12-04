from django.shortcuts import render, redirect
import pandas as pd 
from .models import Prediction
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.
# predictions/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import PredictionForm
from .utils import load_model, load_preprocessor
import os

# Carregar o modelo pickle
#MODEL_PATH = "C:/Users/Usuario/Desktop/Projects/ML_Health_expenses/health_expenses/pickle/model.pkl"
#REPROCESSOR_PATH = "C:/Users/Usuario/Desktop/Projects/ML_Health_expenses/health_expenses/pickle/preprocessor.pkl"
MODEL_PATH = os.path.join(os.getcwd(), "pickle", "model.pkl")
PREPROCESSOR_PATH = os.path.join(os.getcwd(), "pickle", "preprocessor.pkl")

preprocessor = load_preprocessor(PREPROCESSOR_PATH)
model = load_model(MODEL_PATH)


def index(request):
    return render(request, 'index.html')

@login_required
def model_predict(request):
    user_predictions = Prediction.objects.filter(user=request.user)
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Captura os dados do formulário
            sex = form.cleaned_data['sex']
            age = form.cleaned_data['age']
            region = form.cleaned_data['region']
            children = form.cleaned_data['children']
            smoker = form.cleaned_data['smoker']
            bmi = form.cleaned_data['bmi']

            user_input = {
            "sex": sex, 
            "age": age, 
            "region": region, 
            "children": children, 
            "smoker": smoker,
            "bmi": bmi      
            }
            new_data = pd.DataFrame([user_input])

            
            # Pré-processar os dados com o pré-processador salvo
            processed_data = preprocessor.transform(new_data)    

            # Fazer a previsão com o modelo treinado
            predicted_cost = model.predict(processed_data)
            predicted_cost = round(float(predicted_cost[0][0]), 2)

            # saving into the databse
            Prediction.objects.create(
            user = request.user,
            sex=sex,
            age=age,
            region=region,
            children=children,
            smoker=smoker,
            bmi=bmi,
            predicted_cost=predicted_cost,
            )

            # Retorne a previsão como JSON
            return JsonResponse({'predicted_cost': predicted_cost})

    else:
        form = PredictionForm()
    return render(request, 'prediction.html', {'form': form, "user_predictions": user_predictions})

def delete_prediction(request, id):
    get_todo = Prediction.objects.get(user = request.user, id = id)
    get_todo.delete()
    return redirect("model_predict")

@login_required
def clear_all_predictions(request):
    if request.method == 'POST':
        try:
            # Delete all predictions for the current user
            Prediction.objects.filter(user=request.user).delete()
            return JsonResponse({'message': 'All predictions cleared successfully!'})
        except Exception as e:
            return JsonResponse({'error': f'Failed to clear predictions: {str(e)}'}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


# Registro de um novo usuário
def user_signup(request):

    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the home or prediction page
        return redirect('index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# Login do usuário
def user_login(request):

    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the home or prediction page
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('model_predict')  # Redirect para a página inicial ou onde você deseja
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')