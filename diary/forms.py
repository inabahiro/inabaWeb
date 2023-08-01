import os

from django import forms

from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    email = forms.EmailField(label='e-mail')
    title = forms.CharField(label='title', max_length=30)
    message = forms.CharField(label='message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'input your name'

        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'input your e-mail address'

        self.fields['title'].widget.attrs['class']='form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'input title'

        self.fields['message'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'input message'

    # メール送信メソッド
    def send_email(self):
        # 入力値の取得
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ{}'.format(title)
        message = '送信者名:{0}/nメールアドレス:{1}/nメッセージ:/n{2}'.format(name, email, message)
        # 送信元、送信先、ccは環境変数から取得
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [os.environ.get('FROM_EMAIL')]
        cc_list = [email]

        # EmailMessageインスタンスの作成
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()
