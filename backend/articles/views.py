import requests
import re
import json
import re
import time
from bs4 import BeautifulSoup
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def get_news(n_url):
    news_detail = []
    breq = requests.get(n_url)
    bsoup = BeautifulSoup(breq.content, 'html.parser')

    # html 파싱
    title = bsoup.select('h3#articleTitle')[0].text
    news_detail.append(title)

    # 날짜 파싱
    pdate = bsoup.select('.t11')[0].get_text()[:11]
    news_detail.append(pdate)

    # 기사 본문 크롤링 
    _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ")
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    news_detail.append(btext.strip())

    # 신문사 크롤링
    pcompany = bsoup.select('#footer address')[0].a.get_text()
    news_detail.append(pcompany)

    return news_detail

class news(APIView):
    def get(self, request, format=None):
        query = "삼성전자"   # url 인코딩 에러는 encoding parse.quote(query)
        s_date = "2018.08.20"
        e_date = "2010.08.20"
        s_from = s_date.replace(".","")
        e_to = e_date.replace(".","")
        page = 1
        data = {"data":[]}
        while page < 40:
            url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            }
            req = requests.get(url,headers=header)
            cont = req.content
            soup = BeautifulSoup(cont, 'html.parser')    
            for urls in soup.select("._sp_each_url"):
                try :
                    news = {}
                    if urls["href"].startswith("https://news.naver.com"):
                        news_detail = get_news(urls["href"])
                        p_date = news_detail[1]
                        news["title"] = news_detail[0]
                        news["date"] = news_detail[1]
                        news["link"] = urls["href"]
                        news["description"] = news_detail[2]
                        news["company"] = news_detail[3]
                        data["data"].append(news)
                except Exception as e:
                    continue
            page += 10
        return Response(json.dumps(data, ensure_ascii=False), status=status.HTTP_200_OK)
