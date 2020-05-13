from django import template
from bbs import models
from django.db.models import Count

register = template.Library()


@register.inclusion_tag("left_menu.html")
def get_left_menu(username):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    # 查询文章分类及对应的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 查文章标签及对应的文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")

    # 按日期归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")

    return {
        "username": username,
        "category_list" :category_list,
        "tag_list": tag_list,
        "archive_list": archive_list
    }
