n = int(input('Введите количество секунд: '))
hours = n//3600
minutes = (n-hours*3600)//60
seconds = n-((n//60)*60)
print(hours, minutes, seconds)