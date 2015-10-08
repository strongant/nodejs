# _*_coding: UTF-8_*_
from __future__ import  absolute_import
from celery import Celery

#@task(ignore_result=True)，设置没有返回结果
app = Celery('proj',broker='amqp://',backend='amqp://',include=['proj.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600
)
if __name__=='__main__':
    app.start()

