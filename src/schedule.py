import schedule
import time
from src.API import atualizar_precos

schedule.every().hour.do(atualizar_precos)

while True:
    schedule.run_pending()
    time.sleep(1)
