def build_heap(data):
    swaps = []
    n=len(data)
    for i in range(n//2,-1,-1):
        heapsort(i,n,data,swaps)
    return swaps

def heapsort(i,n,data,swaps):
    x=i
    y=2*i+1
    z=2*i+2
    if n>y and data[x]>data[y]:
        x=y
    if n>z and data[x]>data[z]:
        x=z
    if i!=x:
        data[i],data[x]=data[x],data[i]
        swaps.append((i,x))
        i=x

def main():
    try:
        txt=input().split()
        if txt[0]=='I':
            n = int(input())
            data = list(map(int, input().split()))
        elif txt[0]=='F':
            file="tests/"+input()
            with open(file, mode='r') as filename:
                n=int(filename.readline())
                data = list(map(int, filename.readline().split()))

        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        
    except Exception as ex:
        print("Error")
        return

if __name__ == "__main__":
    main()
