from stark.service.stark import site, ModelStark
from .models import *


class UserConfig(ModelStark):
    list_display = ['username', 'email', 'phone']


class ArticleConfig(ModelStark):
    list_display = ['title', ]


site.register(UserInfo, UserConfig)
site.register(Blog)
site.register(Category)
site.register(Tag)
site.register(Article, ArticleConfig)
site.register(ArticleDetail)
site.register(Article2Tag)
site.register(ArticleUpDown)
site.register(Comment)