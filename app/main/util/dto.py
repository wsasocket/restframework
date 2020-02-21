# data transfer object

from flask_restplus import Namespace, fields

# 下面定义的数据结构用于接口数据交换使用，与数据库模型不完全一样
# 由于数据名称可能存在重复的问题，这里需要设置namespace
class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model(
        'user', {
            'email': fields.String(required=True,
                                   description='user email address'),
            'username': fields.String(required=True,
                                      description='user username'),
            'password': fields.String(required=True,
                                      description='user password'),
            'public_id': fields.String(description='user Identifier')
        })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model(
        'auth_details', {
            'email':
            fields.String(required=True, description='The email address'),
            'password':
            fields.String(required=True, description='The user password '),
        })
