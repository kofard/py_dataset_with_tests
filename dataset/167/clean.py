"""
Test cases:
Do you want to enter your denominations ? (Y/N) :N
Enter the change you want to make in Indian Currency: 987
Following is minimal  change for 987 :
500 100 100 100 100 50 20 10 5 2

Do you want to enter your denominations ? (Y/N) :Y
Enter number of denomination:10
1
5
10
20
50
100
200
500
1000
2000
Enter the change you want to make: 18745
Following is minimal  change for 18745 :
2000 2000 2000 2000 2000 2000 2000 2000 2000 500 200 20 20 5

Do you want to enter your denominations ? (Y/N) :N
Enter the change you want to make: 0
The total value cannot be zero or negative.
Do you want to enter your denominations ? (Y/N) :N
Enter the change you want to make: -98
The total value cannot be zero or negative.

Do you want to enter your denominations ? (Y/N) :Y
Enter number of denomination:5
1
5
100
500
1000
Enter the change you want to make: 456
Following is minimal   change for 456 :
100 100 100 100 5 5 5 5 5 5 5 5 5 5 5 1
"""

def find_minimum_change(denominations: list[int], value: str) -> list[int]:
    """Find the minimum change from the given denominations and value"""
    total_value = int(value)
    answer = []
    for denomination in reversed(denominations):
        while int(total_value) >= int(denomination):
            total_value -= int(denomination)
            answer.append(denomination)
    return answer