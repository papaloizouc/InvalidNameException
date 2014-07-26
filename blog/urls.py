from django.conf.urls.defaults import url, patterns


urlpatterns = patterns(
    'blog.views',
    url(r'^admin/article$', 'create_article', {}, name='create_article'),
    url(r'^article/(?P<article_url>[\w-]+)$',
        'show_article', {}, name='show_article'),
)
