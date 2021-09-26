import pymysql

def create_db():

    #database 접근
    db = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        passwd='MySQL 비밀번호',
                        db='satellite',
                        charset='utf8')
    
    # database를 사용하기 위한 cursor
    cursor= db.cursor()
    
    # user 스키마 생성 
    # 컬럼 : (userid(pk)), userpw, name 
    create_user_table = """CREATE TABLE IF NOT EXISTS user(
            userId VARCHAR(256) NOT NULL,
            userPw VARCHAR(256) NOT NULL,
            name VARCHAR(256) NOT NULL,
            PRIMARY KEY(userId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    # image 스키마 생성
    # 컬럼 : (imageNum, userid(fk)), title, 이미지 url
    # shootingtime, shootingperiod, color, font 의 경우 굳이 저장할 필요 없음 
    create_image_table = """CREATE TABLE IF NOT EXISTS image(
            imageNum  INT UNSIGNED NOT NULL AUTO_INCREMENT,
            userId VARCHAR(256) NOT NULL,
            title VARCHAR(256) NOT NULL,
            url VARCHAR(256) NOT NULL,
            FOREIGN KEY(userId) REFERENCES user(userid),
            PRIMARY KEY(imageNum, userId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    # SQL query 실행
    cursor.execute(create_user_table)
    cursor.execute(create_image_table)

    # SQL query 작성
    #sql= """INSERT INTO test(name, nick)
    #     VALUES('test_name', 'test_nickname');"""

    # SQL query 실행
    #cursor.execute(sql)
    #cursor.execute(input_sql)
    
    # 데이터 변화 적용
    db.commit()
    
    # Database 닫기
    db.close()