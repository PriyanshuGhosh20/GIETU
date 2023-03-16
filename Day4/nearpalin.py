#Next Greatest Palindrome
n = input('Enter a number: ')

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if is_palindrome(n):
   n1 = int(n)+1
   while not is_palindrome(n1):
       n1 = n1+1
   print(f'You entered {n}, but the next palindrome is {n1}')
else:
   print("Invalid")
