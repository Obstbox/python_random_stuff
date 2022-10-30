# import sys
import subprocess


download_list=[]
protocol="https"
separator=" "
wget_params=['wget', '--no-check-certificate', '-nc', '-P', 'distfiles']


file = open('url_raw_list')
lines = file.readlines()


for line in lines:
    begin_mark = line.find(protocol)
    #assume useless or empty string
    if begin_mark == -1:
        continue
    else:

        url_raw = line[begin_mark:]
        end_mark = url_raw.find(separator)
        url = url_raw[:end_mark]
        download_list.append(url)

for item in download_list:
    wget_params.append(item)
    testrun = subprocess.run(wget_params)

