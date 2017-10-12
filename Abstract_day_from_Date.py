
import datetime
import calendar


def getDate(date):
    datetime_object = datetime.datetime.strptime("02/03/2017", "%d/%m/%Y")
    print str(calendar.day_name[datetime_object.weekday()])[0:3]+" "+str(date)
