from . import views
from django.urls import path

urlpatterns = [

    ##################  login-register ####################
    path('login', views.loginUsers, name='login'),
    path('registerUser', views.registerUser, name='register'),

    ################### debt-yani-qarz #####################
    path('debtTable', views.debtTable, name='debtTable'),
    path('debtBookCreate', views.debtBookCreate, name='debtBookCreate'),
    path('updateDebt/<str:pk>', views.ubdateDebt, name='ubdateDebt'),
    path('deleteDebt/<str:pk>', views.deleteDebt, name='deleteDebt'),
    
    ################### log out #############################
    path('logoutUser', views.logoutUser, name='logoutUser'),

    #################### user-profile #######################
    path('userprofile', views.UserProfili, name='userprofile'),
    path('user-create', views.userprofilCreate, name='userprofile_create'),
    path('ubdate_profil_user/<str:pk>', views.ubdate_profil_user , name='ubdate_profil_user'),
    path('delete_user_profile/<str:pk>', views.deleteprofile, name='delete_profile'),
    path('user_profile_modelnizatsiya', views.user_profile_modelnizatsiya , name='user_profile_modelnizatsiya'),

    ####################  Abarot  ###########################
    path('abarot_table', views.abarot_table, name='abarot_table'),
    path('createabarot', views.abarotCreate, name='abarot'),
    path('deleteabarot/<str:pk>', views.deleteabarot, name='daleteabarots'),
    path('updateabarot/<str:pk>', views.updateabarot, name='ubdateabarots'),
    
    # product quantity
        
    #######################  Zakaz #################################
    path('buyurtma_table', views.buyurtma_table, name='buyurtma_table'),
    path('buyurtmaCreate', views.buyurtmaCreate, name='buyurtmaCreates'),
    path('deletezakas/<str:pk>', views.deletezakaz, name='zakas-delete'),
    path('updatezakas/<str:pk>', views.updatezakas, name='zakas-update'),  
    
    #########################  messages ###############################
    path('messages-table', views.messages_table, name='messages-chet'),
    path('deletemessages/<str:pk>', views.deletemessages, name='messages-delete'),
    # path('updatemessages/<str:pk>', views.updatemessages, name='messages-update'), 
]
