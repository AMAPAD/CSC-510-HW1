class SimpleCalculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add_numbers(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def multiply_numbers(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b


# Example usage
num1 = 5
num2 = 3

calculator_object = SimpleCalculator()

addition_result = calculator_object.add_numbers(num1, num2)
print(f"The addition of numbers {num1} and {num2} is: {addition_result}")

multiplication_result = calculator_object.multiply_numbers(num1, num2)
print(f"The multiplication of numbers {num1} and {num2} is: {multiplication_result}")
