
from django.shortcuts import redirect, render
from .models import Income,IncomeForm
from django.contrib.auth.models import User
#user can add income entries
def addincome(request):
    uid=request.session.get("uid")
    if request.method=='POST':
        income=request.POST.get("income")
        income_type=request.POST.get("income_type")
        income_date=request.POST.get("income_date")
        description=request.POST.get("description")

        inc=Income()
        inc.income=income
        inc.income_type=income_type
        inc.income_date=income_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect("/")
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,"addincome.html",context)
#added income entries would be visible on income list page
def income_list(request):
    uid=request.session.get("uid")
    inclist=Income.objects.filter(user=uid)
    context={'incl':inclist}
    return render(request,"incomelist.html",context)
#income entries can be deleted
def delete_income(request,id):
    inc=Income.objects.get(id=id)
    inc.delete()
    return redirect("/")
#income entries can be search based on income type
def income_search(request):
    uid=request.session.get("uid")
    srch=request.POST.get("srch")
    incl=Income.objects.filter(user=uid,description__contains=srch)
    context={'incl':incl}
    return render(request,"incomelist.html",context)
#user can edit added income entries
def editIncome(request,id):
    uid = request.session.get("uid")
    instance = Income.objects.get(id=id)

    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=instance)
        if form.is_valid():
            income_obj = form.save(commit=False)
            income_obj.user = User.objects.get(id=uid)
            income_obj.save()
            return redirect("/")
    else:
        print(instance)
        form = IncomeForm(instance=instance)

    context = {'form': form}
    return render(request, "editincome.html", context)