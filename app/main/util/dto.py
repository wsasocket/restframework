# data transfer object

from flask_restplus import Namespace, fields


# 下面定义的数据结构用于接口数据交换使用，与数据库模型不完全一样
# 不完全一样是指数量上可能不一致，主要是根据交互的字段有关
# 名字不一样会在序列化时出问题
# 由于数据名称可能存在重复的问题，这里需要设置namespace
# class 名作为分组标志
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


class Configure:
    api = Namespace('configure',
                    description='Get Or Set Project Config Parameter')
    cfg = api.model(
        'project',
        {
            'projectName': fields.String(
                description='Project Name'),  # can use enum=[] parameter
            'projectStatus': fields.Integer(
                description='Project Status'),  # can use max min parameter
            'id': fields.Integer(description='Project Id')
        })


class Case:
    api = Namespace('case manager',
                    description='Operate case DB data interface')
    casehash = api.model('casehash', {'hash': fields.List(fields.String)})
    case = api.model(
        'case', {
            'caseHash': fields.String(description='current case hash value'),
            'caseTitle': fields.String(description='case title'),
            'caseDetail': fields.String(description='case detail more text'),
            'receiveTime': fields.Date(description='case received Time'),
            'startTime': fields.String(description='case start Time'),
            'expectTime': fields.String(description='case expect Time'),
            'completeTime': fields.String(description='case complete Time'),
            'caseFrom': fields.String(description='who order this case '),
            'usedTime': fields.Integer(),
            'caseProject': fields.String(),
            'caseStatus': fields.Integer(),
            'memo': fields.String(),
            'userId': fields.Integer(description='user Id')
        })