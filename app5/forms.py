from django import forms


class UserInfoForm(forms.Form):
    '''用户状态'''
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'))
    username = forms.CharField(label='用户名', min_length=6,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True))
    age = forms.IntegerField(label='年龄', initial=1)
    mobile = forms.CharField(label="手机号码")
    status = forms.ChoiceField(label="用户状态", choices=STATUS)
    createdate = forms.DateTimeField(label='创建时间', required=False)