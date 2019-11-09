#99乘法表-一般语法
for i in range(1,3):   
    print('%d x %d = %d' % (i,2,i*2),end=' ')
print('')
for i in range(1,4):
    print('%d x %d = %d' % (i,3,i*3),end=' ')
print('')
#最简洁语法
for i in range(1,10):
    for j in range(1,i+1):   
        print('%d x %d = %d' % (j,i,j*i),end=' ')
    print('')

#while语法示例
i = 1
while i <= 9: 
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j,i,i*j),end = '  ') 
        j += 1
    print('')
    i += 1