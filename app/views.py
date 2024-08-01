from django.http import JsonResponse

from selenium import webdriver
from bs4 import BeautifulSoup

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--disable-gpu") 
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Create your views here.
def taiwan(request):
    url = 'https://www.cwa.gov.tw/V8/C/W/County/index.html'
    driver = webdriver.Chrome(options = options)
    driver.get(url)
    sp = BeautifulSoup(driver.page_source, 'html.parser')

    district = ["基隆市", "臺北市", "新北市", "桃園市", "新竹市", "新竹縣", "苗栗縣", "臺中市", 
            "彰化縣", "南投縣", "雲林縣", "嘉義市", "嘉義縣", "臺南市", "高雄市", "屏東縣", 
            "宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣"]

    rain = sp.find_all("span", class_ = "rain")
    rain = [t.text for t in rain]

    temp = sp.find_all("span", class_ = "tem-C is-active")
    temperature = [temp[i].find_all("i") for i in range(len(district))]
    temperature = [[t[0].text, t[1].text] for t in temperature]

    return JsonResponse({'district':district, 'rain':rain, 'temperature':temperature})

def us(request):
    url = 'https://www.accuweather.com/en/us/united-states-weather#google_vignette'
    driver = webdriver.Chrome(options = options)
    driver.get(url)
    sp = BeautifulSoup(driver.page_source, 'html.parser')

    district = sp.find_all("span", class_ = "text title no-wrap")
    district = [t.text for t in district]

    temperature = sp.find_all("span", class_ = "text temp")
    temperature = [t.text for t in temperature]

    return JsonResponse({'district':district, 'temperature':temperature})
