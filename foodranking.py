#fname = input('enter file name:')
#if len(fname)<1:
 #   fname='foodarticle1.txt'
    

with open('foodarticle1.txt') as f:

    lines =f.readlines()
    print(lines)

    