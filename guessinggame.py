import random
a=random.randint(1,9)
TRY=0
Running= True
while Running:
    guess=int(input('choose your number: '))
    if guess<=a:
        if guess==a:
            print('Congrats, right number')
            TRY+=1
            print('you tried %d times'%TRY)
        else:
            print('Your number is lower')
            TRY+=1
            if str(input('wanna try again or exit?: '))=='exit':
                print('you tried %d times'%TRY)
                break
            else:
                continue
    else:
        print('Your number is higher')
        TRY+=1
        if str(input('wanna try again or exit?: '))=='exit':
            print('you tried %d times'%TRY)
            break
        else:
            continue    

