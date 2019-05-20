"""Fibonacci
"""

def _fibonacci(n):
    """Fibonacci base function (naive recursive algorithm)
    Exponential Time

    Args:
        n: The nth number of the fibonacci sequence

    Returns:
        An integer of the nth number in the fibonacci sequence
    """

    if n <= 2:
        # Base case
        f = 1
    else:
        # Recursive call
        f = _fibonacci(n - 1) + _fibonacci(n - 2)
    
    return f


def main():
    """Main
    """
    _fibonacci_number = 10

    answer = _fibonacci(_fibonacci_number)
    print("Fibonacci Number {}: {}".format(_fibonacci_number, answer))

if __name__ == "__main__":
    # Execute only if run as a script
    main()