FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-venv \
    unzip \
    xvfb

RUN apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.8 python3.8-venv python3.8-dev git

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 \
    && update-alternatives --set python3 /usr/bin/python3.8

RUN python3 -m pip install --upgrade pip

# Chrome 설치
RUN apt-get update && \
    apt-get install -y wget gnupg2 && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Chrome 버전 확인
RUN CHROME_VERSION_FULL=$(google-chrome --version | tr -s ' ' | cut -d ' ' -f 3) && \
    CHROME_VERSION=$(echo $CHROME_VERSION_FULL | cut -d '.' -f 1) && \
    echo "Detected Chrome version: $CHROME_VERSION_FULL" && \
    echo "Chrome major version: $CHROME_VERSION"

# ChromeDriver 버전 확인 및 다운로드
RUN if [ -n "$CHROME_VERSION" ]; then \
        CHROMEDRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
        echo "Detected ChromeDriver version: $CHROMEDRIVER_VERSION" && \
        wget -N "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
        unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
        rm chromedriver_linux64.zip; \
    else \
        echo "Chrome version could not be detected."; \
    fi

RUN python3 -m pip install --upgrade requests urllib3 chardet
RUN python3 -m pip install selenium discord.py webdriver_manager

RUN git clone https://github.com/BonhyeonGu/CrawTest app
WORKDIR /app
COPY ./private.py .
ENTRYPOINT ["tail", "-f", "/dev/null"]
