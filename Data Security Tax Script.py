def main():
    data_usage = float(input("Enter your annual data usage in MB: "))
    if data_usage <= 85528:
        tax = (0.18 * data_usage) - 556
    else:
        tax = 14839 + 0.32 * (data_usage - 85528)

    tax = max(tax, 0)
    print(f"Your Data Secuirty Tax is: {round(tax)} MB")

main()

# Sources
# Week 3 Python Script Examples
# Week 3 PowerPoint
