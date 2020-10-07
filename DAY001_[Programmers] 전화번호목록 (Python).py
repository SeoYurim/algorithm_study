# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42577
# hash
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False
    return answer

# sort() 활용
# list안의 string을 정렬하면 숫자라 할지라도 맨 앞자리 숫자의 크기로 정렬된다

# ["119", "97674223", "1195524421"]을
# 정렬하면
# ["119", "1195524421", "97674223"]가 된다

# "1195524421"의 크기가 더 클지라도, 맨 앞자리가 "1"이므로 더 앞에 정렬

# 그렇기에 앞 뒤로만 비교해도 접두어 찾기 가능!