def print_params(a,b,c):
    print(a,b,c)
list_ = [1,'строка',True]
print_params(*list_)

values_list = [5,'name',True]
values_dict = {'a':4,'b':8,'c':12}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [20,'hello']
print_params(*values_list_2, 42)
