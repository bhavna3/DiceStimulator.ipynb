import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        input("Press Enter to roll the dice...")
        dice_results = roll_dice(num_dice)

        print("Rolling", num_dice, "dice...")
        print("Results:", dice_results)

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for using the Dice Rolling Simulator!")

if __name__ == "__main__":
    main()
