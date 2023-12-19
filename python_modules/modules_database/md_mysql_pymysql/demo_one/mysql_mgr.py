#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : fionafan
# @Date     : 2023/12/19 14:15
# @File     : mysql_mgr.py
# @Desc     : mysql管理器

import typing
import pymysql
from dbutils.persistent_db import PersistentDB

# 发生以下异常错误，则重连mysql
from pymysql.constants import CR
_mysql_retry_error = [CR.CR_SERVER_LOST, CR.CR_SERVER_GONE_ERROR]
del CR

_PROGRAM = "VVPyCli"


CONFIG = {
  "database": {
    "mysql": {
      "us_stock_define": {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "dev",
        "password": "xxx*xxx123",
        "database": "finance_stock",
        "__table__": [
          "t_us_stock_define"
        ]
      }
    }
  }
}


def config(filename, *args, default=None):
    """
    获取配置
    """
    cfg = CONFIG.get(filename, {})
    for cfg_name in args:
        if cfg_name is None:
            continue
        cfg = cfg.get(cfg_name, default)
        if not isinstance(cfg, dict):
            return cfg
    return cfg


class BaseMgr(object):
    def __init__(self):
        self._items = dict()

    def add(self, key, value):
        self._items[key] = value

    def remove(self, key):
        self._items.pop(key, None)

    def get(self, key):
        return self._items.get(key)

    def exist(self, key):
        return key in self._items

    def clear(self):
        self._items.clear()

    def keys(self):
        return list(self._items.keys())

    def values(self):
        return list(self._items.values())

    def items(self):
        return list(self._items.items())

    def length(self):
        return len(self.keys())

    def exec_every(self, callback):
        for _, item in self.items():
            rtn = callback(item)
            if rtn is False:
                return False
        return True
    
    
def mysql_retry(max_retry=3):
    """
    mysql断线重连装饰器
    :param max_retry:
    :return:
    """
    def decorator(func):
        import functools, time

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            last_error = None  # 最后执行的异常
            for i in range(0, max_retry+1):
                try:
                    if i > 0:
                        print(f"执行SQL失败:{last_error}, 正在第{i}次重试")
                        time.sleep(1.5)
                        self.connection.ping(reconnect=True)  # 重连
                    return func(self, *args, **kwargs)
                except pymysql.err.Error as ex:
                    last_error = ex
                    if ex.args[0] not in _mysql_retry_error:
                        break
                    pass
            raise last_error

        return wrapper

    return decorator


def cursor_factory(cursorclass):
    class Cursor(cursorclass):
        """
        定制cursor
        """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        @mysql_retry(max_retry=3)
        def execute(self, query, args=None):
            return super().execute(query, args)

        @mysql_retry(max_retry=3)
        def executemany(self, query, args):
            return super().executemany(query, args)

    return Cursor


class Mysql(object):
    """
    Mysql数据库
    """

    def __init__(self, host=None, user=None, password="",
                 database=None, port=3306, charset="utf8mb4",
                 autocommit=True):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._port = port

        # ping检查状态
        self._ping_check = False

        self._conn = pymysql.connect(host=host, user=user, password=password,
                                     database=database, port=port, charset=charset,
                                     autocommit=autocommit, defer_connect=True,
                                     cursorclass=pymysql.cursors.DictCursor, program_name=_PROGRAM)
        self._default_cursor_init()

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def user(self):
        return self._user

    @property
    def database(self):
        return self._database

    @property
    def connection(self):
        """
        底层数据库连接
        :return:
        """
        return self._conn

    def _default_cursor_init(self):
        """
        初始化默认游标
        :return:
        """
        self._cursor = self.cursor()

        self.fetchone = self._cursor.fetchone
        self.fetchmany = self._cursor.fetchmany
        self.fetchall = self._cursor.fetchall
        self.execute = self._cursor.execute
        self.executemany = self._cursor.executemany
        self.mogrify = self._cursor.mogrify

    def connect(self):
        """
        连接数据库
        :return: 成功: True, 失败: False
        """
        try:
            if not self.open:
                self._conn.connect()
                self._ping_check = True
        except:
            print(f"数据库[{self}]连接失败")
            return False
        print(f"数据库[{self}]连接成功")
        return True

    def close(self):
        """
        关闭连接
        :return:
        """
        try:
            self._cursor.close()
            self._conn.close()
        except:
            pass
        finally:
            self._ping_check = False
        print(f"数据库[{self}]连接关闭")

    def cursor(self, cursor=None) -> pymysql.cursors.Cursor:
        """
        新建游标
        :param cursor:
        :return:
        """
        cursorclass = cursor or self._conn.cursorclass
        cursorclass = cursor_factory(cursorclass)
        return self._conn.cursor(cursorclass)

    @property
    def open(self):
        """
        连接是否建立
        :return:
        """
        return self._conn.open and self._ping_check

    def ping(self, reconnect=True):
        try:
            self._conn.ping(reconnect)
            self._ping_check = True
        except Exception as ex:
            self._ping_check = False
            print(f"数据库[{self}]执行PING异常: {ex}")
            return False
        return True

    def __str__(self):
        return f"mysql://{self._user}:***@{self._host}:{self._port}/{self._database}"


