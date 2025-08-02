import math

class Calculator:
    def __init__(self, num1=0, num2=0):
        """Initialize calculator with optional default values"""
        self.num1 = num1
        self.num2 = num2
        self.history = []  # Track calculation history
    
    def _log_operation(self, operation, result):
        """Private method to log operations"""
        self.history.append(f"{operation} = {result}")
    
    def add(self, num1=None, num2=None):
        """Add two numbers"""
        a = num1 if num1 is not None else self.num1
        b = num2 if num2 is not None else self.num2
        result = a + b
        self._log_operation(f"{a} + {b}", result)
        return result
    
    def subtract(self, num1=None, num2=None):
        """Subtract second number from first"""
        a = num1 if num1 is not None else self.num1
        b = num2 if num2 is not None else self.num2
        result = a - b
        self._log_operation(f"{a} - {b}", result)
        return result
    
    def multiply(self, num1=None, num2=None):
        """Multiply two numbers"""
        a = num1 if num1 is not None else self.num1
        b = num2 if num2 is not None else self.num2
        result = a * b
        self._log_operation(f"{a} × {b}", result)
        return result
    
    def divide(self, num1=None, num2=None):
        """Divide first number by second"""
        a = num1 if num1 is not None else self.num1
        b = num2 if num2 is not None else self.num2
        
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        self._log_operation(f"{a} ÷ {b}", result)
        return result
    
    def floor_divide(self, num1=None, num2=None):
        """Floor division (integer division)"""
        a = num1 if num1 is not None else self.num1
        b = num2 if num2 is not None else self.num2
        
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a // b
        self._log_operation(f"{a} // {b}", result)
        return result
    
    def modulo(self, num1=None, num2=None):
        """Get remainder of division"""
        a = num1 if num1 is not None else self.num1
        b = num2 if num2 is not None else self.num2
        
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a % b
        self._log_operation(f"{a} % {b}", result)
        return result
    
    def square(self, num=None):
        """Calculate square of a number"""
        n = num if num is not None else self.num1
        result = n ** 2
        self._log_operation(f"{n}²", result)
        return result
    
    def cube(self, num=None):
        """Calculate cube of a number"""
        n = num if num is not None else self.num1
        result = n ** 3
        self._log_operation(f"{n}³", result)
        return result
    
    def square_root(self, num=None):
        """Calculate square root of a number"""
        n = num if num is not None else self.num1
        
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = math.sqrt(n)
        self._log_operation(f"√{n}", result)
        return result
    
    def factorial(self, num=None):
        """Calculate factorial of a number"""
        n = num if num is not None else self.num1
        
        # Validate input
        if not isinstance(n, int):
            raise TypeError("Factorial requires an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        # Calculate factorial
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        
        self._log_operation(f"{n}!", fact)
        return fact
    
    def power(self, base=None, exponent=None):
        """Calculate base raised to the power of exponent"""
        b = base if base is not None else self.num1
        e = exponent if exponent is not None else self.num2
        result = b ** e
        self._log_operation(f"{b}^{e}", result)
        return result
    
    def percentage(self, num=None, percent=None):
        """Calculate percentage of a number"""
        n = num if num is not None else self.num1
        p = percent if percent is not None else self.num2
        result = (n * p) / 100
        self._log_operation(f"{p}% of {n}", result)
        return result
    
    def absolute(self, num=None):
        """Get absolute value of a number"""
        n = num if num is not None else self.num1
        result = abs(n)
        self._log_operation(f"|{n}|", result)
        return result
    
    def set_values(self, num1, num2):
        """Update the instance variables"""
        self.num1 = num1
        self.num2 = num2
    
    def get_history(self):
        """Return calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
    
    def __str__(self):
        """String representation of calculator"""
        return f"Calculator(num1={self.num1}, num2={self.num2})"
    
    def __repr__(self):
        """Developer representation of calculator"""
        return f"Calculator({self.num1}, {self.num2})"

calculator = Calculator(3, 5)      
        
print(calculator.add())
print(calculator.subtract(10, 5))        
print(calculator.history)