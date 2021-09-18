import test
import time
import datetime
vali, valf = test.times()

date = datetime.date(1, 1, 1)

vi = datetime.datetime.combine(date, vali)
vf = datetime.datetime.combine(date, valf)
result = vf - vi

fresult = int(result.total_seconds())
print('\n', fresult)

def factor_cal():
    raw = test.count()
    carpsec = raw/fresult
    return carpsec



