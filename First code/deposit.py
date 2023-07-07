 # The `LINES` import is not used and can be removed
import random

MAXOFLINES = 3
MAXIMABET = 500
MINIMABET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
#This function checks if there are any winning combinations in the slot machine columns.
#  It takes the columns (a list of lists representing the slot machine display), lines (the number of lines to bet on), bet (the bet amount), 
# and values (a dictionary mapping symbols to their corresponding values) as input.
#  It calculates the winnings based on the winning combinations and returns the winnings amount and win_line (a list of line numbers with winning combinations).

def check_the_win(columns, lines, bet, values):
    winnings = 0  # Fix typo: change 'winning' to 'winnings'
    win_line = []  # Initialize an empty list for win lines
    for line in range(lines):
        symbol = columns[0][line]  # Fix typo: change 'symbol[0][line]' to 'columns[0][line]'
        for column in columns:
            symbol_to_check = column[line]  # Fix typo: change 'symboltocheck' to 'symbol_to_check'
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            win_line.append(line + 1)

    return winnings, win_line

#This function generates a random slot machine display. It takes the number of rows and cols as input and symbols (a dictionary mapping symbols to the count of each symbol). 
# It creates a list of lists representing the slot machine columns with randomly selected symbols.

def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  # Use .items() to iterate through the dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  # Rename 'colums' to 'columns'
    
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#This function prints the slot machine display. It takes columns (a list of lists representing the slot machine display) as input and prints the symbols in a grid-like format.

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

#This function prompts the user to enter the initial amount to play with. It validates the input to ensure it is a positive number and returns the validated amount.
def silt():
    while True:
        amount = input('What would be the amount to be silt $ ')
        if amount.isnumeric():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Enter a valid amount $")

    return amount

#This function prompts the user to enter the number of lines they want to bet on. It validates the input to ensure it is within the valid range and returns the validated lines.
def get_the_lines():
    while True:
        lines = input('Enter the lines to bet on (1-' + str(MAXOFLINES) + '): ')
        if lines.isnumeric():
            lines = int(lines)
            if 1 <= lines <= MAXOFLINES:
                break
            else:
                print("Please enter a valid line")
        else:
            print("Enter the number of lines")

    return lines

#This function prompts the user to enter the bet amount for each line. It validates the input to ensure it is within the valid range and returns the validated bet.
def get_the_bet():
    while True:
        amount = input('How much would you like to bet on each line $')
        if amount.isnumeric():
            amount = int(amount)
            if MINIMABET <= amount <= MAXIMABET:
                break
            else:
                print(f"Amount must be between {MINIMABET} - {MAXIMABET}")
        else:
            print("Enter a valid amount $")

    return amount

#This function handles the gambling process for each round. It takes the current amount as input and interacts with the user to determine the bet amount and number of lines to bet on.
#  It calculates the total bet, checks if the amount is sufficient, spins the slot machine, checks for winnings, and returns the net winnings or losses.

def gamble(amount):
    lines = get_the_lines()
    while True:
        bet = get_the_bet()
        total_bet = lines * bet

        if total_bet > amount:
            print(f"You don't have enough balance. Your current balance is: ${amount}")
        else:
            break

    print(f"The betting amount is ${bet} on {lines}. Total betting is equal to {total_bet}")

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, win_line = check_the_win(slots, lines, bet, symbol_value)
    print(f"You won {winning}...........!!!!!")
    print(f"You win in ",*win_line)
    return winning-total_bet

#This function is the main entry point of the program.
#  It initializes the initial amount, repeatedly calls gamble() function until the user decides to quit, and displays the final balance.   

def main():
    amount = silt()
    while True:
        print(f"Current balance is ${amount}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        amount += gamble(amount)

    print(f"You left with ${amount}")
   

main()




