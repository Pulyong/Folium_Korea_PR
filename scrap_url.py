import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

def headless_chrome(): # 헤드리스 크롬 실행
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=2560x1440")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get("https://www.youtube.com/playlist?list=PL4Lb93R1nd7ctttoHCmCXxEZcGy_KUYpY")
    soup = BeautifulSoup(browser.page_source,"lxml")
    print("시스템 동작중...")
    return soup

def scrap_url(): # 도시 이름과 해당 유튜브url 가져오기
    title_lists=[]
    url_lists=[]    
    soup = headless_chrome()  
    video_titles = soup.find_all("span",attrs={'id':'video-title'})
    video_url = soup.find_all("a",attrs={'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})
    for i in video_titles:
        title = i.get_text().strip()
        title_lists.append(title)
    for i in video_url:
       url = "https://www.youtube.com"+i["href"]
       url = re.split('[=&]+',url)
       url_lists.append(url[1])
    return title_lists,url_lists

def sum_list(): # 도시이름,url을 하나의 리스트로 만들기
    title_url_list = []
    title_lists,url_lists = scrap_url()
    for i in range(len(title_lists)):
        title_url_list.append([title_lists[i],url_lists[i]])
    return title_url_list
    
def run(): # 딕셔너리의 순서와 리스트의 순서 일치시키기
    title_url_list = sum_list()
    match_list = []
    for key in list(pr_dict.keys()):
        for title in title_url_list:
            pattern = f"{key}"
            text = f"{title[0]}"
            if re.search(pattern,text):
                match_list.append((re.search(pattern,text).group(),title[1]))
            else:
                continue
    print("시스템 동작 완료!")
    return match_list          

pr_dict = {"SEOUL":[37.55997841731841, 126.97529766418414],
            "BUSAN":[35.14854620239508, 129.12981211447476],
            "JEONJU":[35.81545662436752, 127.15346127143155],
            "ANDONG":[37.476877710226944, 127.04996061215674],
            "MOKPO":[34.781394296973474, 126.38328745213919],
            "GANGNEUNG":[37.691611597754395, 129.032888716986]}
if __name__ == '__main__':
    match_list = run()
    print(match_list)

    
    
            
