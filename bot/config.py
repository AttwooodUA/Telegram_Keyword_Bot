import os

BOT_TOKEN = os.getenv("7414576699:AAHP4eU4XQ0GkcwbmuFSFQzYVHyZOpISuBg")

if not BOT_TOKEN:
    raise ValueError("Відсутній токен Telegram бота. Встановіть змінну середовища BOT_TOKEN.")
