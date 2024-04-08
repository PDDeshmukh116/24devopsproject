from django.shortcuts import redirect, render
from .models import Expense,ExpenseForm
from account.views import get_balance
#User can add the expense amount and details
def addexpense(request):
    if request.method=='POST':
        expense=request.POST.get("expense")
        if get_balance(request)>int(expense):
            f=ExpenseForm(request.POST)
            f.save()
            return redirect("/")
        else:
            f=ExpenseForm
            context={'form':f,'exp_msg':"Your Expense Amount Less Balance "}
            return render(request,"addexpense.html",context)
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,"addexpense.html",context)
#expense list 
def expense_list(request):
    uid=request.session.get("uid")
    explist=Expense.objects.filter(user=uid)
    expt=set()
    for i in explist:
        expt.add(i.expense_type)
    context={'expl':explist,'expt':expt}
    return render(request,"expenselist.html",context)
#Delete the expense entries
def delete_expense(request,id):
    inc=Expense.objects.get(id=id)git
    inc.delete()
    return redirect("/")
#expense entries can be sorted based on expense type
def sort_byexpense_type(request,ext):
    uid=request.session.get("uid")
    explist=Expense.objects.filter(user=uid)
    expt=set()
    for i in explist:
        expt.add(i.expense_type)
    
    explist=Expense.objects.filter(user=uid,expense_type=ext)
    context={'expl':explist,'expt':expt}
   
    return render(request,"expenselist.html",context)