numbers= [1,2,3,4] # list
print (type (numbers))
print (numbers[0])# dau
print (numbers[-1]) # cuoi
numbers.append(100) # them vao cuoi
print(numbers)
numbers.remove(1) # xoa di gtri 1 dau tien tim thay
a=numbers.pop() # xoa di gtri o cuoi vaf tra ve gtri do
print(numbers)
numbers.extend([5,6,7])  # mo rong lish ban dau
print(numbers)
cnt = numbers.count(1) # dem so luong so 1
lenn= len(numbers)# so luong ptu
print(lenn)
numbers.clear() # xoa sach list
numbers.insert(1,1000) # chen 1000 vao vtri 1
print(numbers)
index_of = numbers.index(1000) # tra ve vi tri cua 1000 trong list
del numbers[index_of] # xoa
#numbers.remove('1000')# xoa gtri 1000
dir(list)