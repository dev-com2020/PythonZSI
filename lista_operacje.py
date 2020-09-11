print(len([1,2,3,4]))

tab1 = [1,2,3]
tab2 = [4,5,6]
print(tab1 + tab2)

tab3 = ['Papa']
print(tab3 * 3)

tab4 = [1,'a','b','d']
print(1 in tab4)

tab5 = [1,2,3]
for x in tab5:
    print(x, end="-")

tab6 = [1,2,3]
tab6.append('Python!')
tab6.append('Python@@')
print(tab6)

tab7 = [55,97,2,13]
tab7.sort()
print(tab7)

tab8 = [1,2,3]
tab8.reverse()
print(tab8)

tab9 = [1,2,3]
del tab9[1]
print(tab9)
