from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import views
from blog.form import RegisterForms,BlogForm
from blog.models import Blog
from django.conf import settings 



def create_blog(request): 
    form_blog = BlogForm()
    if request.method == 'POST':
        form_blog = BlogForm(request.POST)
        if form_blog.is_valid():
            blog = form_blog.save()
            blog.is_published = True
            blog.save()
    return render(request,'create.html', {'form': form_blog})
    

def list_all_blogs(request):
    blog = Blog.objects.all()
    return render(request,'list_all.html', {'blog': blog})



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
    
