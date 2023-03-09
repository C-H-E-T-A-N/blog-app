from django.shortcuts import render,HttpResponse
from blog.models import BlogObj,Contact
import math
# Create your views here.
def home(request):
   return render(request, 'home.html')




def blog(request):

    #below are number of blogs to be displayed on a page
    no_of_posts = 3

    
    #here we will get the page number from the url of the blog page
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)    
    print(page)
    #below we are fetching all the blogs from the blogobj class we made in models
    blogs = BlogObj.objects.all()

    #now we will get the length of blogs i.e no of objects present in the blogs
    length =  len(blogs)
    print(length)

    #logic for pagination
    blogs = blogs[(page-1)*no_of_posts:page*no_of_posts]

    #setting logic for previous and next button
    if page > 1:
        prev = page - 1
    else:
        prev = None    

    if page<(math.ceil(length/no_of_posts)):
        nxt = page + 1
    else:
        nxt = None    
    print(prev,nxt)    
    context = {'blogs':blogs, 'prev':prev, 'nxt':nxt}
    return render(request, 'blog.html', context)
    




def blogpost(request, slug):
    blog = BlogObj.objects.filter(slug = slug).first()
    context = {'blog':blog}
    return render(request, 'blogpost.html', context)




def contact(request):
    if request.method=="POST":
        name =  request.POST['name']
        email =  request.POST['email']
        phone =  request.POST['phone']
        desc =  request.POST['desc']
        object = Contact(name=name, email=email, desc=desc, phone=phone)
        object.save()
    return render(request, 'contact.html')




def search(request):
    return render(request, 'search.html')