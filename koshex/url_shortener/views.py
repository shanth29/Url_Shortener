from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Urls
from random import randint
from django.contrib import messages
from . functions import create_short_url, fetch_long_url, get_similar_data, calculate_time
from django.db.models import F
import webbrowser


# Create your views here.
def index(request):
    return HttpResponse('<h1> WelCome To"URL SHORTENER" Hub !!!</h1>')


@api_view(['POST'])
def convertToShort(request):
    if request.method == 'POST':
        try:
            long_url = request.data.get('long_url')
            if long_url:
                get_short_url = create_short_url(long_url)
                if get_short_url:
                    short_url = Urls.objects.get(long_url = long_url)
                    short_url = 'http://0.0.0.0:8000/' + str(short_url.short_url)
                    return Response({'short_url_exist':short_url},status=status.HTTP_201_CREATED)
                else:
                    short_url = Urls.objects.get(long_url = long_url)
                    short_url = 'http://0.0.0.0:8000/' + str(short_url.short_url)
                    return Response({'short_url_created':short_url},status=status.HTTP_201_CREATED)
            else:
                return Response({'alert':'Please provide long url'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'alert':e}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'alert':'Error in Request'},status=status.HTTP_400_BAD_REQUEST)

          
@api_view(['POST'])
def get_long_url(request):
    if request.method == 'POST':
        try:
            short_url = request.data.get('short_url')
            if short_url:
                short_url = fetch_long_url(short_url)
                if short_url:
                    long_url = Urls.objects.get(short_url = short_url)
                    long_url = long_url.long_url
                    webbrowser.open_new_tab(long_url)
                    Urls.objects.filter(long_url=long_url, short_url=short_url).update(total_hits = F('total_hits')+1)
                    total_hits = Urls.objects.get(long_url = long_url)
                    total_hits = total_hits.total_hits
                    get_total_hour = calculate_time(short_url)
                    if int(get_total_hour) > 0:
                        hourly_hit = total_hits//int(get_total_hour)
                    else:
                        hourly_hit = total_hits
                    return Response({'message':'Url executed !!!','total_hits':total_hits, 'hourly_hits':hourly_hit},status=status.HTTP_201_CREATED)
                else:
                    return Response({'alert':'Url not presents'},status=status.HTTP_201_CREATED)
            else:
                return Response({'alert':'Please provide short url'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'alert':e}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'alert':'Error in Request'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_match_data(request):
    if request.method == 'POST':
        try:
            match_value = request.data.get('item')
            if match_value:
                match_list = get_similar_data(match_value)
                if len(match_list) > 0:
                    return Response({'match_items':match_list},status=status.HTTP_201_CREATED)
                else:
                    return Response({'message':'match not found'},status=status.HTTP_201_CREATED)
            else:
                return Response({'alert':'Please provide item'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'alert':e},status=status.HTTP_400_BAD_REQUEST)
    return Response({'alert':'Error in Request'},status=status.HTTP_400_BAD_REQUEST)
