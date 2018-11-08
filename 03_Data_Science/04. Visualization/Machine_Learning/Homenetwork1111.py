import urllib.request
import datetime
import json
import threading
import time
import random

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_Humidifier = False
g_Dehumidifier = False
g_AI_Mode = False

json_weather_result = []
json_aircondition_result = []
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
day_sec = time.strftime("%S")
x_coodinate = "89"
y_coodinate = "91"

sim_max_humidity = 30
sim_min_humidity = 10
sim_rainfall = 10

code = 'PM10'
datatype = 'DAILY'
period = 'MONTH'

access_key = "jsU49qLNy9Sw%2BOJGYi0nmPVeCe4wvPMY%2BhHxtp59eomTVUTfmq106chOxh5WafWv3eKjTcngemuF0SjFRxkCBw%3D%3D"

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, device_status):
    print("%s 상태 : " % device_name, end="")
    if device_status == True: print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다) 창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요 : "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

def get_Request_URL(url): # (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url) # request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
#        if response.getcode() == 200:
        if response.getcode() == 00:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time): # (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=100"

    url = end_point + parameters

    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def get_Aircondition_URL(): # (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst"

    parameters = "?itemCode" + code
    parameters += "&dataGubun=" + datatype
    parameters += "&searchCondition=" + period
    parameters += "&pageNo=1"
    parameters += "&&numOfRows=1"
    parameters += "&ServiceKey=" + access_key

    url = end_point + parameters

    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time): # (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)
    yyyymmdd = time.strftime("%Y%m%d")
    day_sec = time.strftime("%S")

    if jsonData['response']['header']['resultMsg'] == 'OK':
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s_%s_%s.json' % (yyyymmdd, day_time, day_sec), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s_%s.json SAVED\n' % (yyyymmdd, day_time, day_sec))

def Make_Airconditon_Json(): # (1) 기상 정보(대기환경 시도별 실시간 측정정보) json 파일 생성하는 함수
    jsonData = get_Aircondition_URL()
    yyyymmdd = time.strftime("%Y%m%d")
    day_sec = time.strftime("%S")

    if jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
        for prn_data in jsonData['response']['body']['items']['item']:
            json_aircondition_result.append({'dataTime': prn_data.get('dataTime'),
                               'itemCode': prn_data.get('itemCode'),
                               'dataGubun': prn_data.get('dataGubun'),
                               'daegu': prn_data.get('daegu')})

    with open('대구_대기환경_측정정보_%s_%s_%s.json' % (yyyymmdd, day_time, day_sec), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_aircondition_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('대구_대기환경_측정정보_%s_%s_%s.json' % (yyyymmdd, day_time, day_sec))

def get_Realtime_Weather_Info(): # (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59: # 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30: # 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int-30) # 정확히 30분을 뺀다.
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min) # 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌
        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    return day_time

def update_scheduler():
    if day_min == 30:
        while True:
            if g_AI_Mode == False:
                continue
            else:
                time.sleep(3600)
                Realtime_smart_mode()

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print("4. 시뮬레이터 모드")
    menu_num = int(input("메뉴를 선택하세요 : "))

    if menu_num == 1:
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True: print("작동")
        else: print("중지")
        #start_smart_mode()
        #Realtime_smart_mode()
        #t = threading.Thread(target=update_scheduler)
        #t.daemon = True
        #t.start()
    if menu_num == 3:
        get_Realtime_Weather_Info()
    elif menu_num == 4:
        simulate_mode()

def start_smart_mode():
    global g_Balcony_Windows
    global g_Dehumidifier
    global sim_rainfall
    global sim_max_humidity
    global sim_min_humidity
    day_min_int = int(day_min)
    with open('동구_신암동_초단기예보조회_%s_%s_%s.json' % (yyyymmdd, get_Realtime_Weather_Info(), day_sec), 'r', encoding='utf-8') as f:
        info = json.load(f)
    if 0 <= day_min_int <= 30:
        day_hour_int = int(day_hour)
        day_time = (day_hour_int) * 100
    else:
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int + 1
        day_time = (day_hour_int) * 100
    for dict in info:
        if dict['category'] == "RN1" and dict['fcstTime'] == day_time:
            rainfall = dict['fcstValue']
        if dict['category'] == "REH" and dict['fcstTime'] == day_time:
            humidity = dict['fcstValue']

    g_Balcony_Windows = True

    if rainfall > sim_rainfall:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = not g_Balcony_Windows
            print("발코니 창 닫음")
    if humidity > sim_max_humidity:
        if g_Dehumidifier == False:
            g_Dehumidifier = not g_Dehumidifier
            print("제습기 작동")
        else: print("정지")

def Realtime_smart_mode():
    global g_Balcony_Windows
    global g_Dehumidifier
    global sim_rainfall
    global sim_max_humidity
    global sim_min_humidity
    day_min_int = int(day_min)
    day_sec = time.strftime("%S")
    with open('동구_신암동_초단기예보조회_%s_%s_%s.json' % (yyyymmdd, get_Realtime_Weather_Info(), day_sec), 'r', encoding='utf-8') as f:
        info = json.load(f)
    if 0 <= day_min_int <= 30:
        day_hour_int = int(day_hour)
        day_time = (day_hour_int) * 100
    else:
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int + 1
        day_time = (day_hour_int) * 100
    for dict in info:
        if dict['category'] == "RN1" and dict['fcstTime'] == day_time:
            rainfall = dict['fcstValue']
        if dict['category'] == "REH" and dict['fcstTime'] == day_time:
            humidity = dict['fcstValue']

    g_Balcony_Windows = True

    if rainfall > sim_rainfall:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = not g_Balcony_Windows
            print("발코니 창 닫음")
    if humidity > sim_max_humidity:
        if g_Dehumidifier == False:
            g_Dehumidifier = not g_Dehumidifier
            print("제습기 작동")
        else: print("정지")


def simulate_mode():
    while True:
        print("1. 습한날")
        print("2. 건조한날")
        print("3. 비오는날")
        print("4. 화창한날")
        menu_num = int(input("시뮬레이션하고자 하는 날씨를 선택하세요 : "))
        create_simulate_data(menu_num)

def create_simulate_data(menu_num):
    jsonResult = {}

    global g_Dehumidifier
    global g_Humidifier
    global g_Balcony_Windows

    if menu_num == 1:
        jsonResult['REH'] = random.randrange(61, 101)
        g_Dehumidifier = True
        print("가습기 작동")
    if menu_num == 2:
        jsonResult['REH'] = random.randrange(0, 40)
        g_Humidifier = True
        print("제습기 작동")
    if menu_num == 3:
        jsonResult['RN1'] = random.randrange(1, 201)
        g_Balcony_Windows = False
        print("발코니 창 닫기")
    if menu_num == 4:
        jsonResult['pm10Value'] = random.randrange(0, 51)
        jsonResult['RN1'] = 0
        g_Balcony_Windows = True
        print("발코니 창 열기")

    with open('동구_신암동_초단기예보조회(sim)_%s_%s_%s.json' % (yyyymmdd, day_time, day_sec), 'w', encoding='utf8') as outfile:
        jsonData = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonData)

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요 : "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        break

Make_Airconditon_Json()