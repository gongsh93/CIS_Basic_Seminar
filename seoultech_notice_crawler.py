import requests
from bs4 import BeautifulSoup

def seoultech_notice_crawling():
    html = requests.get('http://www.seoultech.ac.kr/service/info/notice/').text
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find(class_="tbl_list")
    # class_="XXX" or id="XXX" 를 이용해 HTML 태그를 검색할 수 있음
    tbody = table.find("tbody")

    result = [] # 게시글 정보(제목, 날짜)들을 담을 배열 선언
    for tr in tbody.find_all("tr"):
        tds = tr.find_all("td")
        title = tds[1].find("a").contents[0].strip() 
        # .content[0]은 해당 태그 안에 적힌 텍스트를 가져옴
        # .strip() 함수는 텍스트 좌우의 불필요한 공백, 개행문자를 제거함
        date = tds[4].contents[0].strip()
        result.append([title, date])
    
    return result

if __name__ == "__main__":
    notices = seoultech_notice_crawling()
    for notice in notices:
        print(notice)