class MysqlPool(object):
    def __init__(self, host=None, user=None, password="",
                 database=None, port=3306, charset="utf8mb4",
                 autocommit=True):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._port = port

        self._pool = PersistentDB(pymysql, maxusage=None, setsession=None, failures=None, ping=1,
                                  closeable=True, threadlocal=None,
                                  # 以下参数将传递给pymysql
                                  host=host, user=user, password=password,
                                  database=database, port=port, charset=charset,
                                  autocommit=autocommit, defer_connect=False,
                                  cursorclass=pymysql.cursors.DictCursor, program_name=_PROGRAM)

        self._cursorclass = cursor_factory(pymysql.cursors.DictCursor)

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def user(self):
        return self._user

    @property
    def database(self):
        return self._database

    def close(self):
        pass

    def open(self):
        """
        连接是否建立
        :return:
        """
        return True

    def ping(self, reconnect=True):
        pass

    @property
    def connection(self):
        """
        从连接池中获取一个新的连接的游标
        :return: pymysql.cursor
        """
        return self._pool.connection().cursor(self._cursorclass)


class MysqlMgr(BaseMgr):
    def __init__(self):
        super().__init__()

        self._aio_conn = None

    @property
    def aio_conn(self):
        return self._aio_conn

    def init(self, connect=True):
        all_db = config('database', 'mysql')
        if all_db is None:
            return True
        for name, dbconf in all_db.items():
            valid_conf = {k: v for k, v in dbconf.items() if not k.startswith('_')}
            conn = self.create(name, **valid_conf)
            if not connect or not conn.connect():
                return False
            self.add(name, conn)

            name = f'{name}_pool'
            conn_pool = self.create_pool(name, **valid_conf)
            self.add(name, conn_pool)

        return True

    def create(self, name, host=None, user=None, password="",
               database=None, port=3306, charset="utf8mb4",
               autocommit=True) -> typing.Optional[Mysql]:
        """
        创建Mysql连接
        :param name: 连接名称
        :param host: 主机地址
        :param user: 用户
        :param password: 密码
        :param database: 数据库
        :param port: 端口
        :param charset: 字符集
        :param autocommit: 是否自动提交
        :return: 成功返回连接对象, 失败返回None
        """
        if self.exist(name):
            print(f"名称为{name}的数据库连接已经存在, 请检查参数")
            return None
        conn = Mysql(host=host, user=user, password=password,
                     database=database, port=port, charset=charset,
                     autocommit=autocommit)
        return conn

    def create_pool(self, name, host=None, user=None, password="",
                    database=None, port=3306, charset="utf8mb4",
                    autocommit=True):
        """
        创建mysql连接池
        """
        if self.exist(name):
            print(f"名称为{name}的数据库连接已经存在, 请检查参数")
            return None

        conn = MysqlPool(host=host, user=user, password=password,
                         database=database, port=port, charset=charset,
                         autocommit=autocommit)
        return conn

    def get_conn(self, name) -> typing.Union[Mysql, pymysql.cursors.Cursor]:
        """
        根据名称获取数据库连接
        :param name:
        :return:
        """
        name = f'{name}_pool'
        conn = self.get(name)  # type: typing.Union[Mysql, MysqlPool]

        # 对于前次ping失败的连接, 马上再执行一次ping
        if (conn is not None) and (not conn.open):
            print(f"数据库连接[{conn}]不可用, 尝试重新连接")
            conn.ping(reconnect=True)

        return conn.connection

    def shutdown(self):
        """
        关闭所有数据库连接
        :return:
        """

        def close_conn(conn: Mysql):
            conn.close()

        self.exec_every(close_conn)
        self.clear()

    def keep_alive(self):
        """
        保持心跳
        :return:
        """

        def ping_conn(conn: Mysql):
            conn.ping(reconnect=True)

        self.exec_every(ping_conn)


mysql_mgr = MysqlMgr()


def mysql(name=''):
    """
    获取mysql连接实例
    """
    return mysql_mgr.get_conn(name)


def search_stock_codes():
    """
    查询股票所在行业的股票代码列表
    """
    db = mysql('us_stock_define')
    query_sql = f"select code from t_us_stock_define where industry_code=(SELECT industry_code from t_us_stock_define where code='TSLA.us')"
    db.execute(query_sql)
    data = db.fetchall()
    return data


if __name__ == "__main__":
    mysql_mgr.init()
    search_stock_codes()
