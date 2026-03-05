t = int(input())

for _ in range(t):
    tc = int(input())
    
    ans = []
    for i in range(tc):
        for j in range(i+1, tc):
            if i+j == tc:
                ans.append(f"{i} {j}")
    
    print(f"Pairs for {tc}:", end=" ")
    print(", ".join(ans))