# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())

for i in range(T):
    se=""
    so=""
    S=str(input())
    for j in range(len(S)):
        if j%2==0:
            se=se+S[j]
        else:
            so=so+S[j]
    print(se,so)
