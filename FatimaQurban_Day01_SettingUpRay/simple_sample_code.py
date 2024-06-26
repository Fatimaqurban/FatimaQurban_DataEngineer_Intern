import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    number = 120
    
    start_time = time.time()
    result = factorial(number)
    end_time = time.time()
    
    print(f"Factorial of {number} is {result}")
    print(f"Time taken without Ray: {end_time - start_time} seconds")
