"""
Approach 2:

[2, 100, 50, 120, 1000], newBudget = 190
[1000, 120, 100, 50, 2], newBudget = 190

Multiply the potential cap by number of grants that will be affected

surplus -= 1 * (1000 - 120)
surplus -= 2 * (120 - 100)
surplus -= 3 * (100 - 50)
surplus -= 4 * (50 - 2)

1.  Sort
2.  Append a 0 to account for a case where everything is under the cap
3.  Sum the array and subtract the new budget to find surplus
4.  On each loop iteration, find a new potential cap
    How much money can we save if we introduce the new cap at the current index?
    How about the next index? Multiple the number of indexes affected by the 
    amount that would be saved by introducing the cap
5.  Repeat until the surplus becomes negative. That would mean that a lower bound is found
6.  Once a lower bound is found, there may be leftover grant money. Add that in

Time    : O(n log n)
Space   : O(1)
"""

def find_grants_cap(grantsArray, newBudget):
    #   1.
    grantsArray = sorted(grantsArray, reverse = True)

    #   2.
    grantsArray.append(0)

    #   3.
    surplus = sum(grantsArray) - newBudget

    #   4
    if surplus <= 0:
        return grantsArray[0]

    for i in range(len(grantsArray) - 1):
        potential_cap = (i + 1) * (grantsArray[i] - grantsArray[i + 1])
        surplus -= potential_cap
        
        if surplus <= 0:
            break

    smallest_grant_affected = grantsArray[i + 1]
    leftover_money = -(surplus / (i + 1))

    return smallest_grant_affected + leftover_money

"""
input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
           
Approach:

1.  Divide the newBudget by number of grants. x = 38
2.  Check which elements in the array are over 38 y = 4
2a. Subtract sum of elements that are not affected from newBudget = 188
3.  Change x to equal the new 188 / 4
4.  Step through array again and replace with appropriate values

Time  : O(n)
Space : O(1)
"""

grantsArray = [2, 4]
newBudget = 3

print(find_grants_cap(grantsArray, newBudget))