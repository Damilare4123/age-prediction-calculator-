from datetime import datetime
now = datetime.now()
print("📅Date and Time Information")
print(f"\n\n----------------------------")
print(f"Today is: {now.strftime('%A, %d %B %Y')}")
print(f"Current Time is: {now.strftime('%H:%M:%S:%p')}")
