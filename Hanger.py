def draw_hanger(lives):
        hangman_files = [
        "D:/Python/hangman4.txt",
        "D:/Python/hangman3.txt",
        "D:/Python/hangman2.txt",
        "D:/Python/hangman1.txt",
        "D:/Python/hangman0.txt"
    ]

        with open(hangman_files[lives], 'r') as f:
            print(f.read())
def hangman():
    with open('D:/Python/russian_nouns.txt', 'r', encoding="UTF-8") as file:
        words=file.readlines()
        words =[s.strip("\n") for s in words]
    import Module
    d=Module.random_word(words)
    print(d)
    a="_"*len(d)
    print(a)
    b=5
    f="♥"*b
    print(f)
    list_word = list(a)
    list_2=[]

    while Module.lives_check(b):
        c=input()
        b, k = Module.word_check(d,c,list_word,b, list_2)
        f="♥"*b
        draw_hanger(b-1)
        print(f)
        if k==d:
            print('Поздравляю, вы отгадали слово!')
            ans=input('Хотите сыграть еще раз? (да/нет)').lower()
            
            if ans=='да':
                hangman()
    ans=input('Хотите сыграть еще раз? (да/нет)').lower()
    

  
    if ans=='да':
        hangman()
hangman()