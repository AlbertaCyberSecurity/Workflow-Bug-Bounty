
import requests, re, sys, codecs,time
from multiprocessing import Pool
from time import time as timer

global user_agent,helper,directory,ifing,list_targets

def logo():
	banner=(f'''\033
\t #     # ####### #       #    #  ####### #     # #     #
\t #   #  #       #       #   #   #     # ##   ##  #   #
\t  # #   #       #       #  #    #     # # # # #   # #
\t   #    #####   #       ###     #     # #  #  #    #
\t  # #   #       #       #  #    #     # #     #    #
\t #   #  #       #       #   #   #     # #     #    #
\t#     # ####### ####### #    #  ####### #     #    #
\t ##########__Khaled Mohamed__######### GitHub:@xElkomy
\t [Example]: python3 Fuzz-xElkomy.py target.txt DIR if-you-want-check ..!
''')
	print(banner)
	time.sleep(1)
	
logo()

list_targets = sys.argv[1]
directory = sys.argv[2]
ifing = sys.argv[3]
user_agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64).xElkomy AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 '}

try:
    with codecs.open(list_targets, mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))




try:
	if ifing ==None and directory ==None and list_targets ==None:
		logo()
except IOError:
    pass

def get_url(url):
    try:
        wcheck = requests.get(url + directory,headers=user_agent,timeout=3)
        if ifing in wcheck.text:
            print("==>  " + url + directory +"\n  ")
    except:
        pass

def goo():
    try:
        start = timer()
        pp = Pool(30) #Threads
        pr = pp.map(get_url, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except IOError:
        pass


if goo() == 'main':
    goo()
    print('''\t-------------xElkomy-------------
\tBye :(''')
