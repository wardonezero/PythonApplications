from typing import Callable
import random
import time

#Create a generator function generate_orders() that yields 50 simulated orders:
status = ("pending", "processing", "shipped", "cancelled")

def generateOrders():
    order_id = 1
    while order_id <= 50:
        yield {
            "order_id": order_id,
            "customer": random.randint(1000, 2000),
            "amount": f"${round(random.uniform(10.0, 1000.0), 2)}",
            "status": f'{random.choice(status)}'
        }
        order_id += 1

#Create a decorator @validate_order that wraps the generator:
def validateOrders(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    def wrapper(*args, **kwargs):
        invalidCount = 0
        validCount = 0
        with open("invalid_orders.txt", "a") as file:
            for order in function(*args, **kwargs):
                if float(order['amount']) < 0.0 or order['status'] not in status:
                    invalidCount += 1
                    file.write(order + "\n")
                    continue
                validCount += 1
                yield order
        file.close()

    return wrapper

# This decorator will be used before your function runs.
#It should decode the input arguments passed to the function. For example, if the input is a Base64-encoded string or bytes, decode it to get the original content before passing it to the function.
def decode_input(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    def wrapper(*args, **kwargs):
        decoded_args = [arg.decode('utf-8') if isinstance(arg, bytes, str) else arg for arg in args]
        return function(*decoded_args, **kwargs)

    return wrapper

#This decorator should take the output of the function and encode it (for example, using Base64 or any encoding method).
#It should return the encoded result instead of the plain output.
def encode_output(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        encoded_result = result.encode('utf-8') if isinstance(result, str) else result
        return encoded_result

    return wrapper

#This decorator should:
# Automatically log the decoded input, the encoded output, and the execution time of the function.(that is, when was it done)
def log_execution(function: Callable):
    if not callable(function):
        raise TypeError(f"{type(function)} is not callable")

    def wrapper(*args, **kwargs):
        start_time = time.time()
        #what to do ?
        end_time = time.time()
        execution_time = end_time - start_time

        with open("execution_log.txt", "a") as log_file:
            log_file.write("Decoded Input: {}, Encoded Output: {}, Execution Time: {execution_time:.8f} seconds\n")
            log_file.close()
        return 

    return wrapper

#Boolean expression truth table generator
#TODO
    

