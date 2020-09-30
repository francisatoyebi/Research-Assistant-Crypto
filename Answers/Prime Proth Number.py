def main(n):
    '''This is a function to check if an entry is a prime nber or not based on Proth's principle
    
    This function takes in one argument, n. 
    'n': must be an integer.
    '''
        
    def poweroftwo(n):
        '''a function that determines if a number is a power of 2'''
        return (n and (not(n & (n - 1)))) 

    def prothchecker(n):
        '''checks if a number is a proth number'''
        n = n-1
        k = 1
        while(k < (n//k)): 

            if(n % k == 0): 

                if(poweroftwo(n//k)): 
                    return True

            k = k + 2

        return False
    
    def is_prime_number(x):
        '''this is a function to check if a number is a prime number'''
        if x >= 2:
            for y in range(2,x):
                if not ( x % y ):
                    return False
        else:
            return False
        return True        

    if(prothchecker(n)): 
        if n > 1:
            print('it is a proth number, checking if it is prime')
            print('=============================================')
            if is_prime_number(n):
                print(f'\n{n} is a proth and a prime number.')
                
            else:
                print(f'{n} is a proth but not a prime number.')
    else: 
        print("Not a proth number in the first place.")
    