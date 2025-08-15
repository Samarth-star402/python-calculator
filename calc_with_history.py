def show():
    with open('calc_history.txt', 'r') as file:
        history = file.readlines()
    
    if len(history) == 0:
        print("No history available.")
    else:
        print("Calculation History:")
        for line in reversed(history):
            print(line.strip())


def clear_history():
    
    with open('calc_history.txt', 'w') as file:
        file.write('')
    print("History cleared.")

def add_to_history(expression, result):
    with open('calc_history.txt', 'a') as file:
        file.write(f"{expression} = {str(result)}\n")

def calculate(UserInput):
    parts = UserInput.split()
    if len(parts) < 3 or len(parts) % 2 == 0:
        print("Invalid input format. Please enter in the format: number operator number (e.g., 5 + 3).")
        return None
    
    try:
        result = float(parts[0])
    except ValueError:
        print("Invalid number format. Please enter valid numbers.")
        return None
    for i in range(1, len(parts), 2):
        opreater = parts[i]
        num = float(parts[i + 1])
   
        if opreater == '+':
            result += num
        elif opreater == '-':
            result -= num
        elif opreater == '*':
            result *= num
        elif opreater == '/':
            if num == 0:
                print("Error: Division by zero.")
                return None
            result /= num
        else:
            print(f"Unknown operator: {opreater}. Supported operators are +, -, *, /.")
            return None
        if int(result) == result:
            result = int(result)
        
    add_to_history(UserInput, result)
    print(result) 

def main():
    while True:
        UserInput = input("Enter calculation (or 'history' to view history, 'clear' to clear history, 'exit' to quit): ")
        if UserInput.lower() == 'exit':
            break
        elif UserInput.lower() == 'history':
            show()
        elif UserInput.lower() == 'clear':
            clear_history()
        else:
            result = calculate(UserInput)
            if result is not None:
                print(f"Result: {result}")

main()