import pymysql
import os

password = os.environ.get('MYSQL_PASSWORD')

# MySQL 연결 정보 설정
conn = pymysql.connect(
    host='ec2-3-39-192-92.ap-northeast-2.compute.amazonaws.com',
    user='root',
    password=password,  # 환경 변수에서 읽어온 비밀번호 사용
    port=3306,
    charset='utf8'
)

try:
    # 커서 생성
    cursor = conn.cursor()
    
    # MySQL 서버에 접속이 성공하면 이 메시지를 출력
    print("MySQL 서버에 접속 성공")

except pymysql.MySQLError as e:
    # 접속 오류가 발생하면 이 메시지를 출력
    print("MySQL 서버에 접속 실패: %s" % e)

finally:
    # 연결 종료
    conn.close()
