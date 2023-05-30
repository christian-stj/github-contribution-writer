import datetime
from dateutil.relativedelta import relativedelta

input = "011110010001100000010001101111110110000110000011110110011010001100000010001101100000110000110000110011110011011111100000011111101111100110000110000110011110011010001101100010001101100000110000110000110011110011010001101100010001101100000110000110000110011011110010001100100010001101111110111110111110011110000000000000001000000000000000000000000000000000000"

bitlist = []
counter = 0

# Iterate through bitmap and generate one-dimensional list
for i in range(0,51):
    for j in range(0,7):
        if input[i+j*51] == '1':
            bitlist.append(counter)
        counter += 1
        

yearago = datetime.date.today() - relativedelta(years=1)
yearago_weekday = yearago.weekday() + 1 % 7 
last_sunday_yearago = yearago - relativedelta(days=yearago_weekday)


for number in bitlist:
    print(last_sunday_yearago + relativedelta(days=number))
