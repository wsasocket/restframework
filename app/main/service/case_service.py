from app.main import db
from app.main.model.caselist import CaseList
from datetime import date
from sqlalchemy import and_
from hashlib import md5
from functools import reduce
# 逻辑可以从简！！！
# 用户能获取自己的case详细信息，默认是未完成的case


def get_personal_case(userId):
    """ 从数据库中获取个人所有开放的case清单"""
    print(type(userId))
    return CaseList.query.filter(
        and_(CaseList.userId == userId, CaseList.caseStatus == 0)).all()


def create_personal_case(userId, case):
    """ 接受提交的数据，在数据库中创建case记录 """
    if len(case['caseHash']) == 0:
        # 新建的case
        m = md5()
        m.update(case['caseTitle'].encode())
        m.update(date.today().strftime(r'%Y-%m-%d').encode())
        case['casehash'] = m.hexdigest()

    newcase = CaseList(userId=userId,
                       memo=case['memo'],
                       caseProject=case['caseProject'],
                       caseFrom=case['caseFrom'],
                       receiveTime=date.today(),
                       expectTime=case['expectTime'],
                       startTime=case['startTime'],
                       completeTime=case['completeTime'],
                       caseTitle=case['caseTitle'],
                       caseDetail=case['caseDetail'],
                       caseHash=case['caseHash'],
                       caseStatus=case['caseStatus'])
    db.session.add(newcase)
    db.session.commit()


def data_validate(userId, case):
    """ 
    输入数据检查，原则如下：
    如果是新建的case，那么caseHash应当为空，如果是继承过来的case，这个值应当是32字节的md5值
    作为新建的case，必须有的字段是 caseTitle caseProject caseDetail caseFrom receiveTime completeTime 
    caseHash 必须为空。
    作为继承的case，必须有 caseDetail （进展） caseHash作为跟踪case的标志 caseFrom，caseTitle，receiveTime不能修改
    startTime 如果继承的case已经有值则也不能修改
    """
    pass


# def _row2dict(row):
#     d = {}
#     for column in row.__table__.columns:
#         d[column.name] = str(getattr(row, column.name))

#     return d


def data_process(context, data):
    """
    Reduce 的数据处理函数，主要是根据数据hash合并相关数据
    """
    if context is None:
        objlist = []
        obj = dict()
        keylist = [
            'caseHash', 'caseTitle', 'caseDetail', 'receiveTime', 'startTime',
            'expectTime', 'completeTime', 'usedTime', 'caseFrom',
            'caseProject', 'caseStatus', 'memo'
        ]
        for k in keylist:
            obj[k] = data[k]
        objlist.append(obj.copy())
        return objlist
    else:
        #检查casehash作为合并的依据
        if 'caseHash' in data.keys():
            for item in context:
                if data['caseHash'] == item['caseHash']:
                    # 发现有相同的case检查后合并
                    # 更新项目截止时间
                    if item['expectTime'] != data['expectTime']:
                        item['expectTime'] = data['expectTime']
                    # 累计工作时间
                    if isinstance(item['usedTime'], str):
                        item['usedTime'] = int(item['usedTime'])
                    item['usedTime'] += int(data['usedTime'])

                    # 累计工作进展
                    if not item['caseDetail'].endswith('\n'):
                        item['caseDetail'] += '\n'
                    item['caseDetail'] += data['caseDetail']
                    # 累计工作备注
                    if len(data['memo']) > 0:
                        item['memo'] += '\n'
                        item['memo'] += data['memo']
                    # 累计状态
                    item['caseStatus'] = data['caseStatus']
                    return context
            else:
                # 新添加的case
                context.append(data.copy())
        return context


def grep_return_data(data):
    """
    filter函数的处理函数，通过返回的False/true决定data中哪类元素被过滤掉
    这个版本的函数是将caseStatus状态为0，就是还未完成的项目返回，其他屏蔽
    """
    return data['caseStatus'] == '0'


def merge_case_Log(userId=1):
    """
    整合相同的case进展，这个版本的函数处理思路是将当前用户所有case记录读取到内存中进行处理
    这样可以避免大量的数据库访问操作。最终将处理好的数据以DTO的格式返回。
    """
    __row2dict = lambda r: {
        c.name: str(getattr(r, c.name))
        for c in r.__table__.columns
    }
    # ret = filter(
    #     grep_return_data,
    #     reduce(
    #         data_process,
    #         map(
    #             __row2dict,
    #             CaseList.query.filter(CaseList.userId == userId).order_by(
    #                 CaseList.id).all()), None))
    # filter 函数只能返回一个可迭代的对象,不是一个列表，不能直接返回！
    # return [i for i in ret]

    return reduce(
        None,
        filter(
            grep_return_data,
            reduce(
                data_process,
                map(
                    __row2dict,
                    CaseList.query.filter(CaseList.userId == userId).order_by(
                        CaseList.id).all()), None)))
