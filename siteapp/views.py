from django.shortcuts import redirect , render 
from .forms import * 
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


################################### login or register #################################

def loginUsers(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or password was incorrect")
    context = {
    }            
    return render(request, 'siteapp/log_register/login.html')

@login_required(login_url='login') 
def registerUser(request):
    if request.user.is_superuser:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('login')
        context = {
            'form':form
        }    
        return render(request, 'siteapp/log_register/register.html', context)
    else:
        return redirect('dashboard')

################################### End login or register ####################################

@login_required(login_url='login') 
def dashboard(requets):
    products = Abarots.objects.all()
    debtbook = DebdBook.objects.all()
    buyurtma = Zakaz.objects.all()
    user_profili_soni = User_profil_Create.objects.all().count()
    zakas = buyurtma.count()
    mahsulotlarning_umumiy_soni = products.count()
    qarzdorlar_soni = debtbook.count()
    xatlarni_sanash = Habar.objects.all().count()
    income = 0
    for product in products:
        income += product.product_total_price()
    income1 = 0
    for d in debtbook:
        income1 += d.obshi_pul()  
    income2 = 0
    for product in products:
        income2 += product.obshi_mahsulot()   
    income3 = 0
    for b in buyurtma:
        income3 += b.buyurtmasoni()        
    income4 = 0
    for debt in debtbook:
        income4 += debt.tannarx()
    income5 = 0    
    for debts in debtbook:
        income5 += debts.ustki_narx()       
    context = {
        'income':income,
        'income2':income2,
        'income3':income3,
        'income4':income4,
        'income5':income5,
        'income1':income1,
        'zakas':zakas,
        'user_profili_soni':user_profili_soni,
        'mahsulotlarning_umumiy_soni':mahsulotlarning_umumiy_soni,
        'qarzdorlar_soni':qarzdorlar_soni,
        'xatlarni_sanash':xatlarni_sanash,
    }    
    return render(requets, 'siteapp/dashboard.html', context)

########################################## End Dahsboard #####################################
##########################################  Debt #####################################

@login_required(login_url='login')
def debtTable(request):
    if request.method == 'POST':
        search_q = request.POST.get('q')
        Books = DebdBook.objects.filter(full_name__contains=search_q)
    else:    
        Books = DebdBook.objects.all()
    context = {
        'Books':Books
    }
    return render(request, 'siteapp/Debt/debtTable.html', context)

@login_required(login_url='login')
def debtBookCreate(request):
    if request.user.is_superuser or request.user.is_staff: 
        form = Create_Debt()
        if request.method == 'POST':
            form = Create_Debt(request.POST)
            if form.is_valid():
                form.save()
                return redirect('debtTable')
            else:
                form = Create_Debt()
        context = {
            'form':form
        }    
        return render(request, 'siteapp/Debt/createdebt.html', context)
    else:
        return redirect('debtTable')

@login_required(login_url='login')
def ubdateDebt(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        Books = DebdBook.objects.get(id=pk)
        form = Create_Debt(instance=Books)
        if request.method == "POST":
            form = Create_Debt(request.POST, instance=Books)
            if form.is_valid():
                form.save()
                return redirect('debtTable')
        context = {
            'form':form
        }    
        return render(request, 'siteapp/Debt/createdebt.html', context) 
    else:
        return redirect('debtTable')

@login_required(login_url='login')
def deleteDebt(request, pk):
    if request.user.is_superuser:
        Books = DebdBook.objects.get(id=pk)
        if request.method == "POST":
            Books.delete()
            return redirect('debtTable')
        context = {
            'Books':Books
        }    
        return render(request, 'siteapp/Debt/deleteDebt.html', context)
    else:
        return redirect('debtTable')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('loginUser')

#######################################  End Debt ##########################################
#######################################  User objects ##########################################

@login_required(login_url='login')
def UserProfili(request):
    userprofil = User_profil_Create.objects.all()
    context = {
        'username':request.user,
        'userprofil':userprofil,
    }
    return render(request, 'siteapp/userprofi/userprofails.html', context)

@login_required(login_url='login')
def userprofilCreate(request):
    if request.user.is_superuser or request.user.is_staff or request.user.is_active : 
        form = UserprofileCreate()
        if request.method == 'POST':
            form = UserprofileCreate(request.POST)
            if form.is_valid():
                form.save()
                return redirect('userprofile')
            else:
                form = UserprofileCreate()
        context = {
            'form':form,
        }    
        return render(request, 'siteapp/userprofi/usercreate.html', context)
    else:
        return redirect('userprofile')

@login_required(login_url='login')
def ubdate_profil_user(request, pk):
    userprofil = User_profil_Create.objects.get(id=pk)
    form = UserprofileCreate(instance=userprofil)
    if request.method == "POST":
        form = UserprofileCreate(request.POST, instance=userprofil)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    context = {
        'form':form
    }    
    return render(request, 'siteapp/userprofi/usercreate.html', context)

@login_required(login_url='login')
def deleteprofile(request, pk):
    if request.user.is_superuser:
        profile = User_profil_Create.objects.get(id=pk)
        if request.method == "POST":
            profile.delete()
            return redirect('userprofile')
        context = {
            'profile':profile
        }    
        return render(request, 'siteapp/userprofi/deleteuserprofile.html', context)
    else:
        return redirect('userprofile')

@login_required(login_url='login')
def user_profile_modelnizatsiya(request):
    if request.method == 'POST':
        search_q = request.POST.get('q')
        userprofil = DebdBook.objects.filter(full_name__contains=search_q)
    else:
        userprofil = User_profil_Create.objects.all()
    context = {
        'userprofil':userprofil,
    }
    return render(request, 'siteapp/userprofi/userprofil_m.html', context)

#######################################  end user profile  ###########################################
#######################################  Abarot objects  #######################################

@login_required(login_url='login')
def abarot_table(request):
    if request.user.is_superuser or request.user.is_staff:
        products = Abarots.objects.all()
        if request.method == 'POST':
            search_b = request.POST.get('b')
            products = Abarots.objects.filter(product_name__contains=search_b)     
        else:
            products = Abarots.objects.all()       
        income = 0
        for product in products:
            income += product.product_total_price()
        context = {
            'products':products,
            'income':income
        }
        return render(request, 'siteapp/abarot/abarotTable.html', context)
    else:
        return redirect('dashboard')
    
@login_required(login_url='login')
def abarotCreate(request):
    if request.user.is_superuser or request.user.is_staff: 
        form = Create_abarot()
        if request.method == 'POST':
            form = Create_abarot(request.POST)
            if form.is_valid():
                form.save()
                return redirect('abarot_table')
            else:
                form = Create_abarot()
        context = {
            'form':form
        }    
        return render(request, 'siteapp/abarot/createabarot.html', context)
    else:
        return redirect('abarot_table')

@login_required(login_url='login')
def deleteabarot(request, pk):
    if request.user.is_superuser:
        product = Abarots.objects.get(id=pk)
        if request.method == "POST":
            product.delete()
            return redirect('abarot_table')
        context = {
            'product':product
        }    
        return render(request, 'siteapp/abarot/deleteabarot.html', context)
    else:
        return redirect('abarot_table')

@login_required(login_url='login')
def updateabarot(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        products = Abarots.objects.get(id=pk)
        form = Create_abarot(instance=products)
        if request.method == "POST":
            form = Create_abarot(request.POST, instance=products)
            if form.is_valid():
                form.save()
                return redirect('abarot_table')
        context = {
            'form':form
        }    
        return render(request, 'siteapp/abarot/createabarot.html', context) 
    else:
        return redirect('abarot_table')
            


###################################### end Abarot #############################################
#######################################  Zakazlar soni ########################################

@login_required(login_url='login')
def buyurtma_table(request):
    buyurtma = Zakaz.objects.all()
    context = {
        'buyurtma':buyurtma
    } 
    return render(request, 'siteapp/zakas/zakasTable.html', context)

@login_required(login_url='login')
def buyurtmaCreate(request):
    if request.user.is_superuser or request.user.is_staff: 
        form = Create_buyurtmalar()
        if request.method == 'POST':
            form = Create_buyurtmalar(request.POST)
            if form.is_valid():
                form.save()
                return redirect('buyurtma_table')
            else:
                form = Create_buyurtmalar()
        context = {
            'form':form
        }    
        return render(request, 'siteapp/zakas/createzakas.html', context)
    else:
        return redirect('buyurtma_table')

@login_required(login_url='login')
def deletezakaz(request, pk):
    if request.user.is_superuser:
        byurtma = Zakaz.objects.get(id=pk)
        if request.method == "POST":
            byurtma.delete()
            return redirect('buyurtma_table')
        context = {
            'byurtma':byurtma
        }    
        return render(request, 'siteapp/zakas/deletezakas.html', context)
    else:
        return redirect('buyurtma_table')

@login_required(login_url='login')
def updatezakas(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        buyurtma = Zakaz.objects.get(id=pk)
        form = Create_buyurtmalar(instance=buyurtma)
        if request.method == "POST":
            form = Create_buyurtmalar(request.POST, instance=buyurtma)
            if form.is_valid():
                form.save()
                return redirect('buyurtma_table')
        context = {
            'form':form
        }    
        return render(request, 'siteapp/zakas/createzakas.html', context)
    else:
        return redirect('buyurtma_table')

##################################### end zakaz #####################################
################################### massages object  ################################

@login_required(login_url='login') 
def messages_table(request):
    if request.user.is_superuser or request.user.is_staff or request.user.is_active:
        form = Create_messages()
        if request.method == 'POST':
            form = Create_messages(request.POST)
            if form.is_valid():
                form.save()
                return redirect('messages-chet')
        habar_yozish = Habar.objects.all()
        context = {
            'habar_yozish':habar_yozish,
            'form':form,
        }
        return render(request, 'siteapp/messages/messagesTable.html', context)
     
@login_required(login_url='login')
def deletemessages(request, pk):
    if request.user.is_superuser:
        messages = Habar.objects.get(id=pk)
        if request.method == "POST":
            messages.delete()
            return redirect('messages-chet')
        context = {
            'messages':messages
        }    
        return render(request, 'siteapp/messages/deletemessages.html', context)
    else:
        return redirect('buyurtma_table')     
     
################################### end messages ####################################

