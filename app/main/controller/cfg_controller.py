from flask import request
from flask_restplus import Resource

from app.main.service.project_service import get_projects_by_id, get_projects_by_status
from app.main.service.project_service import create_project, close_project
from ..util.dto import Configure
from ..config import ParaEnum

api = Configure.api
project = Configure.cfg


@api.route('/')
class ProjectManger(Resource):
    """
    获取项目的清单数据，默认只返回OPEN，除非使用参数id或者status指定
    创建项目只需要提供'name'字段就好
    关闭项目只需要提供'id'字段就好，不是删除
    """
    @api.marshal_list_with(project, envelope='data')
    @api.param('pid',
               description='grep project info by id',
               type='int',
               default=0)
    @api.param('status',
               description='grep project info by status',
               type='string',
               default='undefine')
    def get(self):
        """获取项目的数据 默认只返回OPEN，除非使用参数id或者status指定"""
        pid = request.args.get('id', default=0, type=int)
        status = request.args.get('status', default='undefine', type=str)
        if pid != 0:
            # 按照 id 检索project
            return get_projects_by_id(pid=pid)
        if status != 'undefine':
            # 按照状态检索
            if 'all' in status.lower():
                return get_projects_by_status(status=[1, 0])
            if 'close' in status.lower():
                return get_projects_by_status(status=[1])
            # default return opened project
            return get_projects_by_status(status=[0])
        # 默认状态，返回所有的OPEN的项目
        return get_projects_by_status(status=[0])

    @api.doc('创建项目')
    @api.expect(project, validate=False)
    def post(self):
        # 创建项目
        return create_project(request.json['projectName'])

    # 需要保证交互数据使用DTO验证
    @api.expect(project, validate=False)
    @api.doc('关闭项目')
    def put(self):
        # 关闭项目
        # print(f'Put Command:{request.json}')
        return close_project(request.json['id'])
