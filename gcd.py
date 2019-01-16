def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    fail=0
    temp=1
    gcd=0
    
    for k in range(1,min(arr)+1):
        for i in range(num):
            print('k: '+str(k))
            if arr[i]%k != 0:
                fail=1
            else:
                temp=k
        
        if fail == 0:
            gcd=temp
    print('gcd: '+str(gcd))
    return gcd       
    pass

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    result= generalizedGCD(n,arr)
