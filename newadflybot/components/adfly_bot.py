from zipfile import Path
from . import proxy_scrapper
from . import useragent
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.firefox import GeckoDriverManager
import time
import os
class Adbot() : 
    def __init__(self) -> None:
        pass
    def get_url(self):
        url = input(" [URL] ")
        return url
    def request_to_url(self , url ,proxy_list):
        ua = useragent.User_Agent
        os.environ['PATH'] += r"E:\\newadflybot\\components"
        for p in proxy_list:
            proxy_ip_port =p
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = proxy_ip_port
            proxy.ssl_proxy = proxy_ip_port
            capabilities = webdriver.DesiredCapabilities.FIREFOX
            proxy.add_to_capabilities(capabilities)
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", ua)
            driver = webdriver.Firefox(desired_capabilities=capabilities)
            try:
                driver.get(str(url))
                print ("Cheking the site...................")
                print ("Clicking Sevices")
                try:
                    elemen = driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr[1]/td/div/div[1]/span[2]/a")
                    time.sleep(7)
                    elemen.click()
                except:
                    print("clicking failed")
                time.sleep(10)
                driver.quit()
            except:
                print ("There is a problem with your internet connention. Try again later")
                time.sleep(8)
            time.sleep(10)
    def proxyscrap(self): 
        p=proxy_scrapper.ProxyScrapper()
        proxy_list =p.create_proxy_list()
        return proxy_list




    

    
