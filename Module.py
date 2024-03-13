
import random

def random_word(word_1):
    return random.choice(word_1)
def lives_check(lives):
    if lives>0:
        return lives
    else :
        print("У вас не осталось жизней")

        
def word_check(word, bukva_guess, list1,lives,list2):
    for i in range(len(word)):
        if bukva_guess==word[i] and bukva_guess not in list2:
            list1[i]=bukva_guess
          
    if bukva_guess in list2:
        print('Вы уже пробовали эту букву')

    if bukva_guess not in word and len(bukva_guess)==1 and bukva_guess not in list2: 
        lives-=1
        list2.append(bukva_guess)
        print(f'Буква {bukva_guess} не встречается в слове')

    if len(bukva_guess)>1:
        print('Вам нужно ввести букву!')
    
    n=''.join(list1)
    print(n)

    return lives, n


