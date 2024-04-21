import random
import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Craw00():
    def __init__(self, bot):
        self.is_running = False
        self.bot = bot
        self.delayRange = [60.7, 120.9]
        self.notice_size = 5
        self.waitTime = 600
        self.patternAnti00 = ["더구", "ㄷㄱ"]
        self.patterns00 = ["그레이", "회색", "그래이", "grey", "evo", "EVO"]
        self.lastID00 = ''
        self.lastID01 = ''
        self.lastID02 = ''


    async def run(self, channel_id):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(channel_id)
        while not self.bot.is_closed() and self.is_running:
            if channel:
                res = self.work00()
                if res is not None and len(res) > 0:
                    # res 리스트의 각 항목에 대해 메시지 포맷팅 및 전송
                    for item in res:
                        title = item.get("title")
                        href = item.get("href")
                        message = f"제목: {title}\n링크: {href}"
                        await channel.send(message)
            await asyncio.sleep(random.uniform(self.delayRange[0], self.delayRange[1]))
            if channel:
                res = self.work01()
                if res is not None and len(res) > 0:
                    # res 리스트의 각 항목에 대해 메시지 포맷팅 및 전송
                    for item in res:
                        title = item.get("title")
                        href = item.get("href")
                        message = f"제목: {title}\n링크: {href}"
                        await channel.send(message)
            await asyncio.sleep(random.uniform(self.delayRange[0], self.delayRange[1]))
            if channel:
                res = self.work02()
                if res is not None and len(res) > 0:
                    # res 리스트의 각 항목에 대해 메시지 포맷팅 및 전송
                    for item in res:
                        title = item.get("title")
                        href = item.get("href")
                        message = f"제목: {title}\n링크: {href}"
                        await channel.send(message)
            await asyncio.sleep(random.uniform(self.delayRange[0], self.delayRange[1]))


    def anyCon(self, patterns, target):
        for pattern in patterns:
            if pattern in target:
                return True
        return False
    
    def noneCon(self, patterns, target):
        for pattern in patterns:
            if pattern in target:
                return False
        return True

    def work00(self):
        res = list()
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Headless 모드 활성화
        chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 사용 안 함
        chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 안 함
        chrome_options.add_argument("--disable-gpu")  # GPU 가속 사용 안 함
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get('https://arca.live/b/airsoft2077?category=%EB%8D%94%ED%8C%90%2F%EB%8D%94%EA%B5%AC')
        i = 0
        try:
            # 요소가 로드될 때까지 최대 10초간 대기
            element = WebDriverWait(driver, self.waitTime).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div[1]/div[1]/span[2]/span[2]"))
            )
            title = element.text
            href = driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]").get_attribute('href')
            pid = driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div/div[1]/span[1]/span").text
            if self.anyCon(self.patterns00, title) and pid != self.lastID00 and self.noneCon(self.patternAnti00, title):
                res.append({"title": title, "href": href})
                self.lastID00 = pid
        except NoSuchElementException:
            print("Element not found.")
        except TimeoutException:
            print("Loading took too much time.")
        finally:
            driver.quit()
        return res
    

    def work01(self):
        res = list()
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Headless 모드 활성화
        chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 사용 안 함
        chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 안 함
        chrome_options.add_argument("--disable-gpu")  # GPU 가속 사용 안 함
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get('https://arca.live/b/airsoft2077?category=%EB%8D%94%ED%8C%90%2F%EB%8D%94%EA%B5%AC&target=all&keyword=d-evo')
        i = 0
        try:
            # 요소가 로드될 때까지 최대 10초간 대기
            element = WebDriverWait(driver, self.waitTime).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div[1]/div[1]/span[2]/span[2]"))
            )
            title = element.text
            href = driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]").get_attribute('href')
            pid = driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div/div[1]/span[1]/span").text
            if self.lastID01 != '' and pid != self.lastID01 and self.noneCon(self.patternAnti00, title):
                res.append({"title": title, "href": href})
            self.lastID01 = pid
        except NoSuchElementException:
            print("Element not found.")
        except TimeoutException:
            print("Loading took too much time.")
        finally:
            driver.quit()
        return res
    

    def work02(self):
        res = list()
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Headless 모드 활성화
        chrome_options.add_argument("--no-sandbox")  # Sandbox 프로세스 사용 안 함
        chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 안 함
        chrome_options.add_argument("--disable-gpu")  # GPU 가속 사용 안 함
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get('https://arca.live/b/airsoft2077?category=%EB%8D%94%ED%8C%90%2F%EB%8D%94%EA%B5%AC&target=all&keyword=%EC%9C%A0%EB%8B%88%ED%8B%B0')
        i = 0
        try:
            # 요소가 로드될 때까지 최대 10초간 대기
            element = WebDriverWait(driver, self.waitTime).until(
                EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div[1]/div[1]/span[2]/span[2]"))
            )
            title = element.text
            href = driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]").get_attribute('href')
            pid = driver.find_element(By.XPATH, f"/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{self.notice_size + 1 + i}]/div/div[1]/span[1]/span").text
            if self.lastID02 != '' and pid != self.lastID02 and self.noneCon(self.patternAnti00, title):
                res.append({"title": title, "href": href})
            self.lastID02 = pid
        except NoSuchElementException:
            print("Element not found.")
        except TimeoutException:
            print("Loading took too much time.")
        finally:
            driver.quit()
        return res
    