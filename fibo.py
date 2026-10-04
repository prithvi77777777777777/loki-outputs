# fibo.py

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def print_fibonacci_series(limit):
    for i in range(limit):
        print(fibonacci(i))

# Example usage
if __name__ == "__main__":
    print_fibonacci_series(10)