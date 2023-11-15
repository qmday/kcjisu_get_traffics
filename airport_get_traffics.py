import os
import cloudscraper

class User:
    BASE_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }

    def __init__(self, email, password, domain):
        self.email = email
        self.password = password
        self.domain = domain
        self.session = cloudscraper.create_scraper()

    def login(self):
        headers = self.BASE_HEADERS.copy()
        headers["accept-language"] = "zh,zh-CN;q=0.9,en;q=0.8,ja;q=0.7"
        login_url = f"https://{self.domain}/auth/login"
        login_data = {
            "email": self.email,
            "passwd": self.password,
        }
        res = self.session.post(url=login_url, data=login_data, headers=headers)
        print(res.json())
        print(self.domain)
        return res

    def get_traffic(self):
        headers = self.BASE_HEADERS.copy()
        headers["accept-language"] = "en-US,en;q=0.9"
        traffic_url = f"https://{self.domain}/user/checkin"
        res = self.session.post(url=traffic_url, headers=headers, verify=False)
        print(f"get_traffic status: {res}")
        try:
            print(res.json())
        except Exception as e:
            print(f"get_traffic error, text: {res.text}, error: {str(e)}")

def main():
    user = User(
        email=os.environ["EMAIL"],
        password=os.environ["PASSWORD"],
        domain=os.environ["DOMAIN"],
    )
    user.login()
    user.get_traffic()
    print("*****************************")

if __name__ == "__main__":
    main()
