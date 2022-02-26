# try:
#     print(x)
# except:
#     print('exception occured')
x='hello'
if not type(x) is int:
    raise Exception('not integer type')