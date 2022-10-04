"""
Users App - Adapters
"""
from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    """Adapter for saving a custom user"""
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        if commit:
            user.save()
        return user