from django.shortcuts import render
from django.http import HttpResponse

# for signing/register
from .models import Feature
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    # feature = Feature() i commented them out because i can have createb it database
    # feature.id = 0S
    # feature.name = 'Fast'
    # feature.is_true = True
    # feature.details = 'Our services is very quick'
    
    # feature1 = Feature()
    # feature1.id = 1
    # feature1.name = 'Reliable'
    # feature1.is_true = True
    # feature1.details = 'Our services is very Reliable'
    
    # feature2 = Feature()
    # feature2.id = 2
    # feature2.name = 'Easy To Use'
    # feature2.is_true = True
    # feature2.details = 'Our services is easy to use'
    
    # feature3 = Feature()
    # feature3.id = 3
    # feature3.name = 'Affordable'
    # feature3.is_true = False
    # feature3.details = 'Our services is very Affordable'
    # features = [feature, feature1, feature2, feature3]
    
    features = Feature.objects.all()
    # since the model is imported i will create new variable to pick the object
    
    
    context = {
        'name' : "Umar",
        'age' : "43",
        'Nationality' : "Nigerian"
        
    }
    return render(request, 'index.html', {'features': features})
    # return render(request, 'index.html')
    # return render(request, 'index.html', context)
    # return render(request, 'index.html', {'name': 'aba'})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not the Same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)
            return redirect('/')
        else:
            messages.info(request, 'Credential Invalid')
            return redirect('login')
            
        # if username_sign == User.objects.filter(username_sign=username_sign).exists():
        #     messages.info(request, 'Wrong Username')
        #     return redirect('login')
        # elif pass_sign == User.objects.filter(pass_sign=pass_sign):
        #     messages.info(request, 'Wrong Password')
        #     return redirect('login')
        # else:
        #     messages.info(request,'Login successful')
        #     return redirect('register')
        
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
    
def posturl(request):
    posts = [1,2,3,4,5,'tim','tom','john']
    return render(request, 'posturl.html', {'posts': posts})

def post(request, pk):
    return render(request,'post.html',{'pk': pk})
    
    
    
def counter(request):
    text = request.POST['text']
    result = len(text.split())
    return render(request, 'counter.html', {'results' : result})

