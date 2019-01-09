#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2019/1/7 18:41
author:    peak
description:
"""
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
daoinkpay = Blueprint(
    'daoinkpay',
    __name__,
)

from alipay import AliPay

# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

app_private_key_string = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Vg+9L1lX9dSbyIzOxf6UXs7QpwYt1H3JuCx55+8rzXHDpDj
M184bofk29TSWO4FqRzkusdiR0qK767CcTG/laveUHN1cmrHQiSa7/XxZrf9Bzas
JK9uOBkmuOlvCXHS9ccJ6krEyu4jVEpD8iK10h/t6SZmEZIH3/LYU1E5IWEAkVTH
ajT1tgWrILW1ASGgkK/MHA3Iu1V0HNX400bvO4yAoTD3AkpQ6AKd8gOWO0E1z+ZE
sFLlRxjEayo20k/Oe/eXmJRJl/LSnlPTgr7Yrr/NxRcsRVM1tD2xltMuadgX+VDA
s0jMQlv9hf6Ko8yQ2xkagW15YOgJa7MJtXS0uQIDAQABAoIBAEUqh9pqvRS2WqkX
Pp/2oyDKu2CdnFjtPuBcessRbtDgzrzUSAzQGCAEzCuJnFn/gmVGg5fmimUNjuvz
7JBjpG36FAC2tQYxm1YSLBK+SpzqizIX8TZJs/va631KuwH+1nmX4oHDZFO77HZL
9zkIGNSs8fkHU8/YVLu8S5bzjhGllu9FWbqG++Mmpb8sL0NzCwUwkDai6EEPG+Dp
BOFKIeTSyeWH0xBPfgXIsHd68pwzkUUKplvaJxkfQWsg6OrJztqWgACOLnk5BO1I
DAkgetc2jEU47jOSmSRBeAkXKffTGdg6zOQGwzRKwnHEnFJJxnzZfj8tjodFelaG
EuctggUCgYEA74N4klUdogQdx/8vYoFbM6fnGGSzbJeYni4Rm7m+GQfO8TkQFrtk
y2qCwDX88cDx9FBv3VYMFeyqHrbj++UiGOGppoMyWXuwMRt8byWWbuN/dTTHEkw0
fEe0QK24PPp7yRhIbOz6vAqe4wHbSClicPEEERmJuFuCqyrAKxJ2WS8CgYEA38Ep
e0CdSWJCxUfIwvBNIRw97rvF9f2azGc7L4rtYEIJvPHPCAYTwbNhK8x3dHmrR38n
9FWHk3qoN9eApXQv1HSoBlonZBBlaXSYXFiQg4Yqd81pNUouBsVOsJ4EGcZRF5dt
fm75RGcyLS2eFgyURpdhseWjxbFxH+x1MxuhBpcCgYBSh2SmV3nMd8qjPUTgll4M
oJA6kYhZpKrL5mfe1tOv4EboS5dFnfCPPvYqsO+lhaxZWNYS2DF15ISB7NcF1uA2
3psMayyQNNRzN1tbGQKK1wz2H+dwYJ29LR/pIXLYYB8DHcDm94k1/hrdcahTZx8q
d4HFOp1/zthpjmOE8+mftQKBgHSwhfOTNPPKXMwJrbeMHo0/70SLhKfPBGXJCGK4
7yaeCfoRmUiz8qW36NswnLOPqDV3KN0RpczR0NyedKbUuwTveZkmdxiGPH0Mo1C1
l1ggJhGofE+gSfSZ/Xm6TqUqeav1+tJPCYwUzWQmQCV7lfBijj56Zjh5W2esp0pq
BEYtAoGBAIgX0ZcSysJ2S9t2XIvnsZV7RpDej0cI5kKRmy3KNzjdrEovyd02pMb3
aOZ6+HsaH7LCkTcjuTs+isOCK4pbwNxFZe3vQha6PzwzieN8yr08mqDyxdKagH9Y
wzDb+0f6mKWkZidJzAis9kE166kOrq7rpUheoFPH5UdyP5xZ7r5/
-----END RSA PRIVATE KEY-----
"""

alipay_public_key_string = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy11eta8nq65qR1Gy9H+u
Db9JbBQDzcOEw3/+EihrOwnGZwrVkqJ6GHygu+zmedBdHBx7eQr53hmX3V0BeNJb
Jiq7H/S27jseWBfGIz0GsQoM3I4pKVAQVI8Kui9P8YeccI0HTMN8fr8VMKpwUllT
ZzG8mZdvQN2Y60dVpNjO5qflOWDOYV972L8r57825ziC1PEHWO4NdLMeFLtGQYyW
V2TLpr7iTufBEqT0aeyjJZKThTAzZYlUKtEhiGx0UtDr5L1/TseIYkIwTSJxEpNq
IyPBcxP+ciwHmkhCnPleyvxs41ziPBO01tBC9ND0XCOBENaak20raIPs0dZ8fxZx
2wIDAQAB
-----END PUBLIC KEY-----
"""

alipay = AliPay(
    appid="2018122662657935",
    app_notify_url=None,  # 默认回调url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    # sign_type="RSA",    # RSA 或者 RSA2
    debug=False          # 默认False
)

# 手机网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
order_string = alipay.api_alipay_trade_wap_pay(
    out_trade_no="20161112",
    total_amount=0.01,
    subject="test",
    return_url="https://www.daoink.com/result",
    notify_url="https://example.com/notify" # 可选, 不填则使用默认notify url
)

@Alipay.route('/test', methods=['POST', 'GET'])
def test():
    url = "https://openapi.alipay.com/gateway.do?" + order_string
    return redirect(url)
