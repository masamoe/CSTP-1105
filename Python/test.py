def solution(number):
    final_sum = 0
    if number != abs(number):
        return final_sum
    else:
        for num in range(number):
            if num % 3 == 0 or num % 5 == 0:
                print(num)
                final_sum = final_sum+num
        return final_sum

print(solution(6))