from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

import pandas as pd 
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import datetime,time
import json
import urllib
import re
import requests
from bs4 import BeautifulSoup
import iex

# Stock Class in iex matches with Stock table in Db
from iex import Stock as Stock_iex

from .models import Stock

from django.views.generic import (

    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)


global current_stock





# def get_data(request,*args,**kwargs):
#     print("\n\n\n\n\n ", request.path(),"\n\n\n\n")
#     data = {"sales":100,"customers":120}
#     return JsonResponse(data)


# API endpoint for Chart and Table Data
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    

    def get_chart_data(self,stock):
        stock_file_name = stock.stock_name + ".csv"       

        strFormat="%Y-%m-%d"
        df = pd.read_csv(os.path.join(os.getcwd(),"stocks_data",stock_file_name))
        date_parser = lambda word : datetime.datetime.fromtimestamp(time.mktime(time.strptime(str(word),strFormat))).strftime("%d-%b-%Y")
        df['Date'] = df['Date'].map(date_parser)

        cols_to_delete = ['Open','High','Low','Adj Close','Volume']
        for col in cols_to_delete:
            del df[col]

        Data = list(df['Close'])
        labels = list(df['Date'])

        return Data,labels


    def get_description(self,stock):
            url = "https://en.wikipedia.org/wiki/"+stock.company_name
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            self.table = soup.find_all("table", class_="infobox vcard")[0]

            #Get Description:
            session = requests.Session()
            URL = "https://en.wikipedia.org/w/api.php"
            SEARCHPAGE = company_name
            PARAMS = {
                'action': "opensearch",
                'list': "search",
                'search': SEARCHPAGE,
                'format': "json"
            }

            response = session.get(url=URL, params=PARAMS)
            DATA = response.json()
            return DATA[2][0:2]
        
    def get_table_data(self,stock):
        url = "https://en.wikipedia.org/wiki/"+stock.company_name
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all("table", class_="infobox vcard")[0]
        return table

  
  
    def get(self, request, format=None):  

        stock = Stock.objects.get(stock_name=current_stock)  

        # Get data from csv to chart them. 
        Data,labels = self.get_chart_data(stock)

        self.table = None
        self.description = None
        
        if stock.is_downloaded == True:
            self.table = stock.table_data
            self.description = stock.description

        else:
            self.table = self.get_table_data(stock)
            self.description = self.get_description(stock)

            #Updating the stock Object 
            stock.is_downloaded = True
            stock.company_name
            stock.table_data =  str(self.table)
            stock.description = self.description
            stock.save()

       

        data = {
        "table_data":str(self.table),
        "labels":labels,
        "Data":Data,
        "Description":self.description,
            }



        return Response(data)
  

class StockListView(ListView):
    template_name = "stocks/stock_list.html"
    queryset = Stock.objects.all()    


class StockDetailView(DetailView):     
    template_name = "stocks/stock_detail.html"        


    def get_object(self):        
        global current_stock
        stock_name = self.kwargs.get('stock_name')
        current_stock = stock_name
        return get_object_or_404(Stock,stock_name = stock_name)


    # def get_context_data(self, **kwargs):
    #     context = {}
    #     stock_name = self.kwargs.get('stock_name')
    #     company_name = Stock.objects.get(stock_name=stock_name).company_name

    #     url = "https://en.wikipedia.org/wiki/"+company_name
    #     page = requests.get(url)
    #     soup = BeautifulSoup(page.text, 'html.parser')
    #     table = soup.find_all("table", class_="infobox vcard")[0]
    #     table = str(table)
    #     return context

    # def get_context_data(self, **kwargs):
    #     global current_stock
    #     url_site = "https://www.google.com/search?q=donald+trump&kponly&kgmid=/m/0cqt90&key=AIzaSyD_6bOqsyts7K1NOUarvvY7CxQ5DzqZI6A&limit=1"
    #     page = requests.get(url_site)
    #     soup = BeautifulSoup(page.text, 'html.parser')

    #     f = open("templates/stocks/" + current_stock +".html","w")
    #     f.write(soup.prettify())
    #     f.close()

        
    # def get_context_data(self, **kwargs):
    #     context = super(StockDetailView, self).get_context_data(**kwargs)
    #     df = pd.read_csv(os.path.join(os.getcwd(),"stocks_data","AAPL.csv"))
    #     temp = df.head()
    #     first = temp.iloc[0:2]
    #     cols_to_delete = ['Open','High','Low','Adj Close','Volume']

    #     for col in cols_to_delete:
    #         del first[col]

    #     gg = first.to_json(orient='records')
    #     first  = first.rename(index=str, columns={"Date": "x", "Close": "y"})

    #     labels = list(first['x'])
    #     values = list(first['y'])


    #     context['labels'] = labels
    #     context['values'] = values



    #     return context




#Inside Else block :

            #Get stock info
            # company_name = Stock.objects.get(stock_name=current_stock).company_name            
            # stock_obj = Stock_iex(current_stock)
            # company_name = stock_obj.company()['companyName']
            # print("\n\n\n\n Company Name is ", company_name,"\n\n\n\n")

            # url = "https://en.wikipedia.org/wiki/"+company_name
            # page = requests.get(url)
            # soup = BeautifulSoup(page.text, 'html.parser')
            # self.table = soup.find_all("table", class_="infobox vcard")[0]

            # #Get Description:
            # session = requests.Session()
            # URL = "https://en.wikipedia.org/w/api.php"
            # SEARCHPAGE = company_name
            # PARAMS = {
            #     'action': "opensearch",
            #     'list': "search",
            #     'search': SEARCHPAGE,
            #     'format': "json"
            # }

            # response = session.get(url=URL, params=PARAMS)
            # DATA = response.json()
            #self.description = DATA[2][0:2]