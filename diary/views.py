from django.shortcuts import render

from django.views import generic


# テンプレート表示のためのTemplateViewを継承
class IndexView(generic.TemplateView):
    # 表示するhtmlを指定
    template_name = "index.html"
