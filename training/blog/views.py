from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import views
from django.contrib.auth.models import User
from blog.form import RegisterForms,BlogForm,Login_form
from blog.models import Blog
from django.conf import settings 
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate,login,logout
    


def home(request):
    return render(request,'blog_index.html')

def registered_user(request):
    form=RegisterForms()
    if request.method=='POST':
        userName = request.POST.get('username', None)
        userPass = request.POST.get('password', None)
        email=request.POST.get('email')
        user = User.objects.create_user(username=userName,password=userPass, email=email)
        user.save()
    return render(request,'register_blog.html', {'form': form})

# @permission_required('blog.add_blog')
def create_blog(request): 
    form_blog = BlogForm()
    if request.method == 'POST':
        form_blog = BlogForm(request.POST)
        if form_blog.is_valid():
            blog = form_blog.save()
            blog.is_published = True
            blog.save()
            return redirect('/demo/list')
    return render(request,'create.html', {'form': form_blog})
    

def list_all_blogs(request):
    blog = Blog.objects.all()
    return render(request,'list_all.html',{'blog':blog})
    

# def get_blogs(request):
#     if request.method  == 'GET':
#             blogs  = Blog.objects.all()
#     return render(request, , {'blogs':blogs})



@permission_required('blog.change_blog')
def update_blog(request,**kwargs):
    form = BlogForm()
    if request.method == 'POST':
        if id:= kwargs.get('id'):
            obj_edit = Blog.objects.get(id=id)
            form = BlogForm(request.POST, instance=obj_edit)
            if form.is_valid():
                form.save()
                return redirect('/demo/list')
    context = {
        'form':form
    }
    return render(request, 'update.html' ,context)


def delete_blog(request,**kwargs):
    if id:=kwargs.get('id'):
        blogs = Blog.objects.get(id=id)
        blogs.delete()
    blog = Blog.objects.all()
    return render(request,'list_all.html', {'blog': blog})


def login_user(request):
    form = Login_form()
    if request.method == "POST":
        print(request.user)
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= name,password=password)
        if user is not None:
            login(request,user)
            print(request.user)
            return redirect('/demo/list')
        else:
            return HttpResponse("please enter valid details for login ")
    return render(request,'blog_login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home page')

@permission_required('UserApi.can_publish', raise_exception=True)
def publish_blog(request, **kwargs):
    if request.method == 'GET':
        if id:= kwargs.get('id'):
                blog = Blog.objects.get(id=id)
                blog.is_published = True
                blog.save()
    return redirect('/demo/list')

def update_user(request,**kwargs):
    print(request.method)
    if request.method == 'POST':
        if id:= kwargs.get('id'):
            print(request.POST)
            password =request.POST.get('password')
            # /main_pass = request.POST.get('confirm_password')
            user = User.objects.get(id=id)
            print(user)
            user.set_password(password)
            user.save()
        else:
            print("Id not found")
            # messages.error(request,'Password did not match')
    return render(request, 'change_pass.html')

def get_published_blog(request):
    blogs = Blog.objects.filter(is_published=True)
    return render(request, 'bloglist.html', {'blogs':blogs})

def get_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'list_blog.html', {'blogs':blogs}) 

    
    





# from django import forms


# class Registerform(forms.Form):
#     num1 = forms.CharField(label='num1', max_length=100)
#     num2 = forms.CharField(label='num2', max_length=100)


# def form_view(request):
#     num1=request.GET.get('num1',"")
#     num2=request.GET.get('num2',"")
#     form = Registerform()
#     result =""
#     if request.method=="GET":
#         if 'add' in request.GET:
#             result=add(num1,num2)
#         if 'sub' in request.GET:
#             result=sub(num1,num2)
#         if 'mul' in request.GET:
#             result=mul(num1,num2)
#         if 'div' in request.GET:
#             result=div(num1,num2)
#     return  render(request,'index.html', {"form": form,'result':result})

# def add(num1,num2):
#     result= int(num1)+int(num2)
#     return result 
# def sub(num1,num2):
#     result= int(num1)-int(num2)
#     return result 
# def mul(num1,num2):
#     result= int(num1)*int(num2)
#     return result 
# def div(num1,num2):
#     result= int(num1)/int(num2)
#     return result


# def hello(request):
#     num1=request.GET.get('num1',"")
#     num2=request.GET.get('num2',"")
#     form=f"""
# #    <form method="GET">
# #    <input type="text" name="num1"  placeholder="Enter num1" value="{num1}"/>
# #    <input type="text" name="num2" placeholder="Enter num2" value="{num2}"/>
# #    <button name="add">+</button>
# #    <button name="sub">-</button>
# #    <button name="mul">*</button>
# #    <button name="div">/</button>
# #     """
#     # result = ""
#     if request.method=="GET":
        
#         if 'add' in request.GET:
#             result=add(num1,num2)
#         if 'sub' in request.GET:
#             result=sub(num1,num2)
#         if 'mul' in request.GET:
#             result=mul(num1,num2)
#         if 'div' in request.GET:
#             result=div(num1,num2)
#     # return HttpResponse(f'<html><body>{form}<h1>RESULT:{result}</h1><body/></html>')
#         return HttpResponse(Registerform )
    
