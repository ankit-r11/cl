def lesser_of_two_evens(m,n):
    lesser=0
    greater=0
    if m>n:
        lesser=n
        greater=m
    else:
        lesser=m
        greater=n
    if m%2==0 and n%2==0:
        return lesser
    elif m%2!=0 or n%2!=0:
        return greater

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

def animal_crackers(line):
    words=line.split()
    if words[0][0]==words[1][0]:
        return True
    return False

print(animal_crackers('Levelheaded Llama'))

print(animal_crackers('Crazy Kangaroo'))

def old_macdonald(text):
    formattedwords=''
    for index,letter in enumerate(text):
        if index==0 or index==3:
            formattedwords=formattedwords+letter.upper()
        else:
            formattedwords=formattedwords+letter
    return formattedwords

print(old_macdonald('macdonald'))


def reverse_sentence(line):
    words=line.split()
    length=len(words)
    final_word=''
    index_list=list(range(0,length))
    index_list.sort(reverse=True)
    print(index_list)
    for item in index_list:
       final_word=final_word+words[item]
       if item!=0:
           final_word=final_word+' '
    return final_word

print(reverse_sentence('Pyhton is a programming language'))

