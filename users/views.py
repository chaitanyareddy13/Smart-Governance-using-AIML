from django.shortcuts import render, redirect
from .models import userregister, sentiments
import joblib
import nltk
# Create your views here.
def index(request):
    return render(request,"index.html")

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = userregister.objects.filter(name=username, password=password)
        if users.exists():
            user = users.first()
            request.session['username'] = username
            return redirect('userhome')
    return render(request,'userlogin.html')

def uregister(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        cnfrmpwd = request.POST.get('confirm_password')
        if password == cnfrmpwd:
            userregister.objects.create(name=username, email=email, password=password)
            return redirect('userlogin')
    return render(request,"register.html")

def userhome(request):
    username = request.session['username']
    print(username)
    return render(request,'userhome.html',{'username':username})

def stem(textmsg):
    stemmer = nltk.stem.PorterStemmer()
    textmsg_stem = ''
    textmsg = textmsg.strip("\n")
    words = textmsg.split(" ")
    words = [stemmer.stem(w) for w in words]
    textmsg_stem = ' '.join(words)
    return textmsg_stem

def newpost(request):
    if request.method == "POST":
        text = request.POST.get('sentiment_text')
        username = request.session.get('username')  # Use .get() to avoid KeyError
        status = "Not Reviewed"
        text_sentiment_model = joblib.load('model/sentimentModel.pkl')
        text_processed = stem(text)
        sentiment = text_sentiment_model.predict([text_processed])  # Pass text_processed as a list
        predicts = 'None'
        if sentiment[0] == 0:
            predicts = "Negative"
        elif sentiment[0] == 1:
            predicts = "Positive"
        sentiments.objects.create(name=username, text=text, sentiment=predicts, status=status)
        return render(request, 'newpost.html',{'submitstatus':'Thank you for submitting response'})
    return render(request, 'newpost.html')

def viewpost(request):
    username = request.session.get('username')
    objs = sentiments.objects.filter(name=username)
    return render(request, 'viewpost.html', {'sentiments': objs})