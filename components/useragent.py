from fake_useragent import UserAgent
class User_Agent():
    def __init__(self) -> None:
        ua= UserAgent()
        random_user_agent = ua.random
        print(ua.random)
        return random_user_agent