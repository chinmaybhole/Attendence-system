from datetime import timedelta,datetime

ACCESS_EXPIRES=datetime.utcnow()+timedelta(minutes = 15) #8 minutes
REFRESH_EXPIRES=datetime.utcnow()+timedelta(minutes = 20) #24 minutes

class Config:
    JWT_SECRET_KEY='A727F449DA02EDA64FFCA41F9B2DF0A65988139E6EC0387DF305AF42EE634049'
    JWT_ACCESS_TOKEN_EXPIRES=ACCESS_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES=REFRESH_EXPIRES
