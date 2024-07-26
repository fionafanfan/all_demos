#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/31 14:49
# @File     : parse_param.py
# @Desc     :
import requests


def req_login():
    url = 'http://trade.firstsechk.com/i-trade/streaming/streamLogin'
    data = 're=1&clm=P678%2FfO7GPWmD%2FwpeYdAePFQNoMhC031pTbUsuXSEGpbPZSYvNhvYEdVY2VfDP0quPOH%2BbXZr2Kp%0AuMXd6s38xyrasInrP2EQaoOyp7LRoJRNbpBNg4AoMzQQ70Hfv1YAMkrqOqx4KOOQp0tcienXQf7s%0AcgB26zKfry5wqOWVW5tjGtstaNlIMfejJUGfpo%2FBlqXzLDIYMFT%2BhWCdZZ7L%2FsQA7QySw%2BOzAtgm%0AwfsQE5nRS8QDkiZPYc4eWDz1Rp2909Rtrcg%2B243ZPrj9mIQS%2FKCayyF6E4Oko%2FlBNfmQSai7sQva%0A4FJMFbj3OnYyEYrYyEJhffgQPbSWs2GsMMfsi0lrTB%2FqyM%2F97o8DznRKRp4W1664wAoeuotkqKvE%0Alj3FWv%2F2mdnLrliLBk343rsrn%2F%2BNkU2Sett0gAWV8r0Fpu9E88l8RU7PX7AR3Dg5%2B5%2BBBvDOmB%2FA%0ARTKxbinjVuLGMwYa5v1%2BJNBj91pPjoYStxwGs%2B3E%2BcIhm4fWYMdRQC8xo62DT0F1wkXjm2zgasZy%0AlMWrIb3iUCOhfq0H81dqQQLWP%2FkAbQpOVY%2FGhfhGIfrBImY76JET6TwbkKr9Dw18sVdWCz8KKNJe%0AmcXj%2F%2BXfdSGAJDmvq%2BZKRe8p6S4XQw4kBvXUOG3zu6%2FRgnfPektpVxfpFRsPzO2AH3dUIQv9jVs%3D%0A'
    r = requests.post(url, data=data)
    print(r.status_code, r.content)


req_login()
