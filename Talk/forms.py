__author__ = 'jaehongs'
from django import newforms as forms

class RegistrationFrom(forms.Form):
    username = forms.CharField(label='사용자 이름', max_length=30)
    email = forms.EmailFIeld(label='이메일')
    password1 = forms.CharField(
        label='비밀번호',
        widgget=forms.PasswordInput()
    )
    password1 = forms.CharField(
        label='비밀번호확인용',
        widgget=forms.PasswordInput()
    )

