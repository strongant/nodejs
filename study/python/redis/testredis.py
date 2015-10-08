# _*_coding: UTF-8_*_

import time
from redis import  Redis
from datetime import datetime

ONLINE_LAST_MINUTES = 5
redis = Redis()


def mark_oneline(user_id):
    now = int(time.time())
