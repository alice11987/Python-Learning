# -*- coding: utf-8 -*-
#没有默认值的parameter，必须放在有默认值parameter的前面！！：就如这里的“sex”
#下面show后面显示的是跟着def的排序
# def show(name='Tom', age=19):
#     print('name:%s, age:%d'%(name, age))
    
def show(sex, name='Tom', age=19):
    print('name:%s, age:%d, sex:%s'%(name, age, sex))
    
show('female', 'Alice')