"""URLs for the account_keeping app."""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.urls import path, re_path

from . import views

router = DefaultRouter()
router.register(r'bank_accounts', views.BankAccountsViewSet, basename='bank_accounts')

urlpatterns = [
    path('', include(router.urls))
    # url(r'transaction/(?P<pk>\d+)/$',
    #     views.TransactionUpdateView.as_view(),
    #     name='account_keeping_transaction_update'),

    # url(r'transaction/create/$',
    #     views.TransactionCreateView.as_view(),
    #     name='account_keeping_transaction_create'),

    # url(r'invoice/(?P<pk>\d+)/$',
    #     views.InvoiceUpdateView.as_view(),
    #     name='account_keeping_invoice_update'),

    # url(r'invoice/create/$',
    #     views.InvoiceCreateView.as_view(),
    #     name='account_keeping_invoice_create'),

    # url(r'accounts/$',
    #     views.AccountListView.as_view(),
    #     name='account_keeping_accounts'),

    # url(r'payees/(?P<pk>\d+)/$',
    #     views.PayeeUpdateView.as_view(),
    #     name='account_keeping_payee_update'),

    # url(r'payees/create/$',
    #     views.PayeeCreateView.as_view(),
    #     name='account_keeping_payee_create'),

    # url(r'payees/$',
    #     views.PayeeListView.as_view(),
    #     name='account_keeping_payees'),

    # url(r'export/$',
    #     views.TransactionExportView.as_view(),
    #     name='account_keeping_export'),

    # url(r'all/$',
    #     views.AllTimeView.as_view(),
    #     name='account_keeping_all'),

    # url(r'(?P<year>\d+)/(?P<month>\d+)/$',
    #     views.MonthView.as_view(),
    #     name='account_keeping_month'),

    # url(r'(?P<year>\d+)/$',
    #     views.YearOverviewView.as_view(),
    #     name='account_keeping_year'),

    # url(r'current-year/$',
    #     views.CurrentYearRedirectView.as_view(),
    #     name='account_keeping_current_year'),

    # url(r'current-month/$',
    #     views.CurrentMonthRedirectView.as_view(),
    #     name='account_keeping_current_month'),

    # url(r'$',
    #     views.IndexView.as_view(),
    #     name='account_keeping_index'),
]
