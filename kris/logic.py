import csv
from datetime import datetime

with open('1.csv', encoding='koi8-r') as data_f:
    main_dict = csv.DictReader(data_f, delimiter=';')
    output_list = []
    for i in main_dict:
        output_list.append(i)

switch = 0
compare_first = {}

def sravnenie(nachalo, konec):
    date_format = "%d.%m.%Y %H:%M"
    nachalo_vremya = datetime.strptime(nachalo['event_time'],date_format)
    konec_vremya = datetime.strptime(konec['event_time'],date_format)
    print(f"################\n{nachalo['event_time']}\n{konec['event_time']}")
    print(f"Vzyalo vremeni {konec_vremya - nachalo_vremya}##################")

for empty in output_list:
    if len(empty['uid']) == 0 and switch == 0:
        switch = 1
        compare_first = empty
    elif len(empty['uid'])!=0 and switch == 1:
        sravnenie(compare_first,empty)
        switch = 0
        compare_first = {}

