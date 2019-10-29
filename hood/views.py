from django.shortcuts import render,redirect
from .models import Neighbourhood,Services,Authorities,Post,Profile,Notifications,Comment,Business,Hoods,Joinhood
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
#from .email import send_priority_email
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import TrendingForm,ProfileForm,PostForm,BusinessForm,CommentForm,HoodForm,JoinHoodForm


def home(request):
    try:
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/login')
            current_user = request.user
            profile = Profile.objects.get(username=current_user)

    except ObjectDoesNotExist:
            return redirect('create-profile')


    return render(request, 'all-pages/index.html')

def create_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request, 'all-pages/profile.html',{'form':form})

def trending(request):
    current_user= request.user
    profile = Profile.objects.get(username=current_user)
    if request.method == 'POST':
        form = TrendingForm(request.POST, request.FILES)
        if form.is_valid():
            trends = form.save(commit=False)
            trends.username = current_user
            trends.save()
            return HttpResponseRedirect('/')

    else:
        form = TrendingForm()

    return render(request, 'all-pages/trends.html', {'form':form})


def alert(request):
    current_user= request.user
    profile = Profile.objects.get(username=current_user)
    trends = Notifications.objects.filter()

    return render(request, 'all-pages/trends.html',{'trends':trends})

def update_profile(request):
    current_user=request.user
    instance = Profile.objects.get(username=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()

            return redirect('home')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)

    else:
        form = ProfileForm()

    return render(request, 'all-pages/update-profile.html', {'form':form})                    

# def create_post(request):
#     current_user = request.user
#     profile = Profile.objects.get(username=current_user)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.username = current_user
#             post.avatar = profile.avatar
#             post.hood = profile.hood
#             post.save()
#             return redirect('posted')
#             #return HttpResponseRedirect('posted')

#     else:
#         form = PostForm()

#     return render(request, 'all-pages/post.html', {'form':form})  

# def biz(request):
#     current_user = request.user
#     profile = Profile.objects.get(username=current_user)

#     if request.method == 'POST':
#         form = BusinessForm(request.POST, request.FILES)
#         if form.is_valid():
#             business = form.save(commit=False)
#             business.owner = current_user
#             business.hood = Profile.hood
#             business.save()
#             return HttpResponseRedirect('business')

#     else:
#         form = BusinessForm()

#     return render(request, 'all-pages/biz.html',{'form':form})   

# # def view_post(request, post):
# #     current_user = request.user

#     # try:
#     #     comments = Comment.objects.filter(post_id=id)

#     # except:
#     #     comments = []  
#     # post = get_object_or_404(Post, post=id)
#     # # post = Post.objects.get(id=id)

#     # if request.method == 'POST':
#     #     form = CommentForm(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         comments = form.save(commit=False)
#     #         comments.username = current_user
#     #         comments.post = post
#     #         comments.save()

#     # else:
#     #     form = CommentForm()

#     #     context = {
#     #         'posts':Post.objects.all()
#     #     }

#     # return render(request, 'all-pages/viewpost.html',{'form':form ,'comments':comments, 'post':post}, context)                       

# @login_required(login_url='/accounts/login/')
# def authorities(request):
#     current_user=request.user
#     profile=Profile.objects.get(username=current_user)
#     authorities = Authorities.objects.filter(hood=profile.hood)

#     return render(request,'authorities.html',{"authorities":authorities})

# @login_required(login_url='/accounts/login/')
# def businesses(request):
#     current_user=request.user
#     profile=Profile.objects.get(username=current_user)
#     businesses = Business.objects.filter(hood=profile.hood)

#     return render(request,'businesses.html',{"businesses":businesses})

# def userprofile(request):
#     context = {
#         'profiles':Profile.objects.all(),
#     }  

#     return render(request, 'all-pages/userprofile.html', context)  

# def posted(request):
#     context = {
#         'posts':Post.objects.all()
#     }    

#     return render(request, 'all-pages/viewpost.html', context)

# def neighbourhoods(request):
#     current_user = request.user
#     profile = Profile.objects.all()
#     if request.method == 'POST':
#         form = HoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hoods = form.save(commit=False)
#             hoods.user = current_user
#            # hoods.name = name
#             hoods.save()
#             return redirect('userprofile')

#     else:
#         form = HoodForm()
#     context = {
       
#         'form':form,
#     } 
#     return render(request, 'all-pages/hood.html',{'form':form}, context)   


# def joinone(request):
#     context = {
#          'hoods':Hoods.objects.all(),
#     }
#     return render(request, 'all-pages/nhood.html', context)

# def joinhood(request):
#     current_user = request.user
#     profile = Profile.objects.all()
#     if request.method == 'POST':
#         form = JoinHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hoodes = form.save(commit=False)
#             hoodes.user = current_user
           
#             hoodes.save()

#             redirect('userprofile')

#     else:
#         form = HoodForm()

#     context = {
#          'joinhoods':Joinhood.objects.all(),
#          'form':form,
#     }
#     return render(request, 'all-pages/join.html', context)
