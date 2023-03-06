from django.shortcuts import render
from django.http import HttpResponse
from django import views
from django import forms


class Registerform(forms.Form):
    num1 = forms.CharField(label='num1', max_length=100)
    num2 = forms.CharField(label='num2', max_length=100)


def form_view(request):
    num1=request.GET.get('num1',"")
    num2=request.GET.get('num2',"")
    form = Registerform()
    result =""
    if request.method=="GET":
        if 'add' in request.GET:
            result=add(num1,num2)
        if 'sub' in request.GET:
            result=sub(num1,num2)
        if 'mul' in request.GET:
            result=mul(num1,num2)
        if 'div' in request.GET:
            result=div(num1,num2)
    return  render(request,'index.html', {"form": form,'result':result})

def add(num1,num2):
    result= int(num1)+int(num2)
    return result 
def sub(num1,num2):
    result= int(num1)-int(num2)
    return result 
def mul(num1,num2):
    result= int(num1)*int(num2)
    return result 
def div(num1,num2):
    result= int(num1)/int(num2)
    return result


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


    
