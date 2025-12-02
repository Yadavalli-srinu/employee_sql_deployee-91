from django.shortcuts import render,redirect
from django.views import View
from app1.models import employee_model
from app1.forms import employee_form
'get'
class employee_details(View):
    def get(self,request):
        data=employee_model.objects.all()
        content={
            "data":data
        }
        return render(request,'home.html',content)

'post'
class employee_empty(View):
    def get(self, request):
        form = employee_form()
        return render(request, 'form.html', {"form": form})

    def post(self, request):
        form = employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home101')
        else:
            
            return render(request, 'form.html', {"form": form})
        
'delete'
class employee_delete(View):
    def get(self, request, id):
        data = employee_model.objects.get(id=id)
        data.delete()
        return redirect('home101')

'update'
class employee_update(View):
    def get(self,request,id):
        data=employee_model.objects.get(id=id)
        form=employee_form(instance=data)
        return render(request,'form.html',{"form":form})
    def post(self,request,id):
        data=employee_model.objects.get(id=id)
        form=employee_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home101')
        else:
            form=employee_form(instance=data)
            return render(request,'form.html',{"form":form})
            
    