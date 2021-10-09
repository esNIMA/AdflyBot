from . import adfly_bot
import time
class Run():
    def __init__(self) -> None:
        adbot=adfly_bot.Adbot()
        while True:
       	    url = adbot.get_url()
            proxy_list = adbot.proxyscrap()
            adbot.request_to_url(url, proxy_list)
            time.sleep(10)




		    
		    