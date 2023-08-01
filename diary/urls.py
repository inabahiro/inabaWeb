from django.urls import path

from . import views

# diaryアプリケーションのルーティングにつける名前
app_name = 'diary'

urlpatterns = [
    # 初期ページ
    path('', views.IndexView.as_view(), name="index"),
    # 問い合わせページ
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    # 日記一覧表示
    path('diary-list/', views.DiaryListView.as_view(), name='diary_list'),
    #
]