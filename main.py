from weather_api import by_zipcode
from sms_api import send_message
import schedule

def main():
    weather_stats = by_zipcode()

    weather_stats_list = list(weather_stats)

    send_message(*weather_stats_list)
    return

if __name__ == "__main__":
     main()
#    schedule.every(30).minutes.do(main)

#    while True:
#       schedule.run_pending()

