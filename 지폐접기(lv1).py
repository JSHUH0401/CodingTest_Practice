#지폐 맥스값 가져와. 지갑의 가로랑 비교해.
# 1. 지폐가 더 크면 지갑 세로랑 비교해.-> 또 크면, 접어!
#만약 이게 끝났다면, 일단 최대값은 지갑의 최대값보다 작아진 상황. 이제 다른쪽 애를 확인할 차례?
def solution(wallet, bill):
    answer = 0
    while max(wallet) < max(bill):
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
            answer += 1
        else:
            bill[1] = bill[1]//2
            answer += 1

    while min(bill) > min(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
            answer += 1
        else:
            bill[1] = bill[1]//2
            answer += 1
    return answer