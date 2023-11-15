from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.urls import reverse
from django.db.models import Q
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import datetime
import json

from .models import User, Excerpt, Reward, TopBook


def index(request):
 
    page = 1
    prepage = 0
    nextpage = 2
    first = 0
    last = 20
    excerpts = Excerpt.objects.all().order_by('-id')[first:last]
    fictions = Excerpt.objects.filter(genre="Fiction").all().order_by('-id')[first:last]
    philos = Excerpt.objects.filter(genre="Philosophy").all().order_by('-id')[first:last]
    poems = Excerpt.objects.filter(genre="Poetry").all().order_by('-id')[first:last]
    rewards = Reward.objects.filter(reward_book="").all()
    unsent = Reward.objects.filter(reward_sent=False).exclude(reward_book="").all().count()
    nbre_excerpts = Excerpt.objects.all().count()
    total_pages = (nbre_excerpts // 20 ) + 1
    if total_pages > 10 :
        pages = 10
    else:
        pages = total_pages
    
    noprevious = True
    nonext = False
    if nextpage > total_pages :
        nonext = True

  
    return render(request, "excerpts/index.html", {
        "excerpts": excerpts,
        "fictions": fictions,
        "philos": philos,
        "poems": poems,
        "rewards": rewards,
        "unsent": unsent,
        "pages": range(1,pages+1),
        "currentPage": page,
        "prepage": prepage,
        "nextpage" : nextpage,
        "nonext": nonext,
        "noprevious": noprevious,
       
                    
    })


def oldpages(request, this_page):
 
    page = this_page
    prepage = page - 1
    nextpage = page + 1
    first = (int(page) - 1) * 20
    last = int(page) * 20
    excerpts = Excerpt.objects.all().order_by('-id')[first:last]
    fictions = Excerpt.objects.filter(genre="Fiction").all().order_by('-id')[first:last]
    philos = Excerpt.objects.filter(genre="Philosophy").all().order_by('-id')[first:last]
    poems = Excerpt.objects.filter(genre="Poetry").all().order_by('-id')[first:last]
    rewards = Reward.objects.filter(reward_book="").all()
    unsent = Reward.objects.filter(reward_sent=False).exclude(reward_book="").all().count()
    nbre_excerpts = Excerpt.objects.all().count()
    total_pages = (nbre_excerpts // 20 ) + 1
    if total_pages > 10 :
        pages = 10
    else:
        pages = total_pages

    nonext = False
    noprevious = False
    
    if prepage == 0:
        noprevious = True
    if nextpage > total_pages :
        nonext = True
  
    return render(request, "excerpts/index.html", {
        "excerpts": excerpts,
        "fictions": fictions,
        "philos": philos,
        "poems": poems,
        "rewards": rewards,
        "unsent": unsent,
        "pages": range(1,pages+1),
        "currentPage": page,
        "prepage": prepage,
        "nextpage": nextpage,
        "nonext": nonext,
        "noprevious": noprevious,
                         
    })

def bylikes(request):

    page = 1
    prepage = 0
    nextpage = 2
    rewards = Reward.objects.filter(reward_book="").all()
    unsent = Reward.objects.filter(reward_sent=False).exclude(reward_book="").all().count()
    noprevious = True
    nonext = True

    excerpts = Excerpt.objects.filter(likes__isnull=False).annotate(count=Count('likes')).order_by('-count')[:22]
    fictions = Excerpt.objects.filter(likes__isnull=False,genre="Fiction").annotate(count=Count('likes')).order_by('-count')[:22]
    philos = Excerpt.objects.filter(likes__isnull=False,genre="Philosophy").annotate(count=Count('likes')).order_by('-count')[:22]
    poems = Excerpt.objects.filter(likes__isnull=False,genre="Poetry").annotate(count=Count('likes')).order_by('-count')[:22]
   
    return render(request, "excerpts/index.html", {
        "excerpts": excerpts,
        "fictions": fictions,
        "philos": philos,
        "poems":poems,
        "rewards": rewards,
        "unsent": unsent,
        "pages": range(1,page+1),
        "currentPage": page,
        "prepage": prepage,
        "nextpage" : nextpage,
        "nonext": nonext,
        "noprevious": noprevious,
               
    })

def search(request, word):
    results = Excerpt.objects.filter(Q(author__icontains=word)|Q(book__icontains=word))
    
    if request.method == "GET":
        return JsonResponse([result.serialize() for result in results], safe=False)

    

def find(request):

    page = 1
    prepage = 0
    nextpage = 2
    rewards = Reward.objects.filter(reward_book="").all()
    unsent = Reward.objects.filter(reward_sent=False).all().count()
    noprevious = True
    nonext = True
      
       
    if request.method == "POST":

        word = request.POST["search"]
        results = Excerpt.objects.filter(Q(author__icontains=word)|Q(book__icontains=word)|Q(excerpt_text__icontains=word))
        excerpts = results.all().order_by('?')[:23]
        fictions = results.filter(genre="Fiction").all().order_by('?')[:23]
        philos = results.filter(genre="Philosophy").all().order_by('?')[:23]
        poems = results.filter(genre="Poetry").all().order_by('?')[:23]
        return render(request, "excerpts/index.html", {
            "excerpts": excerpts,
            "fictions": fictions,
            "philos": philos,
            "poems":poems,
            "rewards": rewards,
            "unsent": unsent,
            "pages": range(1,page+1),
            "currentPage": page,
            "prepage": prepage,
            "nextpage" : nextpage,
            "nonext": nonext,
            "noprevious": noprevious,
        })






@login_required 
def new_excerpt(request):
    thisuser = request.user
    if request.method == "POST":
        thisexcerpt = request.POST["excerpt"]
        author = request.POST["author"]
        book = request.POST["book"]
        genre = request.POST["genre"]
        x = datetime.datetime.now()
        now = f"{x.strftime('%b %d, %Y, %H:%M')}"
        Excerpt.objects.create(user_excerpt=thisuser,excerpt_text=thisexcerpt,author=author,genre=genre,book=book,excerpt_date=now)
        total_excerpts = Excerpt.objects.all().count()
        last_rewarded = Reward.objects.order_by('-id')[0].user_reward
        if total_excerpts % 10 == 0 and thisuser != last_rewarded:
            Reward.objects.create(user_reward=thisuser,reward_date=now)
        return HttpResponseRedirect(reverse("index")) 
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required
def maxday(request):
  
    thisuser = request.user
    x = datetime.datetime.now()
    today = f"{x.strftime('%b %d, %Y')}"
    created = Excerpt.objects.filter(user_excerpt=thisuser,excerpt_date__icontains=today).count()
    
    if request.method == "GET":
        return JsonResponse(created, safe=False)

@login_required
@csrf_exempt
def delete(request, excerpt_id):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    thisexcerpt = Excerpt.objects.get(pk=excerpt_id)
    thisexcerpt.delete()
      
    return HttpResponse(status=204)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "excerpts/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "excerpts/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "excerpts/register.html", {
                
                "message_pw": "Passwords must match.",
                "message_name": "",
                "username": username,
                "email": email,
                "password": password,
                "confirmation": confirmation,
                "class_conf": "form-control is-invalid",
                "class_name": "form-control"
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "excerpts/register.html", {
                
                "message_name": "Username already taken.",
                "message_pw": "",
                "username": username,
                "email": email,
                "password": password,
                "confirmation": confirmation,
                "class_conf": "form-control",
                "class_name": "form-control is-invalid"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "excerpts/register.html", {
                
                "message_name": "",
                "message_pw": "",
                "username": "",
                "email": "",
                "password": "",
                "confirmation": "",
                "class_conf": "form-control",
                "class_name": "form-control"
            })


@csrf_exempt
@login_required
def edit(request, excerpt_id):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    thisexcerpt = Excerpt.objects.get(pk=excerpt_id)
    data = json.loads(request.body)
    thistext = data["text"]
    thisauthor = data["author"]
    thisbook = data["book"]
    thisgenre = data["genre"]
    thisexcerpt.excerpt_text = thistext
    thisexcerpt.author = thisauthor
    thisexcerpt.book = thisbook
    thisexcerpt.genre = thisgenre
    thisexcerpt.save()
      
    return HttpResponse(status=204)



@login_required
def likes(request, excerpt_id):
    thisexcerpt = Excerpt.objects.get(pk=excerpt_id)
    thisuser = request.user
    topbooks = TopBook.objects.all()
    if thisuser in thisexcerpt.likes.all():
        thisexcerpt.likes.remove(thisuser)
    else:
        thisexcerpt.likes.add(thisuser)

    topexcerpts = Excerpt.objects.filter(likes=thisuser).all()
    topexcerpt1 = topexcerpts.values('book').annotate(count=Count('id')).order_by('-count')[0]
    topbook1 = topexcerpt1['book']
    topauthor1 = Excerpt.objects.filter(book=topbook1).all()[0].author
    
    try:
        thisbook = TopBook.objects.get(title_topbook=topbook1)
        if thisbook:
            if thisuser not in thisbook.user_topbook.all():
                thisbook.user_topbook.add(thisuser)

    except ObjectDoesNotExist:
        TopBook.objects.create(title_topbook=topbook1,author_topbook=topauthor1)
        TopBook.objects.get(title_topbook=topbook1).user_topbook.add(thisuser)
        
    if request.method == "GET":
        return JsonResponse(thisexcerpt.serialize())
    
def booklist(request):
    thisuser = request.user
    books = TopBook.objects.filter(user_topbook=thisuser)
    
    if request.method == "GET":
        return JsonResponse([book.serialize() for book in books], safe=False)   


@csrf_exempt
@login_required 
def complete_reward(request, reward_id):
    thisuser = request.user
   
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    thisreward = Reward.objects.get(pk=reward_id)
    data = json.loads(request.body)
    thisaddress = data["address"]
    thisbookid = data["book"]
    thisbook = TopBook.objects.get(pk=thisbookid)
    thisreward.reward_book = thisbook.title_topbook
    thisreward.reward_author = thisbook.author_topbook
    thisuser.address = thisaddress
    
    thisreward.save()
    thisuser.save()
      
    return HttpResponse(status=204)

def rewardlist(request):
    
    rewards = Reward.objects.filter(reward_sent=False)
    
    if request.method == "GET":
        return JsonResponse([reward.serialize() for reward in rewards], safe=False)     


@csrf_exempt
@login_required 
def reward(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    
    data = json.loads(request.body)
    reward_id = int(data["rewardid"])
    thisreward = Reward.objects.get(pk=reward_id)
       
   
      
    return JsonResponse(thisreward.serialize())  
    
@csrf_exempt
@login_required
def sending(request):

    if request.method == "POST":
        reward_id = request.POST["pickedreward"]
        checksent = request.POST["sent"]
        tracking = request.POST["shiptrack"]
        thisreward = Reward.objects.get(pk=reward_id)
        if checksent == "yes":
            sent = True
            thisreward.reward_sent = sent
       
        thisreward.ship_track = tracking
        thisreward.save()
      
    return HttpResponseRedirect(reverse("index"))    
    

