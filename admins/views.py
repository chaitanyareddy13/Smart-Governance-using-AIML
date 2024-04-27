from django.shortcuts import render, redirect
from users.models import sentiments
# Create your views here.
def alogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username=="chaitanya" and password =="1234"):
            return redirect('adminhome')
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html')

def postview(request):
    objs = sentiments.objects.all()
    return render(request,'adminviewpost.html',{'sentiments': objs})

def update_status(request, sentiment_id):
    sentiment = sentiments.objects.get(pk=sentiment_id)
    sentiment.status = "Reviewed"
    sentiment.save()
    return redirect('postview')