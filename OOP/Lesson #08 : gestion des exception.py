# try | raise | except | errornames(ValueError,InsufficientFundsError,TypeError,Exception,ZeroDivisionError)

x=40
y=20

try:
    result = x / y
    raise print("Division performed not successfully.") # This line will only run if no exception is raised
        
except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
            
except TypeError:
        print("Error: Invalid input types. Please provide numbers.")
            
except Exception as e: # Catch any other exception
        print(f"An unexpected error occurred : {e}")
            
else: # This block will execute if no exception is raised in the try block
        print("No exceptions occurred during division.")

finally: # This block always executes, regardless of exceptions
        print("This block always executes.")

# return result
