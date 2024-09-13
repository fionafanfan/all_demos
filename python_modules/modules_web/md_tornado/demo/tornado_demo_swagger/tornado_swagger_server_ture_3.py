import json
import logging
import datetime
import traceback

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado_swagger.setup import setup_swagger
from tornado_swagger.model import register_swagger_model
from tornado_swagger.parameter import register_swagger_parameter


# 定义你的处理程序
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


@register_swagger_model
class ExampleModel:
    """
    ---
    type: object
    description: 示例模型
    properties:
        id:
            type: integer
            format: int64
        name:
            type: string
    """


class BaseHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.write("None")

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 允许跨域访问
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Content-Type", "text/plain; charset=UTF-8")
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")

    def options(self):
        self.set_status(204)
        self.finish()

    @property
    def args_parse(self):
        print("--------------baseHandler args_parse begin--------------")
        _ip = self.request.headers.get('X-Forwarded-For') or self.request.headers.get(
            'X-Real-IP') or self.request.remote_ip
        args_data = {}

        body_data = self.request.body
        print("---base-handler-body_data:{}".format(body_data))
        if isinstance(body_data, bytes):
            body_data = self.request.body.decode('utf8', errors='ignore')
        try:
            args_data = json.loads(body_data)
        except Exception as e:
            print(f"当成json格式解析出错:{e}", exc_info=True)

        for name, values in self.request.arguments.items():
            if not values:
                continue
            else:
                args_data[name] = values[0].decode('utf8').strip()

        if not args_data and body_data:
            if isinstance(body_data, bytes):
                body_data = self.request.body.decode('utf8')
            args_data = tornado.escape.json_decode(body_data)

        args_data['ip'] = _ip

        print("传入参数: {}".format(args_data))
        return args_data


class CreateUserHandler(BaseHandler):
    def post(self):
        """
        ---
        tags:
        - Users
        summary: 创建一个新用户
        description: 使用提供的详细信息创建一个新用户
        parameters:
        - in: body
          name: body
          description: 用户的详细信息
          required: true
          schema:
            $ref: '#/definitions/CreateUserRequest'
        responses:
            201:
                description: 用户成功创建
                schema:
                    $ref: '#/definitions/UserResponse'
            400:
                description: 请求参数错误
                schema:
                    type: object
                    properties:
                        error:
                            type: string
                            example: Invalid input data
        """
        try:
            # 假设我们从请求体中提取了用户数据
            user_data = tornado.escape.json_decode(self.request.body)
            user_id = 123  # 假设创建了用户并返回一个用户ID
            self.set_status(201)
            self.write({"id": user_id, "name": user_data["name"], "email": user_data["email"]})
        except Exception as e:
            self.set_status(400)
            self.write({"error": str(e)})


@register_swagger_model
class CreateUserRequest:
    """
    ---
    type: object
    required:
    - name
    - email
    - password
    properties:
        name:
            type: string
            description: 用户的名称
        email:
            type: string
            format: email
            description: 用户的电子邮件地址
        password:
            type: string
            format: password
            description: 用户的密码
    """

@register_swagger_model
class UserResponse:
    """
    ---
    type: object
    properties:
        id:
            type: integer
            description: 用户ID
        name:
            type: string
            description: 用户的名称
        email:
            type: string
            description: 用户的电子邮件地址
    """


class StockShapeIndicatorHandler(BaseHandler):
    async def get(self):
        await self.post()

    async def post(self):
        """
        ---
        tags:
        - 业务测试
        summary: 行情指标/形态指标查询接口
        description: 输入股票id（正股、停牌、退市的股票）、日期时间（格式：2024/8/20 00:00:00)、K线类型，得到该股票的形态指标
        parameters:
        - in: body
          name: body
          description: 输入
          required: true
          schema:
            $ref: '#/definitions/CreateStockShapeIndicatorRequest'
        responses:
            200:
                description: 响应结果-成功
                schema:
                    $ref: '#/definitions/StockShapeIndicatorResponse'
            0:
                description: 响应结果-失败
                schema:
                    $ref: '#/definitions/StockShapeIndicatorResponse'
        :return:
        """
        data = {"shape": [], "indicator": []}
        msg = '请求成功'
        code = 200
        try:
            args = self.args_parse
            print('\n*********************接收參數*************************:{}'.format(args))

            market = args.get("market", "")  # 必填
            ktype = args.get("kType", "")  # 必填
            ts = args.get("time", 0)  # 必填
            stock_code = args.get("stockCode", "")  # 选填，字段保留，但先不用
            stock_id = args.get("stockId", "")

            # assert all([market, ts, ktype, stock_id]), "market、time、kType、stockId这些是必填参数"
            tiem_cur = int(datetime.datetime.now().timestamp())
            stock = stock_id  # 让stock等于stock_id
            if ts > tiem_cur:
                shape, indicator = [], []
            else:
                shape, indicator = self.run(market, ktype, stock, ts)
            data['shape'], data['indicator'] = shape, indicator

        except Exception as e:
            msg = '请求出错，错误详情:{}'.format(e)
            print("错误追踪详情： {}".format(traceback.print_exc()))
            code = 0
        finally:
            self.set_status(code)
            ret = json.dumps({"code": code, "msg": msg, "data": data}, ensure_ascii=False)
            print(f"返回数据:{ret}")
            self.write(ret)

    def run(self, market, ktype, stock, ts):
        shape = ["黑三兵", "三金叉"]
        indicator = ["MA空头排列", "KDJ低位金叉"]
        return shape, indicator


@register_swagger_model
class CreateStockShapeIndicatorRequest(BaseHandler):
    """
    ---
    type: object
    required:
    - market
    - kType
    - ts
    - stock_id
    properties:
        market:
            type: string
            description: 市场
        kType:
            type: string
            format: kType
            description: k线类型
        ts:
            type: string
            format: ts
            description: 日期时间
        stock_id:
            type: integer
            format: stock_id
            description: 股票id
    """

@register_swagger_model
class StockShapeIndicatorResponse(BaseHandler):
    """
    ---
    type: object
    properties:
        code:
            type: integer
            description: 响应码
        msg:
            type: string
            description: 响应文本提示
        data:
            $ref: '#/definitions/StockShapeIndicatorDataResponse'
            description: 响应数据
    """

@register_swagger_model
class StockShapeIndicatorDataResponse(BaseHandler):
    """
    ---
    type: object
    properties:
        shape:
            type: array
            description: 出现的形态列表

        indicator:
            type: array
            description: 出现的指标类型列表
    """

# 定义路由
routes = [
    tornado.web.url(r"/", MainHandler),
    tornado.web.url(r"/getStockShapeIndicator", StockShapeIndicatorHandler),
    # tornado.web.url(r"/users", CreateUserHandler),
]


# 应用程序类
class Application(tornado.web.Application):
    def __init__(self):
        setup_swagger(routes,
                      swagger_url="/api/doc",
                      api_base_url="/",
                      description="Swagger API definition",
                      api_version="1.0.0",
                      title="Example API",
                      contact="example@example.com",
                      schemes=["http", "https"])
        super(Application, self).__init__(routes, debug=True)


# 启动应用程序
if __name__ == "__main__":
    app = Application()
    PORT = 8888
    app.listen(PORT)
    print(f'server is running {PORT}')
    tornado.ioloop.IOLoop.current().start()
