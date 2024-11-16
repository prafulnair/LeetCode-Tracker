
import re
string = "This Sweater costs $40 dollars"
print(string)

"""
To find the cost of the stuff and then add 20% discount to it 
"""

cost = re.findall(r'\d+',string)
print(cost)
finalCost = int(cost[0]) - 0.2*int(cost[0])

print(f"This sweater cost {finalCost} now")