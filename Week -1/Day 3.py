# Sequencing method
# 1. common 2. List 3. String
text = 'Hello, World!'
print(len(text))
tuple = (1,2,3,4,5)
print(len(tuple))
dictionary={"name" :"pooja", "age":"33", "city":"Mumbai"}
print(len(dictionary))
set={5,6,3,2,1,8,9,4}
print(len(set))
empty=[]
print(len(empty))
nested=[[22,13,5,3],[5,6,7],[89],[67,49,0,10]]
print(len(nested))
numbers={10,20,2,5,30}
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
label=["a","b","z","f"]
print(sorted(label))

#List method
color = ["orange","pink"]
color.append("green")
print(color)

animal = ["dog","cat","pig"]
animal.insert(2,"rat")
print(animal)

range=[6,5,3]
range.remove(5)
print(range)
range.pop(0)
print(range)
range=[2,14,16,18,20]
range.clear()
print(range)