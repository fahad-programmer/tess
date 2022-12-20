import random

def greet_main():
    options = ["hi", "hello! sir", "hey there!", "hi, good to have u back"]
    return(random.choice(options))

def saying_bye_main():
    options = ["bye", "see you soon take care!", "sad to say u bye hope to see u soon!", "bye take care", "will be waiting"]
    return(random.choice(options))

def saying_thanks_main():
    options = ["Mine Pleasure!", "Always at your service", "Always there for you.", "Mention Not!"]
    return (random.choice(options))

def assistant_name():
    options = ["you can call me tess!", "Tess is my name", "Really! you don't know my name", "Tess! here on your service"]
    return (random.choice(options))

def current_time():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def current_date_main():
    from datetime import date
    today = date.today()
    return today

def addition(query):
    #Getting numbers from the query
    numbers = [int(num) for num in query.split() if num.isdigit()]
    return sum(numbers)

def subtract(query):
    #Getting numbers from the query
    numbers = [int(num) for num in query.split() if num.isdigit()]
    return numbers[0] - numbers[1]

def multiply(query):
    import math
    #Getting numbers from the query
    numbers = [int(num) for num in query.split() if num.isdigit()]
    return math.prod(numbers)

def divide(query):
    #Getting numbers from the query
    numbers = [int(num) for num in query.split() if num.isdigit()]
    return numbers[0] / numbers[1]

def math_func(query):
    import math

   

def find_math_function(query):
    import math
    # Split the query into a list of words
    words = query.split()
    function = ''
    
    # Use list comprehension to find the numbers in the query
    numbers = [int(word) for word in words if word.isdigit()]
    
    # Initialize an empty result
    result = {}
    
    # Check if the word 'sin' is in the query
    if 'sin' in words:
        function = "sin"
        # Use list comprehension to calculate the sin of the numbers
        result['sin'] = [math.sin(num) for num in numbers]
    
    # Check if the word 'cos' is in the query
    if 'cos' in words:
        function = "cos"
        # Use list comprehension to calculate the cos of the numbers
        result['cos'] = [math.cos(num) for num in numbers]
    
    # Check if the word 'factorial' is in the query
    if 'factorial' in words:
        function = "factorial"
        # Use list comprehension to calculate the factorial of the numbers
        result['factorial'] = [math.factorial(num) for num in numbers]

     # Check if the word 'sqrt' is in the query
    if 'sqrt' in words:
        # Use list comprehension to calculate the square root of the numbers
        result['sqrt'] = [math.sqrt(num) for num in numbers]
    
    # Check if the word 'log' is in the query
    if 'log' in words:
        # Use list comprehension to calculate the logarithm of the numbers
        result['log'] = [math.log(num) for num in numbers]
    
    # Check if the word 'abs' is in the query
    if 'abs' in words:
        # Use list comprehension to calculate the absolute value of the numbers
        result['abs'] = [abs(num) for num in numbers]
    
    # Return the result
    print(result)

