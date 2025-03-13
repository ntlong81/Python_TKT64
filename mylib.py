abig_prime1 = 518308862288372742720302584531
def is_prime(n:int)->bool:
    if n<2:
        return False
    else:
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False
    return True 
def get_fre_words(text:str)->dict:
    fre_dict = {}
    for word in text.split():
        if word in fre_dict:
            fre_dict[word] += 1
        else:
            fre_dict[word] = 1
    return fre_dict

print('The lib is imported')