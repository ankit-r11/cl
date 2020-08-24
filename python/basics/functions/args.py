## *args treated as tuple 
def sum_number(*abc):
    print(abc)
    return sum(abc)
    
print(sum_number(1,2,4))
