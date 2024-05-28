import random

movies = ['inception','la la land','interstellar','avatar','spider man','avengers','titanic','skyfall','fast and furious','gravity']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letter): 
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def play():
    p1name = input("Enter your name p1 ")
    p2name = input("Enter your name p2 ")
    pp1=0
    pp2=0
    turn=0
    willing = True
    while willing:
        #player1
        if turn%2==0:
            print(p1name,'your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said = True
            while not_said:
                letter= input('Your letter  : ')
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input('press 1 to guess the movie or 2 unlock another letter: '))
                    if d==1:
                        ans=(input('your answer: '))
                        if ans==picked_movie:
                            pp1=pp1+1
                            print('Correct')
                            not_said=False
                            print(p1name, 'Your Score : ',pp1)
                        else:
                            print('Wrong answer, Try again')
                else:
                    print('lettter not found')
            c=int(input('press 1 to continue and 0 to quit '))
            if c==0:
                print(p1name, 'Score : ',pp1)
                print(p2name, 'Score : ',pp2)
                print('Thank You for Playing')
                print('Have a nice day')
                willing=False
            turn=turn+1

        else:
            #player2
            print(p2name,'your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said = True
            while not_said:
                letter= input('Your letter  : ')
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input('press 1 to guess the movie or 2 unlock another letter: '))
                    if d==1:
                        ans=input('your answer: ')
                        if ans==picked_movie:
                            pp2=pp2+1
                            print('Correct')
                            not_said=False
                            print(p2name, 'Your Score : ',pp2)
                        else:
                            print('Wrong answer, Try again')                       
                else:
                    print('lettter not found')
            c=int(input('press 1 to continue and 0 to quit '))
            if c==0:
                print(p1name, 'Your Score : ',pp1)
                print(p2name, 'Your Score : ',pp2)
                print('Thank You for Playing')
                print('Have a nice day')
                willing=False
            turn=turn+1
play()