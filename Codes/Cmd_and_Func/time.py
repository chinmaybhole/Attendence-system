import time
from datetime import datetime

#"2021-12-26 12:50:28"

# Strip the time data
# Find the timin and timeout difference


def time_decode(data):
    # data should be "2021-12-26 12:50:28"
    date,timin =data.split(" ")
    timin = datetime.strptime(f"{timin}","%H:%M:%S")
    return timin

def time_diff(tin,tout):
    if tout - tout :
        pass
    pass
def str2int(tim):
    li = map(int,tim.split(":"))   
    return list(li)
a = "2021-12-26 12:50:28"
date,timin =a.split(" ")
b = "2021-12-26 12:58:40"
date2,timout =b.split(" ")
print(type(timin))
timin = datetime.strptime(f"{timin}","%H:%M:%S")
timout = datetime.strptime(f"{timout}","%H:%M:%S")
# print(timout - timin)
# # split time with ':' then convert the str to int
# timin = str2int(timin)
tin = time_decode(a)
tout = time_decode(b)
print(type(tout - tin))
## Calculate time difference

# print(timin)
