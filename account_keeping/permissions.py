from rest_framework import permissions


class IsBankAccountOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, bank_account):
		return bank_account.condo == request.user.condo