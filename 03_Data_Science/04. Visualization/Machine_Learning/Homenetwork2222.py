import urllib.request
import datetime
import json
import os
import threading
import time
from random import *

g_Dehumid = False
g_Humid = False
g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

humidMax = 60
humidMin = 40

repo_base_name="BigData_Repo"
dir_delimeter='/'
depth_level2_dir="weather_info"
file_limit=3

access_key = "4ruU7ayu0r%2BGctDhbc6L3IruWayh2oiaMDsR%2Fo8iuhpo2qZTPwKyhrKj1EvfIMqssGehRSCfQlQw4uO%2BR6bSXg%3D%3D"

def make_base_dir():
    os.mkdir('.'+dir_delimeter+repo_base_name)

def make_d2_dir(dir_num):
    os.mkdir('.'+dir_delimeter+repo_base_name+'\\'+depth_level2_dir+dir_num)

def directory_num():
    dir_num=len(os.listdir('.'+dir_delimeter+repo_base_name))
    if len(os.listdir('.'+dir_delimeter+repo_base_name+dir_delimeter+depth_level2_dir+str(dir_num))) == file_limit:
        dir_num+=1
        make_d2_dir(str(dir_num))
    return str(dir_num)

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(), url))
        return  None

def getForecast(base_date, base_time, nx, ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += '&numOfRows=100'

    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return  None
    else:
        return  json.loads(retData)

def print_main_menu():
    print('\n1. 장비상태 확인')
    print('2. 장비제어')
    print('3. 스마트 모드')
    print('4. 프로그램 종료')

def print_device_status(device_name,device_status):
    print('%s 상태: '%device_name, end='')
    if device_status == True: print('작동')
    else: print('정지')

def check_device_status():
    print_device_status('난방기', g_Radiator)
    print_device_status('가스벨브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)
    print_device_status('가습기 상태', g_Humid)
    print_device_status('제습기 상태', g_Dehumid)

def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요.')
    print('1. 난방기')
    print('2. 가스벨브')
    print('3. 발코니(베란다) 창')
    print('4. 출입문')
    print('5. 가습기')
    print('6. 제습기')

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_Dehumid, g_Humid

    check_device_status()
    print_device_menu()
    menu_num = int(input('번호를 입력하세요: '))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_Humid = not g_Humid
    if menu_num == 6: g_Dehumid = not g_Dehumid
    check_device_status()

def get_realtime_weather_info():
    jsonResult = []
    now = datetime.datetime.now()
    base_date = now.strftime('%Y%m%d')
    if int(now.strftime('%M')) >= 30 and int(now.strftime('%M')) <= 59:
        base_time = now.strftime('%H%M')
    else:
        hour = int(now.strftime('%H')) - 1
        min = int(now.strftime('%M')) - 30 + 60
        base_time = str(hour) + str(min)
    nx = '89'
    ny = '91'

    jsonData = getForecast(base_date, base_time, nx, ny)
    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for i in jsonData['response']['body']['items']['item']:
            jsonResult.append(i)

    with open('.%s%s%s%s%s%s동구_신암동_초단기예보조회_%s.json' \
                  % (dir_delimeter, repo_base_name, dir_delimeter, depth_level2_dir, \
                     directory_num(), dir_delimeter, now.strftime('%Y%m%d%H%M')), \
                  'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (base_date, now.strftime('%H%M')))
    return jsonResult

def auto_control(result):
    global g_Dehumid, g_Humid, humidMin, humidMax, g_Balcony_Windows
    humid = 0
    rain = 0
    for i in result:
        if i['category'] == 'RN1':
            if i['fcstValue'] > 0:
                g_Balcony_Windows = False
                print('발코니 창문을 닫습니다.')
            rain = int(i['fcstValue'])
        if i['category'] == 'REH':
            humid = int(i['fcstValue'])
            break
    print('강우량 :', rain)
    print('습도 :', humid)
    if humid > humidMax and g_Dehumid == False:
        g_Dehumid = True
        print('제습기가 가동됩니다.')
    if humid < humidMin and g_Humid == False:
        g_Humid = True
        print('가습기가 가동됩니다.')

def simulator():
    print('1. 습한날')
    print('2. 건조한날')
    print('3. 비오는날')
    print('4. 화창한날')
    menu_num = int(input('시뮬레이션하고자 하는 날씨를 선택하세요: '))

    simul_data = []
    if not os.path.exists('./simulator'):
        os.mkdir('./simulator')

    if menu_num == 1:
        simul_data.append(
            {'category':'REH',
             'fcstValue':randint(61, 100)})
        auto_control(simul_data)
        with open('./simulator/simul_data01.json', 'w',encoding='utf-8') as outfile:
            retJson = json.dumps(simul_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
        print('simul_data01.json SAVED')
    elif menu_num == 2:
        simul_data.append(
            {'category': 'REH',
             'fcstValue': randint(1, 40)})
        auto_control(simul_data)
        with open('./simulator/simul_data02.json', 'w', encoding='utf-8') as outfile:
            retJson = json.dumps(simul_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
        print('simul_data02.json SAVED')
    elif menu_num == 3:
        simul_data.append(
            {'category': 'RN1',
             'fcstValue': randint(1, 200)})
        auto_control(simul_data)
        with open('./simulator/simul_data03.json', 'w', encoding='utf-8') as outfile:
            retJson = json.dumps(simul_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)
        print('simul_data03.json SAVED')
    elif menu_num == 4:
        pass

def smart_mode():
    global g_AI_Mode, g_Dehumid, g_Humid, g_Balcony_Windows, humidMax, humidMin
    print('1. 인공지능 모드 조회')
    print('2. 인공지능 모드 상태 변경')
    print('3. 실시간 기상정보 Update')
    print('4. 시뮬레이터 모드')
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num == 1:
        print('현재 인공지능 모드: ', end='')
        if g_AI_Mode == True: print('작동')
        else: print('중지')
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print('현재 인공지능 모드: ', end='')
        if g_AI_Mode == True: print('작동')
        else: print('중지')
    elif menu_num == 3:
        if not os.path.exists('.' + dir_delimeter + repo_base_name):
            make_base_dir()
        if not os.path.exists('.' + dir_delimeter + repo_base_name + dir_delimeter + depth_level2_dir + '1'):
            make_d2_dir('1')
        result = get_realtime_weather_info()
        if g_AI_Mode == True:
            auto_control(result)
    elif menu_num == 4:
        simulator()

def update_scheduler():
    global g_Balcony_Windows, g_Humid, g_Dehumid, humidMax, humidMin
    while True:
        if g_AI_Mode == False:
            continue
        else:
            result = get_realtime_weather_info()
            auto_control(result)
            time.sleep(60*60)

t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()


print('<스마트 홈네트워크 시뮬레이션 프로그램 ver1.0>')
while True:
    print_main_menu()
    menu_num = int(input('메뉴를 선택하세요: '))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        break