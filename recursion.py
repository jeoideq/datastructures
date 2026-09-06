

def display(n):
        if n==0: #base case 
                return n
        else: #recursive case 
                print("jade")
                display(n-1)
    

display(5)


def display(n):
        if n==0:
                return n
        else:
                display(n-1)
                print(n)
                
display(10)