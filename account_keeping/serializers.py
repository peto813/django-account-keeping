# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ['user','name', 'account_number','routing_number','currency', 'initial_amount', 'total_amount', 'active']
		model  = Account


