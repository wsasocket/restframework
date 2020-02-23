from app.main import db
from app.main.model.project import Project
from ..config import ParaEnum
# from sqlalchemy import and_, in_, or_

# 维护项目状态


def get_projects_by_status(*, status=[1, 0]):
    return Project.query.filter(Project.projectStatus.in_(status)).all()


def get_projects_by_id(*, pid=0):
    return Project.query.filter(Project.id == pid).all()


def close_project(id):
    response_object = {
        'status': 'success',
        'message': 'Close Project Status OK'
    }
    try:
        Project.query.filter(Project.id == id).update({'projectStatus': 1})
        # print(p.projectStatus)
        # p.projectStatus = 1
        # db.session.update()
        db.session.commit()
        return response_object
    except Exception as e:
        print(e)
        response_object = {
            'status': 'error',
            'message': 'Close Project Status Fail'
        }
        return response_object


def create_project(name):
    response_object = {'status': 'success', 'message': 'Create New Project OK'}
    try:
        obj = Project(projectName=name, projectStatus=0)
        db.session.add(obj)
        db.session.commit()
        return response_object
    except Exception as e:
        print(e)
        response_object = {
            'status': 'error',
            'message': 'Create New Project Fail'
        }
        return response_object
