def main():
    print("=== Saving Helper Program ===")

    while True:
        name = input("Enter name: ")
        grade = input("Enter grade level: ")
        status = input("Enter dormer or cityscholar: ")
        allowance = float(input("Enter allowance per month (₱): ").replace("₱", ""))
        expenses = float(input("Enter expenses per month (₱): ").replace("₱", ""))

        difference = allowance - expenses

        print("\n--- Result for", name, "---")
        if difference > 0:
            print(f"You have ₱{difference:.2f} left of your allowance.")
        elif difference == 0:
            print("You used your exact allowance. No money left, no over budget.")
        else:
            print(f"You are over budget by ₱{abs(difference):.2f}.")

        again = input("\nDo you want to add another student? (yes/no): ").lower()
        if again != "yes":
            break

    print("\nThank you for using Saving Helper!")

main()
