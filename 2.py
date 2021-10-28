#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     05.10.2021
# Copyright:   (c) admin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n, k = map(int, input().split())
*a, = map(int, input().split())
a.sort()
left = 0
right = a[-1] - a[0] + 1
while left < right:
    mid = (left + right)//2
    cows = 1
    last = a[0]
    for cur in a[1:]:
        if cur - last > mid:
            cows += 1
            last = cur
    if cows >= k:
        left = mid+1
    else:
        right = mid
print(left)