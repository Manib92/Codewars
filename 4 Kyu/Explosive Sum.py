"""
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
sum(1) # 1
sum(2) # 2  -> 1+1 , 2
sum(3) # 3 -> 1+1+1, 1+2, 3
sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

sum(10) # 42
Explosive
sum(50) # 204226
sum(80) # 15796476
sum(100) # 190569292
"""

def exp_sum(n):
    #How I did this problem was by working out the number of 1s,2s,3s,... which were in each partition.
    #create nxn array filled with 0s except the diagonal and all partitions
    #for 1s which were set to 1 as that is what I had observed.
    p = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(n+1):
        p[i][i] = 1
        p[i][1] = 1
    p[0][1] = 0
    #I'll need to give an example to explain this part...
    '''
    for partition 8 if I was looking for the number of 5s I know that 8-5=3 as 3<5 then
    the number of 5s in p(8) is equal to p(3). However if I was looking for the number of 3s in p(8) I would get
    8-3 = 5 but as 5>3 then I would look at the different numbers from 1 upto 3 for p(5) and total them together.
    ie in p(5) 1s = 1, 2s = 2 and 3s = 2 and the total would be 5 which is the number of 3s found in p(8).
    '''
    #For all partitions
    for i in range(2,n+1):
        #For all numbers within partition
        for j in range(2,i+1):
            rows = i-j
            total = 0
            #Total all of the numbers
            for k in range(1,j+1):
                if rows > j:
                    total += p[rows][k]
                else:
                    total += p[rows][k]
            p[i][j] = total
        p[i][i] = 1
    #Total the nth column as that is all we care about
    return sum(p[-1][:])
