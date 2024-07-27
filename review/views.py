from django.shortcuts import render
from .models import EReview
from .forms import reviewForms,UserRegeistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request,'index.html')

def review_list(request):
    reviews= EReview.objects.all().order_by('-created_at')
    return render(request,'review_list.html',{'reviews':reviews})

@login_required
def review_create(request):
    if request.method == 'POST':
       form=reviewForms(request.POST,request.FILES)
       if form.is_valid():
           review=form.save(commit=False)
           review.user = request.user
           review.save()
           return redirect('review_list')

    else:
       form = reviewForms()
    return render(request,'review_form.html',{'form':form})

@login_required
def review_edit(request,review_id):
    review= get_object_or_404(EReview,pk=review_id, user=request.user)
    if request.method=='POST':
       form=reviewForms(request.POST,request.FILES,instance=review)
       if form.is_valid():
           review=form.save(commit=False)
           review.user = request.user
           review.save()
           return redirect('review_list')
    else:
        form=reviewForms(instance=review)
    return render(request,'review_form.html',{'form':form})

@login_required
def review_delete(request,review_id):
    review=get_object_or_404(EReview,pk=review_id,user=request.user)
    if request.method=='POST':
        review.delete()
        return redirect('review_list')
    return render(request,'review_confirm_delete.html',{'review':review})


def register(request):
    if request.method=='POST':
        form = UserRegeistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('review_list')
    else:
        form=UserRegeistrationForm()
    return render(request,'registration/register.html',{'form':form})


def search(request):
    
    if request.method=="POST":
        searched=request.POST['searched']
        reviews= EReview.objects.filter(movies_series_name__icontains=searched)
        
        return render(request,'search.html',{'searched':searched,'reviews':reviews})
    else:
        return render(request,'search.html',{})