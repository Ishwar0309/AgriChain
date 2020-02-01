from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import json
from django.http import JsonResponse
import matplotlib.pyplot as plt

def index(request):
    return render(request,'user/analyse.html')

def analyse(request):
    post_id = request.GET.get('post_id')
    df = pd.read_csv("media/csvfiles/new.csv")
    predict_year_labels = [2013,2014,2015,2016,
                   2017,2018,2019]
    year_labels = [1999,2000,2001,2002,2003,2004,
                   2005,2006,2007,2008,2009,2010,
                   2011,2012,2013,2014,2015,2016,
                   2017,2018,2019]

    # years = np.arange(2013,2020).reshape(-1,1)
    dict = {label:0 for label in year_labels}
    data = {}

    if post_id == 'bajra':
        bajra_val1 = []
        bajra_val2 = []
        for year,bajra in zip(df['Year'],df['Bajra_area']):
            if bajra:
                dict[year] = bajra
                bajra_val1.append(bajra)
        print(dict)
        X = np.array(df[['Year','Bajra_area']]).reshape(-1,2)
        Y = np.array(df['Bajra'])
        linear_clf = LinearRegression()
        linear_clf.fit(X,Y)
        Bajra_predict = linear_clf.predict(np.array([[2013,5975899],[2014,6280987],
                            [2015,5767891],[2016,6995811],
                            [2017,5863171],[2018,5865861],
                            [2019,5977992]]).reshape(-1,2))
        Bajra_predict.reshape(-1,1)
        for year,bajra in zip(predict_year_labels,Bajra_predict):
            dict[year] = bajra
            bajra_val2.append(bajra)
        print(dict)
        data['title'] = 'Bajra Cultivation Statistics'
        options = {
            'title': {
                'display': True,
                'text': 'Bajra Cultivation Statistics'}
        }
        datae = {
            'labels' :  year_labels,
            'datasets' : [{
                'label': 'Old Statistics',
                'data': bajra_val1,
                'fill': True,
                # 'backgroundColor': "#0074D9",
                'borderColor': "#7FDBFF"
                },
                {
                    'label': 'Predicted Statistics',
                    'data': bajra_val1+bajra_val2,
                    'fill': -1,
                    # 'backgroundColor': "#B10DC9",
                    'borderColor': "#FFDC00"
                }]
        }
        data['datasets'] = datae
        data['options'] = options
        print(data)
        print(dict)
        return JsonResponse(data)
        # print("ALRETEDDDDDDD")
        # plt.plot(df['Year'],df['Bajra'],label="Old Stats")
        # # plt.plot(years,Bajra_predict,label="Predicted Stats")
        # plt.title('Bajra Statistics')
        # plt.ylabel('Bajra Cultivation')
        # plt.legend()
        # plt.ticklabel_format(useOffset=False, style='plain',axis='both')
    if post_id == 'wheat':
        wheat_val1 = []
        wheat_val2 = []
        for year,wheat in zip(df['Year'],df['Wheat_area']):
            if wheat:
                dict[year] = wheat
                wheat_val1.append(wheat)
        print(dict)
        X = np.array(df[['Year','Wheat_area']]).reshape(-1,2)
        Y = np.array(df['Wheat'])
        linear_clf = LinearRegression()
        linear_clf.fit(X,Y)
        Wheat_predict = linear_clf.predict(np.array([[2013,2975899],[2014,2980987],[2015,3367891],
                            [2016,3265811],[2017,3163871],[2018,3465861],
                            [2019,3577992]]).reshape(-1,2))
        Wheat_predict.reshape(-1,1)
        for year,wheat in zip(predict_year_labels,Wheat_predict):
            dict[year] = wheat
            wheat_val2.append(wheat)
        print(dict)
        data['title'] = 'Wheat Cultivation Statistics'
        options = {
            'title': {
                'display': True,
                'text': 'Wheat Cultivation Statistics'}
        }
        datae = {
            'labels' :  year_labels,
            'datasets' : [{
                'label': 'Old Statistics',
                'data': wheat_val1,
                'fill': -1,
                # 'backgroundColor': "#0074D9",
                'borderColor': "#7FDBFF"
                },
                {
                    'label': 'Predicted Statistics',
                    'data': wheat_val1+wheat_val2,
                    'fill': -1,
                    # 'backgroundColor': "#B10DC9",
                    'borderColor': "#FFDC00"
                }]
        }
        data['datasets'] = datae
        data['options'] = options
        print(data)
        print(dict)
        return JsonResponse(data)
        # plt.plot(df['Year'],df['Wheat'],label="Old Stats")
        # # plt.plot(years,Wheat_predict,label="Predicted Stats")
        # plt.title('Wheat Statistics')
        # plt.xlabel('Years')
        # plt.ylabel('Wheat Cultivation')
        # plt.legend()
        # plt.ticklabel_format(useOffset=False, style='plain',axis='both')
    if post_id == "jowar":
        jowar_val1 = []
        jowar_val2 = []
        for year,jowar in zip(df['Year'],df['Jowar_area']):
            if jowar:
                dict[year] = jowar
                jowar_val1.append(jowar)
        print(dict)
        X = np.array(df[['Year','Jowar_area']]).reshape(-1,2)
        Y = np.array(df['Jowar'])
        linear_clf = LinearRegression()
        linear_clf.fit(X,Y)
        Jowar_predict = linear_clf.predict(np.array([[2013,497589],[2014,698009],
                            [2015,720891],[2016,920511],
                            [2017,840871],[2018,545861],
                            [2019,667992]]).reshape(-1,2))
        Jowar_predict.reshape(-1,1)
        for year,jowar in zip(predict_year_labels,Jowar_predict):
            dict[year] = jowar
            jowar_val2.append(jowar)
        data['title'] = 'Jowar Cultivation Statistics'
        options = {
            'title': {
                'display': True,
                'text': 'Jowar Cultivation Statistics'}
        }
        datae = {
            'labels' :  year_labels,
            'datasets' : [{
                'label': 'Old Statistics',
                'data': jowar_val1,
                'fill': -1,
                # 'backgroundColor': "#0074D9",
                'borderColor': "#7FDBFF"
                },
                {
                    'label': 'Predicted Statistics',
                    'data': jowar_val1+jowar_val2,
                    'fill': -1,
                    # 'backgroundColor': "#B10DC9",
                    'borderColor': "#FFDC00"
                }]
        }
        data['datasets'] = datae
        data['options'] = options
        print(data)
        print(dict)
        return JsonResponse(data)
        # plt.plot(df['Year'],df['Jowar'],label="Old Stats")
        # # plt.plot(years,Jowar_predict,label="Predicted Stats")
        # plt.title('Jowar Statistics')
        # plt.xlabel('Years')
        # plt.ylabel('Jowar Cultivation')
        # plt.legend()
        # plt.ticklabel_format(useOffset=False, style='plain',axis='both')

    if post_id == 'barley':
        barley_val1=[]
        barley_val2=[]
        for year,barley in zip(df['Year'],df['Barley_area']):
            if barley:
                dict[year] = barley
                barley_val1.append(barley)
        print(dict)
        X = np.array(df[['Year','Barley_area']]).reshape(-1,2)
        Y = np.array(df['Barley'])
        linear_clf = LinearRegression()
        linear_clf.fit(X,Y)
        Barley_predict = linear_clf.predict(np.array([[2011,397589],[2012,180987],[2013,236891],
                            [2014,126811],[2015,363871],[2016,265861],
                            [2017,277992]]).reshape(-1,2))
        Barley_predict.reshape(-1,1)
        for year,barley in zip(predict_year_labels,Barley_predict):
            dict[year] = barley
            barley_val2.append(barley)
        print(dict)
        data['title'] = 'Barley Cultivation Statistics'
        options = {
            'title': {
                'display': True,
                'text': 'Barley Cultivation Statistics'}
        }
        datae = {
            'labels' :  year_labels,
            'datasets' : [{
                'label': 'Old Statistics',
                'data': barley_val1,
                'fill': -1,
                # 'backgroundColor': "#0074D9",
                'borderColor': "#7FDBFF"
                },
                {
                    'label': 'Predicted Statistics',
                    'data': barley_val1+barley_val2,
                    'fill': -1,
                    # 'backgroundColor': "#B10DC9",
                    'borderColor': "#FFDC00"
                }]
        }
        data['datasets'] = datae
        data['options'] = options
        print(data)
        print(dict)
        return JsonResponse(data)

        # plt.plot(df['Year'],df['Barley'],label="Old Stats")
        # # plt.plot(years,Barley_predict,label="Predicted Stats")
        # plt.title('Barley Statistics')
        # plt.xlabel('Years')
        # plt.ylabel('Barley Cultivation')
        # plt.legend()
        # plt.ticklabel_format(useOffset=False, style='plain',axis='both')

    if post_id == "maize":
        maize_val1 =[]
        maize_val2 =[]
        for year,maize in zip(df['Year'],df['Maize_area']):
            if maize:
                dict[year] = maize
                maize_val1.append(maize)
        print(dict)
        X = np.array(df[['Year','Maize_area']]).reshape(-1,2)
        Y = np.array(df['Maize'])
        linear_clf = LinearRegression()
        linear_clf.fit(X,Y)
        Maize_predict = linear_clf.predict(np.array([[2013,1035899],[2014,1080987],
                            [2015,1067891],[2016,1095999],
                            [2017,1163871],[2018,1065861],
                            [2019,1177992]]).reshape(-1,2))
        Maize_predict.reshape(-1,1)
        for year,maize in zip(predict_year_labels,Maize_predict):
            dict[year] = maize
            maize_val2.append(maize)
        print(dict)
        data['title'] = 'Maize Cultivation Statistics'
        options = {
            'title': {
                'display': True,
                'text': 'Maize Cultivation Statistics'}
        }
        datae = {
            'labels' :  year_labels,
            'datasets' : [{
                'label': 'Old Statistics',
                'data': maize_val1,
                'fill': -1,
                # 'backgroundColor': "#0074D9",
                'borderColor': "#7FDBFF"
                },
                {
                    'label': 'Predicted Statistics',
                    'data': maize_val1+maize_val2,
                    'fill': -1,
                    # 'backgroundColor': "#B10DC9",
                    'borderColor': "#FFDC00"
                }]
        }
        data['datasets'] = datae
        data['options'] = options
        print(data)
        print(dict)
        return JsonResponse(data)

        # plt.plot(df['Year'],df['Maize'],label="Old Stats")
        # # plt.plot(years,Maize_predict,label="Predicted Stats")
        # plt.title('Maize Statistics')
        # plt.xlabel('Years')
        # plt.ylabel('Maize Cultivation')
        # plt.legend()
        # plt.ticklabel_format(useOffset=False, style='plain',axis='both')


# def getData(request):
#
#     temp = {'rice':[1,2,3],
#             'bajra':{'old':[1,2,8],'predicted':[8,6,5]},
#             'wheat':[2,5,6]}
#     return JsonResponse(temp[post_id],safe=False)

