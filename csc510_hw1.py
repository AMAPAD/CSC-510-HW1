class simple_Calculator():
    def add_numbers(a, b):
        """Add two numbers and return the result."""
        return a + b
    def multiply_numbers(a, b):
         """Multiply two numbers and return the result."""
        return a * b


num1 = 5
num2 = 3


calculator_Object = simple_Calculator()


addition_Result = calculator_Object.add_numbers(num1, num2)
print("The addition of numbers 5 and 3 is: ", addition_Result)


multiplication_Result = calculator_Object.multiply_numbers(num1, num2)
print("The multiplication of numbers 5 and 3 is: ", multiplication_Result)
