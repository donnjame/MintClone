from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import MoneyAccount, Bill
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'data_tracking/data_tracking_base.html'

class ThanksPage(TemplateView):
    template_name = 'data_tracking/thanks.html'


class MoneyAccountsListView(LoginRequiredMixin, ListView):
    model = MoneyAccount
    

class MoneyAccountsDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'money_account_details'
    model = MoneyAccount
    template_name = 'data_tracking/MoneyAccount_detail.html'
    

class MoneyAccountCreateView(CreateView, LoginRequiredMixin):
    model = MoneyAccount
    fields = ('account_type', 'balance')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MoneyAccountCreateView, self).form_valid(form)
    

class MoneyAccountDeleteView(LoginRequiredMixin, DeleteView):
    model = MoneyAccount
    # success_url = reverse_lazy('')
    pass

class BillListView(LoginRequiredMixin, ListView):
    model = Bill
    

class BillDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'bill_details'
    model = Bill
    template_name = 'data_tracking/Bill_detail.html'
    

class BillCreateView(LoginRequiredMixin, CreateView):
    model = Bill
    fields = ('bill_type','bill_name','bill_amount','automatic_payment')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BillCreateView, self).form_valid(form)

class BillDeleteView(LoginRequiredMixin, DeleteView):
    model = Bill
    # success_url = reverse_lazy('')
    pass

class MonthlyBillListView(ListView):
    template_name = 'data_tracking/Monthly_bill_list.html'
    model = Bill
    def get_queryset(self):
        return Bill.monthly_bill_objects.monthly_bills()


def pie_chart(request):
    labels = []
    data = []

    queryset = Bill.objects.all()
    for b in queryset:
        labels.append(b.bill_name)
        data.append(b.bill_amount)
    
    return render(request, 'data_tracking/pie_chart.html',{
        'labels': labels,
        'data': data,
    })


