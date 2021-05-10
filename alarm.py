import time

message = input("Enter the message that u want to show: ")
give_time = input("Enter the time(HH-MM-SS) when u want to see this Message: ")

while True:
    now = time.strftime("%H-%M-%S")
    print(now, end='\r')
    if now == give_time:
        break
    time.sleep(1)

print("Your Message is:")
print(message)
