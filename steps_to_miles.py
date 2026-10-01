class NegativeValueError(Exception):
    def __init__(self, message):
        self.message = message

def steps_to_miles(steps):
    try:
        steps = int(steps) 
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered.")
    
    if steps < 0:
        raise NegativeValueError("Exception: Negative Step Count Entered.")
    
    return steps / 2000  

def main():
    try:
        steps = input("Enter the number of steps: ")
        miles = steps_to_miles(steps)
        print(f'{miles:.2f} miles walked.')
    except ValueError as e:
        print(e)
    except NegativeValueError as e:
        print(e.message)

if __name__ == "__main__":
    main()
