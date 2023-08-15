import string,random
def  pass_gen(lengthPass,strengh):
    # the pass word length is determined by the lengthPass var
    if lengthPass <8 :
        raise Exception("The password must be at least eight characters long")
    if strengh not in ['weak','strong','very']:
        raise Exception('You have to choose a valid option')

    pwd =""
    lower = string.ascii_lowercase
    letter = string.ascii_letters
    symbol = string.punctuation
    dig = string.digits
    if strengh=='weak':
        lengthPass -=2
        for i in range(2): pwd += random.choice(dig)
        pwd += ''.join(random.sample(lower,lengthPass))
    elif strengh== "strong":
        l = lengthPass // 3
        for i in range(l): pwd += random.choice(dig)
        pwd += ''.join(random.sample(letter,lengthPass -l))
    elif strengh== "very":
        l= random.randint(4,lengthPass//2)
        pwd += ''.join(random.sample(dig + symbol,l))
        lengthPass -= l
        pwd += ''.join(random.sample(letter,lengthPass))
    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)

if __name__ == '__main__':
    try:
        leng = int(input("Enter the length for the passWord "))
        stren = input("Enter the strengh for the passWord, (weak, strong, very) ")
    except Exception as e:
        print(e)
    print(pass_gen(lengthPass=leng,strengh=stren))
