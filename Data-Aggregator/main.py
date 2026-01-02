numbers = []

while True:
    try:
        num = input("\nEnter numbers or type 'done' to stop: ").lower()
        
        if num == "done":
            print("All numbers are entered")
            break

        else:
            number = int(num)
            numbers.append(number)
    
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if numbers == []:
    print("\nNo numbers were entered.")

else:
    print(f"\nThe lenght of the list is: {len(numbers)}")
    print(f"The sum of all numbers is: {sum(numbers)}")
    print(f"The average of numbers is: {sum(numbers) / len(numbers)}")
    print(f"The maximum value in numbers is: {max(numbers)}")
    print(f"The minimum value in numbers is: {min(numbers)}\n")
