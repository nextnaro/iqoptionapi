from datetime import datetime, timedelta
import time


def date_to_timestamp(dt):
    return dt.timestamp()


def get_expiration_time(timestamp, duration):
    now_date = datetime.fromtimestamp(timestamp)
    exp_date = now_date.replace(second=0, microsecond=0) + timedelta(minutes=1)
    if exp_date.timestamp() - timestamp <= 30:
        exp_date += timedelta(minutes=1)
    else:
        exp_date += timedelta(minutes=2)
    
    exp = []
    for _ in range(5):
        exp.append(exp_date.timestamp())
        exp_date += timedelta(minutes=1)
    
    idx = 50
    index = 0
    exp_date = now_date.replace(second=0, microsecond=0)
    while index < idx:
        if int(exp_date.strftime("%M")) % 15 == 0 and exp_date.timestamp() - timestamp > 60 * 5:
            exp.append(exp_date.timestamp())
            index += 1
        exp_date += timedelta(minutes=1)

    remaning = [int(t) - int(time.time()) for t in exp]
    close = [abs(x - 60 * duration) for x in remaning]
    min_close = close.index(min(close))
    
    return int(exp[min_close]), min_close


def get_remaining_time(timestamp):
    now_date = datetime.fromtimestamp(timestamp)
    exp_date = now_date.replace(second=0, microsecond=0) + timedelta(minutes=1)
    if exp_date.timestamp() - timestamp <= 30:
        exp_date += timedelta(minutes=1)
    else:
        exp_date += timedelta(minutes=2)
    
    exp = []
    for _ in range(5):
        exp.append(exp_date.timestamp())
        exp_date += timedelta(minutes=1)
    
    idx = 11
    index = 0
    exp_date = now_date.replace(second=0, microsecond=0)
    while index < idx:
        if int(exp_date.strftime("%M")) % 15 == 0 and exp_date.timestamp() - timestamp > 60 * 5:
            exp.append(exp_date.timestamp())
            index += 1
        exp_date += timedelta(minutes=1)

    remaning = []
    for idx, t in enumerate(exp):
        if idx >= 5:
            dr = 15 * (idx - 4)
        else:
            dr = idx + 1
        remaning.append((dr, int(t) - int(time.time())))

    return remaning
