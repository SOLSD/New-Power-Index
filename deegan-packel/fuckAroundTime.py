def combo(lst):
    new_lst =[]
    n = len(lst)
    for i in range(n):
        size = 1
        while size < n:
            combo = [lst[i]]
            for j in range(n):
                if i < j and len(combo) <= size:
                    combo.append(lst[j])
            new_lst.append(combo)
            size += 1
    print(new_lst)

combo([1,2,3,4])
