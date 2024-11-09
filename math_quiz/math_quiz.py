import random


def random_integer(min, max):
    """
    Get a random integer between min and max.
    Parameters: 
        min : int, an integer specifying at which position to start.
        max : int, an integer specifying at which position to end.
    Returns: 
        int, a random integer between min and max.
    """
    try:
        # Check if inputs are integers
        if not isinstance(min, int) or not isinstance(max, int):
            raise TypeError("Both min and max must be integers.")
        
        # Ensure min is less than or equal to max
        if min > max:
            raise ValueError("min must be less than or equal to max.")
        
        # Generate random integer
        return random.randint(min, max)
    
    except TypeError as e:
        print(f"Input Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")


def operator_random_choice():
    """
    get a randomly selected element from the specified list
    parameters: 
    returns: str, a randomly selected element from the specified list
    """
    return random.choice(['+', '-', '*'])


def simpl_calculator(num1, num2, operator):
    """
    make a simple operations add, substract and multplication
    parameters: num1 : float, first number
                num2 : float, second number 
                operator: str, the intented operation 
    returns: tuple (operation, result):
                 operation: str,  num1 operator num2
                 result: float, result of operation
    """
    operation = f"{num1} {operator} {num2}"
    if operator== '+': #result = num1 - num2 #bug, operand should be +
                        result = num1 + num2 #add operation
    elif operator== '-': #result = num1 + num2 #bug, operand should be -
                        result = num1 - num2 #substract operation
    else: result = num1 * num2
    return operation , result

def math_quiz():
    """
    make a random operation between two rondom numbers 
    parameters: 
    returns: 
    """
    start = 0
    pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    #for _ in range(pi): # bug, range should be integer
    for _ in range(int(pi)):
        num1 = random_integer(1, 10); #select num1 randomly 
        #num2 = random_integer(1, 5.5); #bug, max sholud be integer 
        num2 = random_integer(1, 5); #select num1 randomly 
        operator = operator_random_choice()#select the operator randomly 

        operation , result = simpl_calculator(num1, num2, operator)# the operation and its result 
        print(f"\nQuestion: {operation}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == result:
            print("Correct! You earned a point.")
            start += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {start}/{pi}")

if __name__ == "__main__":
    math_quiz()
