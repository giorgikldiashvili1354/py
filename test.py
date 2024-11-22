
'''n = 6

result_list = [0]*6

for i in range(1,n+1) :
    result_list[i-1] = i**2

print(result_list)'''


'''////////'''


'''list_numb = [12,13,43,18,17]

result_list =[i%3 == 0 for i in list_numb]

print(list_numb)'''



'''//////////'''

'''n = 5
result_list = [1 for x in range(n)]

print(result_list)'''

'''////////'''



'''list_numb = [12,13,43,18,17]

result_list =[2*i-1 for i in list_numb if i%3 == 0]

print(result_list)'''

'''//////'''

'''print('p y t h o n'.split(' '))'''

'''/////////'''

'''//////'''

'''numb = input(' input your numbers with spacese:')

print(numb)'''

'''/////////'''


'''numb = input(' input your numbers with spacese:')


result_list = [i for i in numb.split(' ')]


print(result_list)'''

'''/////////////////'''

'''text = 'python'
result = [el.upper() for el in text]


print(result)'''

'''///////////////'''

'''result = [x for x in range(100,200)if x%2 == 0 or x%3 == 0]

print(result)'''

'''/////////////...'''

'''names = ['ia', 'goga', 'putbca']
result = [n.capitalize() for n in names if len(n)>4]

print(result)'''

'''numb = [12, 22, 34, 6, 7, 89, 0]

result = [f'{x} is even' if x%2 == 0 else f'{x} is odd' for x in numb]

print(result)'''