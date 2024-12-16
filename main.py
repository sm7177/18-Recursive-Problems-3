# def Hanoi(n,a,b,c):
#     if n==1:
#         print("Move disk 1 from rod",a,"to rod",b)
#         return
#     Hanoi(n-1,a,c,b)
#     print("Move disk",n,"from rod",a,"to rod",b)
#     Hanoi(n-1,c,b,a)
    
    
# n=int(input("Enter the number:"))
# Hanoi(n,"A","C","B")





keypad=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def printcombo(combo,curr,output,n):
    if(curr==n):
        print(*output,sep=",")
        return
    for i in range(len(keypad[combo[curr]])):
        output.append(keypad[combo[curr]][i])
        printcombo(combo,curr+1,output,n)
        output.pop()
        if (combo[curr]==0 or combo[curr]==1):
            return
        
combination=[2,3,3]
n=len(combination)
printcombo(combination,0,[],n)