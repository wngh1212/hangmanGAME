import random


eng = ['python','information','material','privilege','system']
engs = random.choice(eng)
word = ''

oppr = 10 #기회 횟수

while oppr > 0:
    
    fail = 0
    
    for char in engs:
        
        if char in word:
            print(char,end='')

        else:
            print('_',end=' ')
            fail += 1
    
    if fail==0:
        print('모든 영어 알파벳을 맞추셨습니다')
        
        break
    print()

    
    guess= input("문자를 입력하세요")
    
    word += guess
    
    if guess not in engs:
        oppr -=1
        print("해당하는 글자가 아닙니다")
        print("남은 기회는 ", oppr, '회입니다')
        if oppr ==0:
            print("모든기회를 소진해 글자를 맞추는데 실패 하였습니다")