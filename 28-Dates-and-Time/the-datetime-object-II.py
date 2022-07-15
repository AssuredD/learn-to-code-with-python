from datetime import datetime

today = datetime.today()
print(today.strftime("%m"))
print(today.strftime("%m %d"))
print(today.strftime("%m/%d/%Y"))
print(today.strftime("%Y-%m-%d"))
print(today.strftime("%d-%m-%y"))

print(today.strftime("%A"))
print(today.strftime("%B"))
print(today.strftime("%Y"))
print(today.strftime("%A, %C %B %Y"))
