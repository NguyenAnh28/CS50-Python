def main():
    # List 
    month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    # Ask user for input
    

    # Letter form (September 8, 1969)
    while True:
        try:
            date = input("Date: ")
            date = date.replace("/", " ")
            date = date.replace(",", "")
            m, d, y = date.split(" ")
                
            if m in month:
                month_index = month.index(m) + 1
                m = str(month_index).zfill(2)
                d = d.zfill(2)
                final = f"{y}-{m}-{d}"
                break

            elif (int(d) > 0 and int(m) > 0 and int(y) > 0):
                m = m.zfill(2)
                d = d.zfill(2)
                y = y.zfill(4)
                final = f"{y}-{m}-{d}"
                break

        except ValueError:
            print(end="")

    # Print the final product
    print(final)

    

main()