from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


########################################################################################
#class based
class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        ser_article = ArticleSerializer(article, many=True)
        return Response(ser_article.data)

    def post(self, request):
        ser_article = ArticleSerializer(data=request.data)

        if ser_article.is_valid():
            ser_article.save()
            return Response(ser_article.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):
    def get_object(self, pk):
        try:
            article = Article.objects.get(pk = pk)
            return article
        except article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):# idk why must using request
        article = self.get_object(pk)
        ser_article = ArticleSerializer(article)
        return Response(ser_article.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        ser_article = ArticleSerializer(article, data=request.data)

        if ser_article.is_valid():
            ser_article.save()
            return Response(ser_article.data, status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response('delete success', status=status.HTTP_200_OK )


########################################################################################
#function based with decorator
@api_view(['GET','POST'])
def article_list_version_api_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        ser_articles = ArticleSerializer(articles, many=True)
        return Response(ser_articles.data)

    elif request.method == 'POST':
        ser_article = ArticleSerializer(data=request.data)
        if ser_article.is_valid():
            ser_article.save()
            return Response(ser_article.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET', 'DELETE'])
def article_detail_version_api_view(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser_article = ArticleSerializer(article)
        return Response(ser_article.data)

    elif request.method == 'PUT':
        ser_article = ArticleSerializer(article, data = request.data)
        if ser_article.is_valid():
            ser_article.save()
            return Response(ser_article.data, status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################################################################
#function based
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        ser_articles = ArticleSerializer(articles, many=True)

        return JsonResponse(ser_articles.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        ser_article = ArticleSerializer(article)
        return JsonResponse(ser_article.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)


