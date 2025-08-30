def divide_numbers(a, b):
    try:
        
        result = a / b
    except ZeroDivisionError as e:
       
        print(e)
       
        raise
    except TypeError as e:
        
        print(e)
    else:
       
        print(f"The result of {a} divided by {b} is {result}")
    finally:
       
        print("Execution completed.")

# Test cases
try:
    divide_numbers(10, 2)
    divide_numbers(10, 'a') 
    divide_numbers(10, 0) 
     
except (ZeroDivisionError):
    print("Handled the ZeroDivisionError or TypeError raised from the function.")
