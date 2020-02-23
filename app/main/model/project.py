# 用户定义的项目列表
from .. import db
from ..config import ParaEnum


class Project(db.Model):
    """定义所有项目的名称"""
    __tablename__ = 'project'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   nullable=False)
    projectName = db.Column(db.String(128), unique=True, nullable=False)
    projectStatus = db.Column(db.Integer,
                              nullable=False,
                              default=0,
                              comment='Project Process Or Close')
