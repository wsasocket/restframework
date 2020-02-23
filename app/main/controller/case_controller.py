from flask import request
from flask_restplus import Resource
from flask_restplus import reqparse
from flask import json
from ..util.dto import Case
from ..util.decorator import token_required
from ..service.auth_helper import Auth
from ..service.case_service import get_personal_case, create_personal_case, merge_case_Log

api = Case.api
_case = Case.case
_casehash = Case.casehash


@api.route('/list')
class CaseListAll(Resource):
    @api.marshal_list_with(_case, envelope='case')
    # @token_required
    @api.param('page',
               description='current record page',
               type='int',
               default=0)
    @api.param('count', description='count per page', type='int', default=10)
    def get(self):
        page = request.args.get('page', default=0, type=int)
        count = request.args.get('count', default=10, type=int)
        """获取用户的case所有列表，用户信息在头部的jwt信息中获取"""
        return get_personal_case(1)


@api.route('/')
class CaseOperate(Resource):
    @api.marshal_list_with(_case, envelope='case')
    # @token_required
    def get(self):
        """获取用户的case未完成列表，用户信息在头部的jwt信息中获取"""
        obj, _ = Auth.get_logged_in_user(request)
        # return get_personal_case(obj['data']['user_id'])
        return merge_case_Log(1)

    @api.expect(_case, validate=True)
    def post(self):
        """创建一个新的case"""
        obj, _ = Auth.get_logged_in_user(request)
        # userId = obj['data']['user_id']
        userId = 1
        return create_personal_case(userId, request.json)

    # @api.expect(_case, validate=True)
    # def put(self):
    #     """更新一个的case"""
    #     pass


# @api.route('/hash')
# class CaseListByHash(Resource):
#     @api.marshal_list_with(_case, envelope='case')
#     @api.expect(_casehash, validate=True)
#     def post(self):
#         """根据case的hash获取case列表,!!!测试用!!!"""
#         pass