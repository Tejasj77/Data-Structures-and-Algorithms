#passwords = ['because','can','do','must','we','what']
#loginattempt = 'wedowhatwemustbecausewecan'

#passwords = ['ab','abcd','cd']
#loginattempt = 'abcd'

#passwords = ['hello','planet']
#loginattempt = 'helloworld'

#passwords = ['ozkxyhkcst','xvglh','hpdnb','zfzahm']
#loginattempt = 'zfzahm'

#passwords = ['gurwgrb','maqz','holpkhqx','aowypvopu']
#loginattempt = 'gurwgrb'

#passwords = ['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','aaaaaaaa','aaaaaaaaa','aaaaaaaaaa']
#loginattempt = 'aaaaaaaaaab'

#passwords = ['fjrg','ckcapp','zhhwync','cgwkpsuzy','prnqnyek','tgfx','rxiydd','pgkujtpp','lxhwbxi','exsfzd']
#loginattempt = 'fjrgfjrgprnqnyekexsfzdlxhwbxilxhwbxizhhwynccgwkpsuzy'
integrity_counter = 0
def execution(passwords,loginattempt,integrity_counter):
    total = []
    char_counter = 0
    for i,j in enumerate(loginattempt):
        print(integrity_counter)
        if(len(total)!=0):
            for passing in range(integrity_counter):
                continue
            # if j == total[-1][-1]:
            #     continue
        addition = ''
        for iter in passwords:
            if j in iter:
                integrity_counter = 0
                for iter_counter in range(0,len(iter)):
                    if (i+iter_counter)<len(loginattempt):
                        if loginattempt[i+iter_counter] == iter[iter_counter]:
                            integrity_counter+=1
                            char_counter+=1
                if integrity_counter==len(iter):
                    addition+=iter
                    total.append(iter)
                    break

        print(total)
    if "".join(total)==loginattempt:
        return (" ".join(total))
    else:
        return "WRONG PASSWORD"

print(execution(passwords,loginattempt,integrity_counter))