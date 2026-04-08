import os


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://demoqa.com/")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "10000"))