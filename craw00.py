import random
import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Craw00():
    def __init__(self, bot):
        self.is_running = False
        self.bot = bot
        self.stack = list()
        self.stack_size = 5
        self.notice_size = 5
        self.patterns = ["그레이", "회색", "그래이", "grey", "mcx", "스피어", "MCX", "레거시"]


    async def run(self, channel_id):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(channel_id)
        while not self.bot.is_closed() and self.is_running:
            if channel:
                res = self.work()
                if res is not None and len(res) > 0:
                    # res 리스트의 각 항목에 대해 메시지 포맷팅 및 전송
                    for item in res:
                        title = item.get("title")
                        href = item.get("href")
                        message = f"제목: {title}\n링크: {href}"
                        await channel.send(message)
            await asyncio.sleep(random.uniform(8.9, 21.3))


    def anyCon(self, target):
        for pattern in self.patterns:
            if pattern in target:
                return True
        return False


    def work(self):
        res = list()
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Headless 모드 활성화
        chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 사용 안 함
        chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 안 함
        chrome_options.add_argument("--disable-gpu")  # GPU 가속 사용 안 함
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get('https://arca.live/b/airsoft2077?category=%EB%8D%94%ED%8C%90%2F%EB%8D%94%EA%B5%AC')
        if len(self.stack) == 0:
            for i in range(self.stack_size):
                title = driver.find_element_by_xpath(f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div[1]/div[1]/span[2]/span[2]").text
                href = driver.find_element_by_xpath(f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]").get_attribute('href')
                if self.anyCon(title):
                    res.append({"title": title, "href": href})
                self.stack.append(title)
        else:
            for i in range(self.stack_size):
                title = driver.find_element_by_xpath(f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div[1]/div[1]/span[2]/span[2]").text
                href = driver.find_element_by_xpath(f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]").get_attribute('href')
                if self.anyCon(title) and title not in self.stack:
                    res.append({"title": title, "href": href})
                self.stack[i] = title

        driver.quit()
        return res