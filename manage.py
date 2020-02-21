# 参考连接
# https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
# pip freeze >requirments.txt
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
#  需要迁移的数据模型
from app.main.model import user
from app.main.model import blacklist
# dev 是在config.py中定义的开发模式的key,系统将使用配置文件中的参数运行
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

# 数据迁移操作
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
# 数据库初始化和整合的命令
# python manage.py db init
# 命令执行完成会增加migrations目录
# python manage.py db migrate --message 'initial database migration'
# 命令执行完成形成生成数据库结构的脚本
# python manage.py db upgrade
# 命令执行完成会生成sqlite的db文件，具体数据库连接/类型在config.py文件中定义
# 如果在开发中需要修改数据库结构只需要执行后两步，如果需要执行init指令需要将db和migrations目录都删除


@manager.command
def run():
    """ 运行程序 """
    # $ python manage.py run
    app.run()


@manager.command
def test():
    """运行单元测试"""
    # $ python manage.py test

    # 将测试脚本以test开头放到test目录中
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
