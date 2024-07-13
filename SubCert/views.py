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
@csrf_exempt
def confirm_request(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        if request_id:
            request_details = CompanyRequest.objects.get(id=request_id)
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
            # Redirect to the prompt page with the request ID
            return HttpResponseRedirect(reverse('prompt_page') + '?request_id=' + request_id)
    return JsonResponse({'error': 'Invalid request'}, status=400)

# View to display the prompt page
def prompt_page(request):
    request_id = request.GET.get('request_id')
    if request_id:
        request_details = CompanyRequest.objects.get(id=request_id)
        if request_details.status == 'confirmed':
            # Retrieve the login credentials
            login_credentials = AutomaticLogin.objects.last()
            return render(request, 'prompt-page.html', {
                'request_confirmed': True,
                'username': login_credentials.Username,
                'password': login_credentials.Password
            })
    return render(request, 'prompt-page.html', {'request_confirmed': False})

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
    return render(request,'login.html')