from django.urls import path
from . import views

app_name = 'data_tracking'

urlpatterns = [
    path('',views.HomeView.as_view(), name = 'home_page'),
    path('account_list/',views.MoneyAccountsListView.as_view(), name = 'acc_list'),
    path('account_list/<int:pk>/',views.MoneyAccountsDetailView.as_view(), name = 'acc_detail'),
    path('bill_list/', views.BillListView.as_view(), name = 'bill_list'),
    path('bill_list/<int:pk>/', views.BillDetailView.as_view(), name = 'bill_detail'),
    path('create_account/', views.MoneyAccountCreateView.as_view(), name = 'create_acc'),
    path('create_bill/',views.BillCreateView.as_view(), name = 'create_bill'),
    path('delete_account/', views.MoneyAccountDeleteView.as_view(), name = 'delete_acc'),
    path('delete_bill/',views.BillDeleteView.as_view(), name = 'delete_bill'),
    path('thanks/',views.ThanksPage.as_view(), name = 'thanks'),
    path('pie-chart/',views.pie_chart, name='pie_chart'),
    path('monthly-bills', views.MonthlyBillListView.as_view(),name='monthly_bills'),
    
    

]
