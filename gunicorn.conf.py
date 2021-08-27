"""
@project : Poirot
@author  : harumonia
@mail   : zxjlm233@163.com
@ide    : PyCharm
@time   : 2020-12-11 09:34:28
@description: None
"""


# debug = True
# threads = 2
# worker_connections = 1
loglevel = 'info'
bind = "0.0.0.0:5000"
pidfile = '/logs/gunicorn/gunicorn.pid'
accesslog = '/logs/gunicorn/gunicorn_acess.log'
errorlog = '/logs/gunicorn/gunicorn_error.log'
daemon = False

# 启动的进程数
workers = 1
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
