# 2021-swe 
2021 Fall Semester SW Engineering Term Project  

## 🌏 SDD(Satellite Data Display)  
☑ 날짜, 기간 등 세부 조건을 사용자가 원하는 대로 선택하여 조회한 인공위성 산출물 전시 영상을 제공  
☑ 영상의 제목, 위도 및 경도의 폰트 크기를 사용자가 원하는대로 커스텀하여 조회가능하며 갤러리에 저장   
☑ 갤러리에서 한 번에 여러 전시 영상을 다운 받을 수 있으며 한 번 다운 받았던 영상을 다시 다운로드 가능   

## 📄 기능
- 회원가입
<img width="800" alt="signin" src="https://user-images.githubusercontent.com/52441906/150471262-47bab8f3-1dfa-4ac6-a435-4afd32c4c9dd.png" >
</br>

- 로그인 
<img width="800" alt="login" src="https://user-images.githubusercontent.com/52441906/150471278-2405916c-8cad-4265-9d8c-e8607a7b5970.png">
</br>

- 인공위성 영상 조회 / 갤러리 저장 
<img width="800" alt="login" src="https://user-images.githubusercontent.com/52441906/150473131-b5bb6462-5cc8-41e0-9463-7f8dba8752ce.gif">

</br>

- 갤러리 전시 / 다운로드 / 삭제

<img width="800" alt="login" src="https://user-images.githubusercontent.com/52441906/150473403-c3ead6be-dfae-4bf6-b5f3-ad24030b74f3.gif">

## 🖥 실행방법
### Frontend 
```bash
npm start
```
### Backend 
1. `backend/app.py`, `backend/db.py` 자신의 PC에 설치된 local mysql password로 변경
2. `backend/config.py` 파일 생성 후 Access key 입력
3. `requirements.txt` 모듈 설치   
```bash
pip install -r requirements
```

### Satellite Data 

1. `backend/map_generator/data`에 데이터 추가
2. `backend/map_generator/config/config.yaml`에 데이터의 설정 정보 추가
