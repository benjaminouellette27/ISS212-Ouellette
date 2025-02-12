def main():
    year = int(input("Enter the year to check the patch cycle: "))
    if year < 2019:
        print("Not withing the managed patch period")
    else:
        if year % 4 != 0:
            print("standard year")
        elif year % 100 != 0:
            print("patch year")
        elif year % 400 != 0:
            print("standard year")
        else:
            print("patch year")

main()

# Sources
# Week 3 powerpoint and script examples
