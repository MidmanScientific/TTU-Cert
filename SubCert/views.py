from django.shortcuts import render,redirect
from .models import myData
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import CompanyRequest, AutomaticLogin
import random, string

# View to handle company registration
def registration(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        post_office = request.POST.get('post_office')
        status = request.POST.get('status', 'pending')

        # Save the company request
        CompanyRequest.objects.create(
            company_name=company_name,
            email=email,
            contact=contact,
            location=location,
            post_office=post_office,
            status=status
        )

        # Redirect to the prompt page
        return HttpResponseRedirect(reverse('prompt_page'))

    return render(request, 'registration.html')

# View to display the admin dashboard


# View to handle AJAX request for viewing request details
@csrf_exempt
def view_request_details(request):
    if request.method == 'GET':
        request_id = request.GET.get('request_id')
        if request_id:
            request_details = CompanyRequest.objects.get(id=request_id)
            return JsonResponse({
                'company_name': request_details.company_name,
                'email': request_details.email,
                'contact': request_details.contact,
                'location': request_details.location,
                'post_office': request_details.post_office
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)

# View to handle confirmation of a company request
from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import random, string
from .models import CompanyRequest, AutomaticLogin
from .models import myVerification
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import random, string
from .models import CompanyRequest, AutomaticLogin

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import random, string
from .models import CompanyRequest, AutomaticLogin

def confirm_request(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        if request_id:
            request_details = get_object_or_404(CompanyRequest, id=request_id)
            # Generate automatic login credentials
            username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            # Save the login credentials
            AutomaticLogin.objects.create(
                Username=username,
                Password=password
            )
            # Update the request status
            request_details.status = 'confirmed'
            request_details.save()
            # Store credentials in session
            request.session['username'] = username
            request.session['password'] = password
            request.session['request_id'] = request_id
            # Redirect to the prompt page
            return HttpResponseRedirect(reverse('prompt_page'))
    return JsonResponse({'error': 'Invalid request'}, status=400)

def prompt_page(request):
    request_id = request.session.get('request_id')
    context = {
        'request_id': request_id,
    }
    return render(request, 'prompt-page.html', context)

def check_request_status(request):
    request_id = request.session.get('request_id')
    if request_id:
        request_details = get_object_or_404(CompanyRequest, id=request_id)
        if request_details.status == 'confirmed':
            username = request.session.pop('username', None)
            password = request.session.pop('password', None)
            return JsonResponse({
                'request_confirmed': True,
                'username': username,
                'password': password
            })
    return JsonResponse({'request_confirmed': False})


def myAdmin(request):
    requests = CompanyRequest.objects.all()
    return render(request, 'Admin.html', {'requests': requests})

def Admin_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        if myData.objects.filter(username=username,password=password).exists():
            return redirect('myAdmin')
        else:
            error_message = 'username or password incorrect'
            return render(request,'Admin-login.html',{'error_message':error_message})
    else:
        return render (request,'Admin-login.html')    



def login (request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        if AutomaticLogin.objects.filter(Username=username,Password=password).exists():
            return redirect('verification')
        else:
            failed_message='Incorrect username or password'
            return render(request,'login.html',{'failed_message':failed_message})
    
    return render(request,'login.html')



def verification(request):
    if request.method == 'POST':
        unique_number = request.POST['unique_number']
        try:
            details = myVerification.objects.get(unique_number=unique_number)
            return render(request, 'result.html', {'details': details})
        except myVerification.DoesNotExist:
            # Pass an error message to the template if the unique number is not found
            return render(request, 'result.html', {'error_message': 'Result not found'})
    return render(request, 'verification.html')

def result (request):
    return render (request,'result.html')

def homepage(request):
    return render(request,'homepage.html')