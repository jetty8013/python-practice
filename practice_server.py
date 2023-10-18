import pymysql
from flask import Flask, jsonify
import os

password = os.environ.get('MYSQL_PASSWORD')

app = Flask(__name__)

# MySQL 연결 정보 설정
conn = pymysql.connect(
    host='ec2-3-39-192-92.ap-northeast-2.compute.amazonaws.com',
    user='root',
    password=password,  # 환경 변수에서 읽어온 비밀번호 사용
    database='account_info',
    port=3306,
    charset='utf8'
)

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        # 커서 생성
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()

        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'email': user[2]
            }
            user_list.append(user_dict)

        return jsonify(user_list)

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
