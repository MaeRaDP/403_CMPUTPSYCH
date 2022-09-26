# Are 1 and 1.0 equivalent?
print(1 == 1.0)
# Are "1" and "1.0" equivalent?
print('1' == '1.0')
# Are 5 and (3+2) equivalent?
print(5 == (3+2))
# [Are 1 and 1.0 equivalent?] X [Are "1" and "1.0" equivalent?] X [Are 5 and (3+2) equivalent?]
# 5 ways to get True as output
print(1 == 1.0 and not '1' == '1.0' and 5 == (3+2)) #True
print(1 == 1.0 and not '1' == '1.0' or 5 == (3+2)) #True
print(1 == 1.0 and '1' == '1.0' or 5 == (3+2)) #True
print(1 == 1.0 or'1' == '1.0' or 5 == (3+2)) #True
print(1 == 1.0 or '1' == '1.0' and 5 == (3+2)) #True