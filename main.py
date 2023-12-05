import mysql.connector

# MySQL 서버에 연결
db = mysql.connector.connect(
    host='192.168.56.101',
    port=4567,
    user='jyheo',
    password='2023',
    database='TERM_P'
    charset='utf8'
)

cursor = db.cursor()
'''
sql문 입력받거나 sql 변수에 넣음.
'''
while True:
    print("===============")
    print("1. 학생 추가")
    print("2. 단과대로 검색")
    print("3. 팀 소속으로 검색")
    print("4. 종료")
    print("===============")
    
    choice = input("원하는 작업을 선택하시오(1/2/3/4): ")
    
    if choice == '4':
        break
        
    if choice == '1':
        print("학생 정보를 입력하기 위한 테이블은 다음 형식을 따릅니다.")
        cursor.execute("SHOW COLUMNS FROM student")
        
        inform_str = input("각 정보를 공백 기준으로 구분하여 입력하세요")
        name, st_num, dep, response, team = inform_str.split(" ")
        cursor.execute("INSERT INTO student (name, st_num, dep, res, team) VALUES(" +name + ',' + st_num + ',' + dep + ',' + response + ',' +team+ ')')
        
        print("입력되었습니다.")
       


cursor.execute(sql)
idx = cursor.fetchall() ##ㅇㅇㅇ


db.commit()

#종료
cursor.close()
db.close()