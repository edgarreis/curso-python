import requests
import bs4
import re
from datetime import datetime, time, timedelta
from time import sleep

interval = 10
last_clock = time(hour=2, minute=58, second=0)

while True:

    headers = {
        "user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    url = "https://relogioonline.com.br/horario/"

    req = requests.get(url, headers=headers)

    html = bs4.BeautifulSoup(req.content,'html.parser')

    time_element = html.find(class_ = "colored digit text-nowrap font-digit")

    time_content = time_element.string

    h, m, s = map(int, time_content.split(':'))
    #hour, minutes, seconds = map(lambda value: re.sub(r'[^0-9]', '', value), time_content.split('.'))
    clock = time(hour=h, minute=m, second=s)

    #delta = clock - last_clock

    if clock < last_clock:
        print("Alarme")
    
    last_clock = clock

    print(f"Hour: {h}, Minute: {m}, Second: {s}")
    #print(type(delta))
    #print(delta)
    
    # <div class="btn-text"><p>21/09 -CURITIBA/PR (link em breve)</p><p class="link-text">instagram.com/giovanafagundes</p></div>
    #<span id="lbl-time" class="colored digit text-nowrap font-digit" style="font-size: 102px;">01:19:41</span>

    sleep(interval)