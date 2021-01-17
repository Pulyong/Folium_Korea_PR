Folium 라이브러리를 통한 한국 홍보
============
Imagine your Korea
------------
### Feel the Rhythm of Korea
https://www.youtube.com/c/imagineyourkorea/featured

* 외국인들에게 한국을 새로운 방식으로 소개하는 유튜브 채널입니다.

* 그 중에 Feel the Rhythm of Korea라는 프로젝트는 한국 고유의 음악을 현대식으로 재해석한 곡에 새로운 안무를 만들어 
한국의 여러 지역을 홍보하는 프로젝트 입니다.

* 현재 서울을 홍보한 영상의 조회수는 4500만회가 넘을정도로 외국인들이 관심을 가지는 영상입니다.

* 이 영상에서 영감을 얻어 Folium라이브러리로 해당 도시가 어디인지 지도로 알려주면 좋을 것 같아서 프로젝트를 시작했습니다.

scrap_url.py
----------
### 프로그램 코드

* scrap_url은 Folium을 통해 html을 만들기 전에 동영상의 주소들을 크롤링 하기위해 만든 파일입니다.

* 유튜브는 requests를 통해 크롤링이 되지 않아서 selenium을 통해 헤드리스 크롬으로 크롤링을 진행하였습니다.

* 단순히 유튜브를 통해 영상과 url만을 가져오는 것이 아니라 욕심을 내어 새로운 동영상이 올라왔을 경우 해당 도시와 좌표만 
딕셔너리에 입력하면 추가로 새로운 도시의 영상과 url도 크롤링 할 수 있게 만들었습니다.

Promotion.py
----------
### 프로그램 코드

* scrap_url.py에서 함수를 가져와서 실제로 지도안에 해당 도시의 핀을 박는 과정입니다.

* for문을 사용하여 간단하게 표현하려고 노력했고, popup에 html형식으로 유튜브 영상을 넣었습니다.

* 해당 프로그램으로 생성된 웹페이지를 현재 레퍼지토리에 올려놨습니다.

후기
----

* 아이디어부터 결과까지 스스로 기획하고 만든 작품이라 만드는데 너무 재밌었습니다.

* 남들이 봤을 때도 간단하고, 재사용이 가능하도록 코드를 만들려고 노력했습니다.

* JavaScript를 배워보고 싶다는 욕심이 커지는 계기가 됐습니다.
