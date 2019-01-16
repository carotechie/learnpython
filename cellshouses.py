
def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    
    for d in range(days):
        n_st=states
        for i in range(len(states)):
            if i == 0:
                if states[1] == 0:
                    n_st[i]=0
            elif i == len(states)-1:
                if states[-2] == 0:
                    n_st[i]=0
            else:
                if states[i-1] != states[i+1]:
                    n_st[i]=1
                else:
                    n_st[i]=0
        print('New status: '+str(n_st))
        states=n_st
    return n_st

if __name__ == '__main__':
    
    s = list(int, raw_input())
    n = int(raw_input())
    
    newstatus=cellCompete(s,n)