def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_ind = 0
    sort_ind = 0
    if ext == "code":
        ext_ind = 0
    elif ext == "date":
        ext_ind = 1
    elif ext == "maximum":
        ext_ind = 2
    else:
        ext_ind = 3
    if sort_by == "code":
        sort_ind = 0
    elif sort_by == "date":
        sort_ind = 1
    elif sort_by == "maximum":
        sort_ind = 2
    else:
        sort_ind = 3
    real = []
    lst = []
    for cell in data:
        if cell[ext_ind] < val_ext:
            answer.append(cell)
            lst.append(cell[sort_ind])
    
    for i in range(len(answer)):
        for cell in answer:
            if cell[sort_ind] == min(lst):
                real.append(cell)
                answer.pop(answer.index(cell))
                lst.pop(lst.index(min(lst)))
                print(lst)
                if len(lst) == 0:
                    break 
    return real

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date",20300501,"remain"))