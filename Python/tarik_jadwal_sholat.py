#!/bin/python

import json
import subprocess
import time
from datetime import datetime
from datetime import timedelta
#from dateutil.relativedelta import relativedelta

now = datetime.now()
localtime = time.asctime( time.localtime(time.time()) )
current_date = now.strftime("%Y/%m/%d")
tomorrow = datetime.now() + timedelta(days=1)
#d1 = current_date + tomorrow
city_code = "1221"
result = subprocess.run(["curl", f"https://api.myquran.com/v1/sholat/jadwal/{city_code}/{current_date}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result_json = json.loads(result.stdout)

print(result_json["data"]["lokasi"])
print(result_json["data"]["daerah"])
print(f'Hari/Tanggal: {result_json["data"]["jadwal"]["tanggal"]}')
print(f'Waktu Sekarang',localtime)
print(f'- imsak {result_json["data"]["jadwal"]["imsak"]}')
print(f'- subuh {result_json["data"]["jadwal"]["subuh"]}')
print(f'- terbit {result_json["data"]["jadwal"]["terbit"]}')
print(f'- dhuha {result_json["data"]["jadwal"]["dhuha"]}')
print(f'- dzuhur {result_json["data"]["jadwal"]["dzuhur"]}')
print(f'- ashar {result_json["data"]["jadwal"]["ashar"]}')
print(f'- maghrib {result_json["data"]["jadwal"]["maghrib"]}')
print(f'- isya {result_json["data"]["jadwal"]["isya"]}')

result1 = subprocess.run(["curl", f"https://api.myquran.com/v1/sholat/jadwal/{city_code}/{tomorrow}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result_json1 = json.loads(result1.stdout)

print(result_json["data"]["lokasi"])
print(result_json["data"]["daerah"])
print(f'Hari/Tanggal: {result_json["data"]["jadwal"]["tanggal"]}')
print(f'Waktu Sekarang',localtime)
print(f'- imsak {result_json["data"]["jadwal"]["imsak"]}')
print(f'- subuh {result_json["data"]["jadwal"]["subuh"]}')
print(f'- terbit {result_json["data"]["jadwal"]["terbit"]}')
print(f'- dhuha {result_json["data"]["jadwal"]["dhuha"]}')
print(f'- dzuhur {result_json["data"]["jadwal"]["dzuhur"]}')
print(f'- ashar {result_json["data"]["jadwal"]["ashar"]}')
print(f'- maghrib {result_json["data"]["jadwal"]["maghrib"]}')
print(f'- isya {result_json["data"]["jadwal"]["isya"]}')