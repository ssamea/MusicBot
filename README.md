# MusicBot
- Discord for Listening Music with Python
- 셀레니움을 이용한 뮤직 봇  파이썬으로 구현하기

## 사전 필요한 준비문
- Discord 사이트에서 개발자 메뉴에서 Bot을 생성한 후 토큰을 저장해주세요
- cmd나 그 외 IDE 터미널에서 필요한 패키지들을 설치해줍니다
- pip install discord
- pip install selenium
- pip install beautifulsoup4
- pip install youtube_dl
- pip install requests
- pip install asyncio
- 크롬에서 ffmpeg를 다운받아 설치해주시고 추후 코드에 ffmpeg 실행파일의 환경 변수 'path'에 경로를  넣어주세요 
- URL없이 이름으로 검색하기위해 크롤링을 하는 크롬드라이버를 설치해주시고 실행파일의 경로를 코드에 적어주세요 (코드 보시면 주석있습니다)

## 1. 봇 인사 기능
![봇인사말](https://user-images.githubusercontent.com/49589578/118580813-7db21900-b7cb-11eb-8983-51c72c64af55.JPG)

## 2. 봇 입장 명령 기능
![봇조인](https://user-images.githubusercontent.com/49589578/118580814-7ee34600-b7cb-11eb-8ce4-7b12db5af077.JPG)

## 3. 봇 노래 재생 명령 기능
![노래재생](https://user-images.githubusercontent.com/49589578/118580815-7ee34600-b7cb-11eb-9ffa-6ebeaca28980.JPG)
![크롤링](https://user-images.githubusercontent.com/49589578/118581523-bef6f880-b7cc-11eb-8d16-8421e467c088.JPG)

## 4. 봇 노래 재생 끄기 기능
![끄기](https://user-images.githubusercontent.com/49589578/118585371-b81fb400-b7d3-11eb-8279-ad7136ff6de7.JPG)

## 5. 노래 리스트 추가 기능
![add](https://user-images.githubusercontent.com/49589578/118585364-b655f080-b7d3-11eb-814b-3e20edbece94.JPG)

## 6. 노래 리스트 삭제 기능
![rm](https://user-images.githubusercontent.com/49589578/118585367-b6ee8700-b7d3-11eb-9a4a-d28ad4f522ad.JPG)

## 7. 현재 노래 리스트 목록 출력 기능
![list](https://user-images.githubusercontent.com/49589578/118585366-b655f080-b7d3-11eb-91bc-4445ad233927.JPG)

## 8. 현재 재생 노래 제목 출력 기능
![nowplaying](https://user-images.githubusercontent.com/49589578/118585369-b7871d80-b7d3-11eb-9cdb-988c810a7991.JPG)

## 9. 현재 재생중인 노래 일시정지 기능
![pause](https://user-images.githubusercontent.com/49589578/118585361-b5bd5a00-b7d3-11eb-94dd-15b506064c78.JPG)
