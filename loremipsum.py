import random
import os
import re
from subprocess import check_call
clear = lambda: os.system('cls')

ftext=''
for file in os.listdir("books"):
    if file.endswith(".txt"):
        ftext = ftext+'.' + open(os.path.join("books", file), 'r', encoding="utf-8").read()

def su(w):
    for x in w:
        if x.isalpha():
            if x.isupper():
                return True
            return False

def stripper(wrd):
    c=0
    for x in wrd:
        if x.isalpha():
            if x.isupper():
                return wrd[c:]
            return False
        c=c+1



def rdm(wolist):
    while True:
        crand=random.choice(wolist)
        if su(crand):
            return crand


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)



b= ftext.replace('?', '?.')
b=b.replace('!', '!.')
b=b.replace('..', '.')
b=b.replace('\n', ' ')
b=b.replace('  ', ' ')
b=b.split('.')


def f(c, t):
    lst=[]
    for x in b:
        if len(x.strip().split(' '))==c and x[-1]==t:
            lst.append(x)

    clear()
    print('Enter word count(and text type optional such as "6 ?", "5 !"):')
    print('\n')
    cw=rdm(lst)
    copy2clip(stripper(cw))
    print(stripper(cw))
    
    return cw
    print('\n\n\n\n\n')
    
def s(c):
    lst=[]
    for x in b:
        if su(x):
            if len(stripper(x).strip().split(' '))==c:
                lst.append(x)
    clear()
    print('Enter word count(and text type optional such as "6 ?", "5 !"):')
    print('\n')
    cw=rdm(lst)
    copy2clip(stripper(cw))
    print(stripper(cw))
    return cw
    print(b.index(cw))
    print(b[b.index(cw)+1])
    print('\n\n\n\n\n')





def sw(c, wtm):
    lst=[]
    for x in b:
        if su(x):
            if len(stripper(x).strip().split(' '))==c:
                for f in stripper(x).strip().split(' '):
                    if f==wtm:
                        lst.append(x)
    clear()
    print('Enter word count(and text type optional such as "6 ?", "5 !"):')
    print('\n')
    cw=rdm(lst)
    copy2clip(stripper(cw))
    print(stripper(cw))
    return cw
    print(b.index(cw))
    print(b[b.index(cw)+1])
    print('\n\n\n\n\n')








lst=''
gnum=1
lword=''
header=True
while True:
    if header:
        print('Enter word count(and text type optional such as "6 ?", "5 !"):')

    inp = input()
    if inp=='exit' or inp=='quit':
        break

    elif inp=='more':

        def hasLet():
            global gnum
            global lword
            if not gnum:
                lword=b[gnum]
                gnum=b.index(lword)+1
            else:
                lword=b[gnum]
                gnum=gnum+1
            try:
                reex=re.search('[a-zA-Z]', stripper(b[gnum]))
                if reex:
                    copy2clip(stripper(b[gnum]))
                    print(stripper(b[gnum]))
                else:
                    hasLet()
            except:
                    hasLet()
        hasLet()
        continue



    elif inp=='prev':
        def hasLetP():
            global gnum
            global lword
            if not gnum:
                lword=b[gnum]
                gnum=b.index(lword)-1

            else:
                lword=b[gnum]
                gnum=gnum-1
            try:
                reex=re.search('[a-zA-Z]', stripper(b[gnum]))
                if reex:
                    copy2clip(stripper(b[gnum]))
                    print(stripper(b[gnum]))
                else:
                    hasLetP()
            except:
                    hasLetP()
        hasLetP()

        continue


    inp=inp.split(' ')
    lst=inp
    if len(inp)==2:
        if len(inp[1])==1:
            gnum=1
            header=False
            f(int(inp[0]), inp[1])
        else:
            gnum=False
            header=False
            try:
                lword = sw(int(inp[0]), inp[1])
            except:
                print('cant find')
                
    else:
        try:
            gnum=False
            header=False
            lword = s(int(inp[0]))
        except:
            try:
                s(int(lst[0]))
            except BaseException as error:
                print(error)




