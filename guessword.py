import random
#----------------------------hard-----------------------------------------------------------
def hard(word):
    prospathies = 6
    print("your attemps:",prospathies)
    #print(word)
    lista_word = []
    for i in word :
        lista_word.append(i)
    anyp = []
    
    alph=[chr(i) for i in range(913,930)]+[chr(i)for i in range(931,938)]
    
    icl = []
    al_g_2=[]
    al_g_1 = []
    number=1
    z=[]
    while prospathies > 0:
        fed = ['-' for _ in lista_word]

        guess = input("give a word: no"+str(number)).upper()
        print(guess)
        
        for i in guess:
            if i not in  al_g_1:
                
                
                if guess == word:
                    print("correct!!!")
                    prospathies = 0
                    break
        
                if len(guess) != 5:
                    print("the word must have exactly 5 letters")
            
                    continue
                for i, (a, b) in enumerate(zip(lista_word, guess)):
             
                    if a == b :
                        fed[i]="O"
                    elif b in lista_word:
                        fed[i]="X"
                    else:
                        if b not in icl:
                            icl.append(b)#grammata poy den yparxoyn sto guess
            else:
                if i not in z:
                    z.append(i)
                
        if z:
            print("Cannot use letters known not to exist in word",z)
      
        
             
                
       
        for i in guess:
            if i not in lista_word and i in alph:
                anyp.append(i)
                alph.remove(i)
                al_g_1.append(i)          
                    
        for i in guess:
            if i in lista_word and i in alph:
                
                 alph.remove(i)
                 al_g_1.append(i)

        for i in guess:
            if i not in z:
                number +=1
                break
            break    
          
        
       
      
        print("you have already guess the letter ",al_g_1)        
        
        c= "".join(fed)
        d ="".join(anyp)
        #alph_join = "".join(alph) mou aresei perisotero na emfanizetai san lista
        print("letters you can use",alph)
        print("letters that not exist in secret word", d)

        print(c)
    
        prospathies -= 1
        
        print("the attemps you have:",prospathies)
        if prospathies == 0:   
            print("out of attemps!!")
    print("the hiden word was", word)
       
    
#--------------------------------------------------------normal_mode------------------------------------------------------------------------------------------------------------------------------  
    

def normal(word):
    prospathies = 6
    print("your attemps:",prospathies)
    #print(word)
    lista_word = []
    
    for i in word :
        lista_word.append(i)
    #print(lista_word)
    alph=[chr(i) for i in range(913,930)]+[chr(i)for i in range(931,938)]
   
    icl = []
    al_g_2=[]
    al_g_1=[]
    number=1
    
    while prospathies>0:
        
        fed = ['-' for _ in lista_word]

  
        guess = input("give a word: No"+str(number)).upper()#na to kanw na dinei tis fores pou edwse leksi       
        print(guess)
        
        if len(guess)!=5:
            print("the word must have exactly 5 letters")
            continue
        if guess==word:
            print("correct!!! ")
            prospathies = 0
            break
        
        for i, (a, b) in enumerate(zip(lista_word, guess)):
            if a == b :
                fed[i]="O"
            elif b in lista_word:
                fed[i]="X"
            else:
                if b not in icl:
                    icl.append(b)#grammata poy den yparxoyn sthn mantepsia
                
                
        for i in guess:
            if i not in lista_word and i in alph:
                
                alph.remove(i)
                al_g_1.append(i)                             
        for i in guess:
            if i in lista_word and i in alph:
                
                 alph.remove(i)
                 al_g_2.append(i)
                 al_g_1.append(i)

        print("you have already guess the letter ",al_g_1)
        
        
    
        c= "".join(fed)
        v="".join(icl)
        print("letters you have to use",alph)
        print(c)
            
        print("letters not in secret word",v)
        
        number=number+1
        
        prospathies = prospathies-1
        print("attemps you have:",prospathies)
        if prospathies == 0:   
            print("out of attemps!!!")
    print("the hiden word was", word)
        


    

#______________________________________MAIN_________________________________________________________

f = open("5letterwords.txt", encoding="utf-8")
w=[]
for line in f :
    c= line.strip()
    w.append(c)

random_word = random.choice(w)

mode = input("choose mode H for hard N for normal").lower()

if mode == "h":
    mode_hard = hard(random_word)
    print (mode_hard)
else:
    mode_normal = normal(random_word)
    print(mode_normal)

