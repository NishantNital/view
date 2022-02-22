def digits(n):
    # write your code here
    list=[]
    if n:
        x=n%10
        list.append(x)
        n=n/10
    for y in range(len(list)):
        print(y-1)    
def main():
    n = int(input())
    digits(n)

