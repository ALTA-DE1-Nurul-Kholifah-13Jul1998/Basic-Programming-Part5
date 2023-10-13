def prime_number(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number%2==0 or number%3==0:
        return False
    if number >= 5:
        i = 5
        while i*i < number:
            if number%i==0 or number%(i+2)==0:
                return False
            i += 1
        return True  

if __name__ == '__main__':
    print(prime_number(1500450271)) # True     
    print(prime_number(1000000007)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(7)) # True
    print(prime_number(11)) # True
