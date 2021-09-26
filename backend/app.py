from os import path
from flask import Flask
from flask_restx import Api, Resource, reqparse

from db import create_db

app = Flask(__name__)
api = Api(app)
user_ns = api.namespace('user',description = '사용자 계정 API')
image_ns = api.namespace('satellite',description = '위성 영상 데이터 API')
#imageNum, userid, keyword, shootingtime, shootingperiod, title, color, font, url
user_parser = reqparse.RequestParser()
imageParser = reqparse.RequestParser()

# 로그인 
@user_ns.route("/api/login")
class user_login(Resource):
    def post(self):
        return "login"
        
# 위성 영상 생성 및 조회 
@image_ns.route("/api/create")
class create_image(Resource):
    def post(self):
        return "Hello world!"


if __name__ == '__main__':
    create_db()
    app.run()