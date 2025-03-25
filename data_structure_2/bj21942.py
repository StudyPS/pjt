"""
부품 대여장
https://www.acmicpc.net/problem/21942
"""

import sys
from collections import defaultdict


def convert_sec(date: str) -> int:
    result = 0
    day, time = date.split("/", 2)
    day = int(day)
    hour, minute = map(int, time.split(":", 2))
    result += (day * 24 * 60) + hour * 60 + minute
    return result


def time_to_seconds(time_str: str) -> int:
    date_part, time_part = time_str.split()  # 연도 제외
    month, day = map(int, date_part.split("-")[1:])  # 월, 일 추출
    hour, minute = map(int, time_part.split(":"))  # 시, 분 추출

    # 월별 일 수 (윤년 고려 안 함)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 1월 1일부터 해당 월일까지의 총 일 수 계산
    total_days = sum(days_in_month[: month - 1]) + (day)

    # 초로 변환
    return total_days * 24 * 60 + hour * 60 + minute


# print(convert_sec(D))


C, D, M = sys.stdin.readline().strip().split()
LOOP_COUNT = int(C)
FINE = int(M)  # 1분당 벌금
TIMEOUT = convert_sec(D)
rent_list = {}
result_list = defaultdict(int)
for i in range(LOOP_COUNT):
    date, time, part, human = sys.stdin.readline().strip().split()
    key = part + "|" + human
    if not rent_list.get(key):
        rent_list[key] = time_to_seconds(date + " " + time)
    else:
        prev_time = rent_list[key]
        curr_time = time_to_seconds(date + " " + time)
        check = (curr_time - prev_time) - TIMEOUT

        if check > 0:
            result_list[human] += check * FINE
        del rent_list[key]
if len(result_list) == 0:
    print("-1")
for human, fine in sorted(result_list.items()):
    print(human, fine)
