from django.urls import path

from . import views

# diaryアプリケーションのルーティングにつける名前
app_name = 'diary'

urlpatterns = [
    # 引数1 : http://<ホスト名>/〜の場合のルーティング
    # 引数2 : 処理を渡すviewを指定
    # 引数3 : ルーティング名
    path('', views.IndexView.as_view(), name="index"),
]