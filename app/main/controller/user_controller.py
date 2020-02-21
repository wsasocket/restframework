from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user
# 在严格限定数据结构（namespace之内的数据结构）减少输出的随意性，也可以方便形成文档


@api.route('/')
class UserList(Resource):
    # api.doc: 增加文档说明
    @api.doc('list_of_registered_users')
    # api.marshal_list_with 当序列化输出结果为列表时使用，单个对象序列化要按照数据模型处理
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """罗列出所有注册的用户"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    # api.expect: 指定输入的数据模型
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
# api.param: 指定必须的参数
@api.param('public_id', 'The User identifier')
# api.response: 指定其中一个响应,相当于override了一个响应
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    # api.marshal_with 指定序列化模型
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user