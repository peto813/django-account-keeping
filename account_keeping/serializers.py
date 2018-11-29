# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Account
from condo_manager.serializers import BaseUserSerializer

class AccountSerializer(serializers.ModelSerializer):
	user = BaseUserSerializer(read_only=True)
	class Meta:
		fields = ['user','name', 'account_number','routing_number','currency', 'initial_amount', 'total_amount', 'active']
		model  = Account


