
def find_nth_fib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return find_nth_fib(n-1) + return find_nth_fib(n-2)



# O(N) TIME
def find_nth_fib(n):
    last_two = [0,1]
    if n < 3:
        return last_two[n-1]
    
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1]= next_fib
        counter += 1
    return last_two[1]


def find_nth_fib(n, already_found={1:0, 2:1}):
    if n in already_found:
        return already_found[n]
    already_found[n] = already_found(n-1, already_found) + already_found(n-2, already_found)
    return already_found[n]
    
