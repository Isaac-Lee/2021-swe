import pymysql

def create_db():

    #database 접근
    db = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        passwd='mysql pw',
                        db='satellite',
                        charset='utf8')
    
    # database를 사용하기 위한 cursor
    cursor= db.cursor()

    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    
    # user 스키마 생성 
    # 컬럼 : (userid(pk)), userpw, name 
    create_user_table = """CREATE TABLE IF NOT EXISTS user(
            userId VARCHAR(256) NOT NULL,
            userPw VARCHAR(256) NOT NULL,
            name VARCHAR(256) NOT NULL,
            PRIMARY KEY(userId)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    # image 스키마 생성
    # 컬럼 : (userid(fk), url), title, shootingperiod, shootingtime,keyword
    create_image_table = """CREATE TABLE IF NOT EXISTS image(
            userId VARCHAR(256) NOT NULL,
            url VARCHAR(256) NOT NULL,
            title VARCHAR(256) NOT NULL,
            shootingPeriod VARCHAR(256) NOT NULL,
            shootingTime VARCHAR(256) NOT NULL,
            keyword VARCHAR(256) NOT NULL,
            FOREIGN KEY(userId) REFERENCES user(userid),
            PRIMARY KEY(userId,url)
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