# app/__init__.py

from flask_restplus import Api
from flask import Blueprint
# 下面两个是 namespace
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)
# 创建蓝图
api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )
# 注册蓝图
# path指定url的前缀，如果不注明，就使用namespace的名称作为前缀
api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)