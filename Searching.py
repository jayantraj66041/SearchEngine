data = ["jayant raj", "Harsh RAJ", "muKTA sinha", "Bijay Kr Sinha", "Ajay"]
print("***** Data Set *****\n")
for a in data:
    print(a)
print("\n")
#data = [x.lower() for x in data]
search = input("Enter a keyword - ")
points = [0 for a in range(0,len(data))]
#print(points)

# edject match
count = 0
for d in data:
    if d == search:
        points[count] += 1
    count += 1
del count
search = search.lower()
data = [x.lower() for x in data]

# case match
count = 0
for d in data:
    if d == search:
        points[count] += 1
    count += 1
del count
#print(points)

# is exist anywhere
count = 0
for d in data:
    if search in d:
        points[count] += 1
    count += 1
del count

count = 0
#s = search
for d in data:
    c = -1
    p = 0
    for i in search:
        if (i in d) and c < d.index(i):
            c = d.index(i)
            p += 1
    if p > len(search)//2:
        points[count] += 1
    count += 1
del count

if max(points) == 0:
    print("No match found!")
else:
    print(data[points.index(max(points))])
