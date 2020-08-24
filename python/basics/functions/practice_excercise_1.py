def spy_game(nList):
    #is_present=False
    iteration_count=0
    for n in nList:
        if (n==0 or n==7) :
            iteration_count=iteration_count+1
        else:
            iteration_count=0
        if iteration_count==3:
            return True
            #break

    return False

# print(spy_game([1,2,4,0,7,0,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([0,0,7,0,4,5,0]))

# def spy_game_1(nList):
#     for n in nList:
#         if n==0 or n==7:

def spy_game_1(nList):
    code=[0,0,7,'a']
    for n in nList:
        if n==code[0]:
           code.pop(0)
    return len(code)==1

print(spy_game_1([1,2,4,0,7,0,5]))
print(spy_game_1([1,0,2,4,0,5,7]))
print(spy_game_1([0,0,7,0,4,5,0]))

    
          
       
