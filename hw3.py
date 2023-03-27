def get_fixed_price(m):
    y=m*100/(100-discount)
    return y

discount=int(input('할인율은?'))
q=int(input('a상품의 할인된 가격은?'))
a=get_fixed_price(q)
r=int(input('b상품의 할인된 가격은?'))
b=get_fixed_price(r)
print('a상품의 정가',a,'원')
print('a상품의 정가',b,'원')
