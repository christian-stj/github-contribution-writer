import datetime, subprocess
from dateutil.relativedelta import relativedelta

input = ""

# Input is string with 51 by 7 zeroes or ones
with open("input", "r") as input_file:
    input = input_file.read().replace("\n", "")

bitlist = []
counter = 0

# Iterate through bitmap and generate list of index of 1-bits
for i in range(0,51):
    for j in range(0,7):
        if input[i+j*51] == '1':
            bitlist.append(counter)
        counter += 1


yearago = datetime.date.today() - relativedelta(years=1)
yearago_weekday = yearago.weekday() + 1 % 7
next_sunday_yearago = yearago - relativedelta(days=yearago_weekday-7)

datelist = [str(next_sunday_yearago + relativedelta(days=number)) for number in bitlist]

subprocess.run(["git", "checkout", "--orphan", "fake-commits"])

for date in datelist:
    for _ in range(0,10):
        subprocess.run(["git", "commit", "--allow-empty", "--date", date, "-m", date])


subprocess.run(["git", "checkout", "main"])
subprocess.run(["git", "merge", "--allow-unrelated-histories", "fake-commits", "-m", "Get fake commits in there"])
subprocess.run(["git", "branch", "-D", "fake-commits"])


