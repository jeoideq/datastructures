

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

def sum(n):
    if n==0:
        return n 
    else: 
        return n+sum(n-1)

add=sum(10) 
print(add)






