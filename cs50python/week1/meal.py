def main():
    time = input("What time is it? ")
    time = convert(time)
    
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")

def convert(time):
        # Change time from the format x:xx to x.xx/60 form (float)
        hour, minute = time.split(":")
        minute = float(minute)
        f_minute = minute/60
        f_hour = float(hour)
        return f_hour + f_minute

if __name__ == "__main__":
    main()

