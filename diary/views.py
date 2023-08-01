import logging
import os


from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm
from .models import Diary

logger = logging.getLogger(__name__)


# 初期ページ
class IndexView(generic.TemplateView):
    # 表示するhtmlを指定
    template_name = "index.html"


# 問い合わせページ
class InquiryView(generic.FormView):
    # 表示するhtmlを指定
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    # form_validメソッドのoverride バリデーションに問題なかった場合、実行
    def form_valid(self, form):
        # form.pyのsend_mail()メソッド
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry send by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


# 日記一覧表示ページ
class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


