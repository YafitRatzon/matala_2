#Matala2 
#Yafit Ratzon 205655343

def revword(word:str)-> str:
    word= list(word)
    start = 0
    end = len(word)-1
    while start < int(len(word)/2):
        temp = word[start]
        word[start] = word[end]
        word[end] = temp
        start+=1
        end-=1
    word="".join(word).lower()
    return word

def countword()->int:
    file= open('text.txt','r')
    word= file.readline()
    word=word.lower()
    word=word.rstrip()
    count=1
   
    for line in file:
        line=line.rstrip()
        listt=line.split(' ')
        for node in listt:
            node=revword(node)
            if node == word:
                count+=1
    return count


