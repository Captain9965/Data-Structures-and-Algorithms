

"""
    For normal recursion, the space complexity is always O(n), for tail recursion, it
    is O(1)
    This is tail recursion:

"""

""" normal  recursive factorial: """

def factorial_recursive(number: int):
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)

""" tail recursive with O(1) space complexity """
def tail_recursive_factorial(number: int, totalsoFar = 1):
    if number == 0:
        return totalsoFar
    return tail_recursive_factorial(number - 1, totalsoFar * number)

def factorial_iterative(number: int):
    result = number
    while number > 1:
        result = result * (number - 1)
        number -= 1
    return result
def first_no_10_fibonacci_iterative():
  
    val = 1
    prev_val = 0
    result = []
    result.append(prev_val)

    for i in range(9):
        result.append(val)
        old_prev = prev_val
        prev_val = val
        val += old_prev
    return result

def first_10_fibonacci_recursive(prev = 0, val = 1, result:list = []):
    if len(result) > 9:
        return result
    if not result:
        result.append(prev)
    result.append(val)
    return first_10_fibonacci_recursive(val , prev + val, result)

if __name__ == "__main__":
    number = 4
    print(factorial_recursive(number))
    print(factorial_iterative(number))

    print(first_no_10_fibonacci_iterative())

   
    print(first_10_fibonacci_recursive())
    print(tail_recursive_factorial(4))

