from datetime import timedelta
ACCESS_EXPIRES=timedelta(minutes = 15) #8 minutes
REFRESH_EXPIRES=timedelta(minutes = 60) #24 minutes

class Config:
    JWT_SECRET_KEY='B536EB890F1ECEBA'
    JWT_ACCESS_TOKEN_EXPIRES=ACCESS_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES=REFRESH_EXPIRES
