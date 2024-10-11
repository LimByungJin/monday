# matplotlib=차트 
import matplotlib.pyplot as plt
import matplotlib 
import time
import numpy as np
font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False
import seaborn as sns 


import pandas as pd
import numpy as np
import time

#새로운import
import urllib.request
import json


#1단계
def getRequestURL(url, enc='utf-8'):
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        if response.getcode()==200:
            first = response.read()
            
            print(first)
            print('- ' * 70)


            ret = first.decode(enc)
            print(ret)
        return ret
    except Exception as ex:
        print('10-02-수요일 에러이유 ', ex)
        

# 문서형태json 100행갯수  1페이지 서울지역  ver=1.0
# json_data = getAirsido('json','100','1','서울','1.0') 
# https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=본인껏~D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0
#2단계
def getAirsido(returnType,rownum,pageNo, sidoName, ver ):
    print()
    print('공공데이터 시도별 실시간 측정정보 조회getAirsido()')
    serviceKey='수정수정여러분껏'
    url='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
    parameter = '?_type=json&serviceKey='+serviceKey
    parameter =  parameter + '&returnType=' + returnType
    parameter =  parameter + '&numOfRows='+rownum + '&pageNo='+pageNo
    parameter =  parameter + '&sidoName='+urllib.parse.quote(sidoName) +'&ver='+ver
    url = url + parameter
    print(url)
    print()
    ret_data  = getRequestURL(url)
    print()

    print('ㄴ결과 ' , ret_data)
    if ret_data == None:
        None
    else:
        return json.loads(ret_data)
    

#3단계
print('air미세먼지 test 시작 12시 28분 ')
result = [ ]
for i  in range(6): 
    # 문서형태json 100행갯수  1페이지 서울지역  version=1.0
    json_data = getAirsido('json','100','1','서울','1.0') 
    if(json_data['response']['header']['resultMsg']=='NORMAL_CODE'):
        sidoName = json_data['response']['body']['items'][i]['sidoName']
        stationName = json_data['response']['body']['items'][i]['stationName']
        o3Value =  json_data['response']['body']['items'][i]['o3Value'] #오존농도
        no2Value = json_data['response']['body']['items'][i]['no2Value'] #이산화질소농도
        pm10Grade = json_data['response']['body']['items'][i]['pm10Grade'] #미세먼지농도
        print(f'sidoName={sidoName} stationName={stationName} o3Value={o3Value} no2Value={no2Value} pm10Grade={pm10Grade}')
        result.append([sidoName]+[stationName]+[o3Value]+[no2Value]+[pm10Grade])          
           

print()
print(result)
df = pd.DataFrame(result)
path = './data/air.csv'
#df.to_csv(path, encoding='cp949')
#print(path, '파일 저장 성공했습니다')
print('air미세먼지 test 접근 성공  12시 28분 ')
print()
