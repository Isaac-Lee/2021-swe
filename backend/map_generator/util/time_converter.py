from datetime import datetime as dt
from datetime import timedelta

def kst2utc(shooting_period=str, shooting_time=str):
    shooting_period = f"{shooting_period[:4]} {shooting_period[4:6]} {shooting_period[6:]}"
    kst = f"{shooting_period} {shooting_time}"
    utc = dt.strptime(kst, '%Y %m %d %H')
    utc += timedelta(hours=-9)
    return utc.strftime("%Y%m%d_%H")

# test 용 코드
if __name__ == '__main__':
    time_str = '2019 04 14 10'
    utc = dt.strptime(time_str, '%Y %m %d %H')
    utc += timedelta(hours=-9)
    print(utc.strftime("%Y%m%d_%H"))