import time
from datetime import date
d = date.today()
print ('Hora:', time.strftime("%I:%M:%S"))
print('DIA:', d.day)
print('MES:', d.month)
print('AÑO:', d.year)