# Integer 整型
# String 字符串
# Text 文本
# DateTime 日期
# Float 浮点型
# Boolean 布尔值
# PickleType 存储一个序列化（ Pickle ）后的Python对象
# LargeBinary 巨长度二进制数据

# 原生sql语句操作
# sql = 'select * from user'
# result = db.session.execute(sql)

# # 查询全部
# User.query.all()
# # 主键查询
# User.query.get(1)
# # 条件查询
# User.query.filter_by(User.username='name')
# # 多条件查询
# from sqlalchemy import and_
# User.query.filter_by(and_(User.username == 'name', User.password == 'passwd'))
# # 比较查询
# User.query.filter(User.id.__lt__(5))  # 小于5
# User.query.filter(User.id.__le__(5))  # 小于等于5
# User.query.filter(User.id.__gt__(5))  # 大于5
# User.query.filter(User.id.__ge__(5))  # 大于等于5
# # in查询
# User.query.filter(User.username.in_('A', 'B', 'C', 'D'))
# # 排序
# User.query.order_by('age')  # 按年龄排序，默认升序，在前面加-号为降序'-age'
# # 限制查询
# User.query.filter(age=18).offset(2).limit(3)  # 跳过二条开始查询，限制输出3条

# # 增加
# use = User(id, username, password)
# db.session.add(use)
# db.session.commit()

# # 删除
# User.query.filter_by(User.username='name').delete()

# # 修改
# User.query.filter_by(User.username='name').update({'password': 'newdata'})

# 查询制定的id列
# result = RiskDataModel.query.with_entities(RiskDataModel.id)  # 返回BaseQuery

# 返回指定的两列
# result = RiskDataModel.query.with_entities(RiskDataModel.id, RiskDataModel.name)

# 并且去重
# result  = RiskDataModel.query.with_entities(RiskDataModel.store_st_id).distinct().all()
