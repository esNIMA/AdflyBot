from Proxy_List_Scrapper import ALL, Scrapper, Proxy, ScrapperException
class ProxyScrapper():
    def __init__(self) -> None:
        pass
    def create_proxy_list (self):
        proxy_list=[]
        scrapper = Scrapper(category=ALL, print_err_trace=False)
        data = scrapper.getProxies()
        print("Scrapping Proxies:")
        for item in data.proxies:
            proxy_list.append('{}:{}'.format(item.ip, item.port))
        return proxy_list