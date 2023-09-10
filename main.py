import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if symbol != column[line]:
                break
        else:
            winning += values[symbol]*bet
            winning_lines.append(line+1)
    
    return winning, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i !=len(columns) - 1:
                print(column[row], end="|")
            else: print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("Please enter a positive number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How many lines would you like to bet on? [1-{MAX_LINES}] ")
        if lines.isdigit():
            lines = int(lines)
            if lines in range (1,MAX_LINES+1):
                break
            else:
                print(f"Amount must be between 1 and {MAX_LINES}")
        else:
            print(f"Please enter a positive number in range [1-{MAX_LINES}].")

    return lines


def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each line? [{MIN_BET}-{MAX_BET}] ")
        if bet.isdigit():
            bet = int(bet)
            if bet in range (MIN_BET,MAX_BET+1):
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print(f"Please enter a positive number in range [{MIN_BET}-{MAX_LINES}].")

    return bet


def spin(balance):
    number_of_lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*number_of_lines

        if total_bet <= balance:
            break

        print(f"You bet exceeds your balance. Your current balance is {balance}")

    print(f"You are betting {bet}$ on {number_of_lines} lines. Total bet is equal to: {number_of_lines * bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, number_of_lines, bet, symbol_value)
    print(f"You won {winnings}$.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: {balance}$")
        answer = input("Press Enter to spin (q to quit, e to deposit). ")
        if answer == "q": break
        if answer == "e": balance += deposit()
        balance += spin(balance)    
    print(f"You're left with {balance}$")

if __name__ == "__main__":
    main()