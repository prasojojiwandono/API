from django.urls import path
from .views import article_list, article_detail, \
    article_list_version_api_view, article_detail_version_api_view, ArticleDetailView,\
    ArticleView

urlpatterns = [
    ###function based
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),

    ## function based with api_view decorators
    path('article_api_view/', article_list_version_api_view),
    path('detail_api_view/<int:pk>/', article_detail_version_api_view),

    ##class based
    path('article_class/',ArticleView.as_view()),
    path('article_detail_class/<int:pk>/', ArticleDetailView.as_view()),
]