# 서버리스

[ 17일 실시간 ]

- 5일 서버리스 : 2차 프로젝트를 서버리스로
- 6일 스프링
- 6일 도커, 쿠버네티스

## 서버리스 프론트엔드

네임서버
ssh
22번포트의 의미
sudo : 관리자 권한으로 실행
presudo :
service : apt-get install 한 것 은 service에 등록됨

인스턴스 재부팅 -> ip주소 바뀜

서버 접속 : `ssh -i 키이름.pem ubuntu@ip주소`

sftp연결 후 파일 업로드 : `sftp -i 키이름.pem ubuntu@ip주소`, `put index.html`

패키지 매니저 업데이트 : `sudo apt-get update`

nginx 상태 체크 : `sudo service nginx status`

nginx 중지/실행 : `sudo service nginx stop/start`

포트 확인 : `netstat -tnlp`

http로 접속해보기 : `curl localhost`

`histroty`

웹서버 종류

- nginx
- apache
