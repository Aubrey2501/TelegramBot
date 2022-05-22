import re

all_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_nums = re.findall(r'\b\w{0}[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]\d{3}\w{1}[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]\d{2,3}', all_numbers)
print('Список номеров частных автомобилей:', private_nums)

taxi_nums = re.findall(r'\b\w{1}[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]\d{5,6}', all_numbers)
print('Список номеров такси:', taxi_nums)