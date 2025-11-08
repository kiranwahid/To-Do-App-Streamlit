import time

# 🎉 Ask the user for countdown time in seconds
countdown_time = int(input("⏳ Enter the countdown time in seconds: "))

# 🕰 Start the countdown
while countdown_time > 0:
    minutes, seconds = divmod(countdown_time, 60)
    time_format = '{:02d}:{:02d}'.format(minutes, seconds)
    
    # Display the current countdown time ⏱
    print(f"⏳ {time_format} remaining")
    
    # Decrease the countdown time by 1 second
    countdown_time -= 1
    
    # Pause for 1 second to simulate countdown ⌛
    time.sleep(1)

# 🎊 Time's up!
print('\n ⏱ Time is over!')
