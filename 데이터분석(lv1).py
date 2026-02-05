def solution(data, ext, val_ext, sort_by):
    by = [ "code", "date", "maximum", "remain" ]
    answer = []
    for item in data:
         if item[by.index(ext)] < val_ext:
              answer.append(item)
    return sorted(answer, key = lambda x: x[by.index(sort_by)])
#lambda는 함수를 대신하는 것. KEY 뒤에 나오는 것은 그걸 기준으로 정렬한다는 뜻. 3차원 배열이어도 동일하다.
print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date",20300501,"remain"))