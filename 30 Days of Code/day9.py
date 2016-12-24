#Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

N = int(input())
def factorial(N):
    if N > 1:
        return N * (factorial(N-1))
    else:
        return N

print(factorial(N))
