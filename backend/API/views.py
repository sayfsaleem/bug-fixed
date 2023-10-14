from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import * 
from django.contrib.auth.decorators import login_required
import json 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password




User = get_user_model()

########################################       USER LOGIN VIEW               ################################

@csrf_exempt
def Login(request):

    message = None
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            print(password)
            print(email)

            user = User.objects.get(email=email)

            if user.check_password(password):
                print(user)
                if user is not None:
                    login(request, user)                
                    message = 'Successfully created your Account'            
            else:
                print("Hello World")

    except Exception as Error:
        message = Error


    response = JsonResponse({'message': message})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Replace with your frontend URL
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

    return response

########################################       REGISTRATION VIEW               ################################


@csrf_exempt
def Register(request):
    status = False 
    message = None

    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            new_user = User(
                username=email,
                email=email,
                password=password
            )

            new_user.save()
            login(request, new_user)
            
            message = 'Successfully created your Account'            

    except Exception as Error:
        message = Error


    response = JsonResponse({'message': message})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Replace with your frontend URL
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

    return response


########################################    CREATE SELLER PROFILE VIEW               ################################


@login_required(login_url='login')
def Create_Seller_Profile(request):

    status = False
    current_user = request.user 

    existing_seller_profile = SellerProfile.objects.filter(user=current_user).exists()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        seller_img = request.FILES.get('seller_profile_img')
        seller_desc = request.POST.get('seller_desc')
        business_title = request.POST.get('business_title')
        business_desc = request.POST.get('business_desc')

        if current_user and first_name and last_name and seller_img and seller_desc and business_title and business_desc:

            if not existing_seller_profile:

                new_seller = SellerProfile.objects.create(
                    user=current_user,
                    first_name=first_name,
                    last_name=last_name,
                    seller_desc=seller_desc,
                    img=seller_img,
                    business_title=business_title,
                    business_desc=business_desc,
                )
                new_seller.save()
                status = True
            else:

                status = "User has a Seller Profile already."
        else:

            status = False

    return JsonResponse({'response': status})




########################################    CREATE PRODUCT VIEW               ################################


@csrf_exempt
def CreateProduct(request):

    message = None

    user = request.user 

    if request.method == 'POST':

        message = "Someone made a Post request to create a product"

        title = request.POST.get('title')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        desc = request.POST.get('desc')

        try:
            new_product = Product.objects.create(
                user=user,
                title=title,
                category=category,
                quantity=quantity,
                price=price,
                desc=desc
            )

            new_product.save()       

            message = "success"
        except Exception as e:
            message = 'Error'


    response = JsonResponse({'message': message})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Replace with your frontend URL
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

    return response 



########################################    CREATE PRODUCT VIEW               ################################

def CurrentUser(request):

    user = None
    status = False 

    str_user = str(request.user)

    if request.user:
        print(request.user)
        status = True
        user = {
            "id" : request.user.id,
            "email": request.user.email,
        }



    response = JsonResponse({'loggedIn': status, 'user':user })
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Replace with your frontend URL
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

    return response 






