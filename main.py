from datetime import datetime

going_on_site = 2 # a week

# Get today's date
today_date = datetime.today()

# Convert string to datetime
holdiday_date = datetime.strptime('2026/6/26', "%Y/%m/%d")

days_left = holdiday_date - today_date

weeks_left = days_left / 7

print(f"{days_left.days}","days")

print(f"{weeks_left.days}","weeks")






