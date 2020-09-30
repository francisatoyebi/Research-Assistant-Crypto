def main(n):
    '''This is a function to check if an entry is a prime nber or not based on Proth's principle
    
    This function takes in one argument, nber. 
    'nber':must be an integer.
    
    Example: '''
    def poweroftwo(n): 
        return (n and (not(n & (n - 1)))) 
    # Function to check if the 
    # Given nber is Proth nber or not 

    def prothchecker(n): 
        n = n-1
        k = 1
        while(k < (n//k)): 
            # check if k divides n or not 
            if(n % k == 0): 

                # Check if n / k is power of 2 or not 
                if(poweroftwo(n//k)): 
                    return True
            # update k to next odd nber 
            k = k + 2

        # If we reach here means 
        # there exists no value of K 
        # Such that k is odd nber 
        # and n / k is a power of 2 greater than k 
        return False
    
    def is_prime_number(x):
        if x >= 2:
            for y in range(2,x):
                if not ( x % y ):
                    return False
        else:
            return False
        return True        

    # Check n for Proth nber 
    if(prothchecker(n)): 
        if n > 1:
            print('it is a proth number, checking if it is prime')
            if is_prime_number(n):
                print(f'\n{n} is a proth and a prime number')
            else:
                print(f'{n} is a proth but not a prime number')
    else: 
        print("not a proth number in the first place"); 
    