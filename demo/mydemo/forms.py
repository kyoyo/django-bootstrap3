from django import forms


class IndexForm(forms.Form):
    username = forms.CharField(max_length=20,label='ユーザ名')
    password = forms.CharField(widget=forms.PasswordInput,label='パスワード')