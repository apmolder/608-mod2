values = [47, 95, 88, 73, 88, 84]

print('Sum', sum(values))
print('Count', len(values))

mean = sum(values)/ len (values)

print('Mean', mean)

# Mode and Median code 
# source "https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/"
values.sort()
List = []

x = 0 
while x < len(values):
    List.append(values.count(values[x]))
    x += 1
    
d1 = dict(zip(values, List))
d2 = {k for (k,v) in d1.items() if v == max (List)}

print('Mode', str(d2))

# Median
y = len(values)
values.sort()

if y % 2 == 0:
    median1 = values[y//2]
    median2 = values[y//2 - 1]
    median = (median1 + median2)/2
else:
    median = values[n//2]
    
print('Median' + str(median))


