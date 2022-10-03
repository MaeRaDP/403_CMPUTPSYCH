# Variable operations exercises

# 1. Create 3 vars
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_int)
print(sub_code + subnr_str)

# 2. use operations to create following output

# "sub 2"
print(sub_code + " " + subnr_str)

# "sub 222"
print(sub_code + " " + (subnr_str)*3)

# "sub2sub2sub2"
print((sub_code + subnr_str)*3)

# "subsubsub222"
print((sub_code)*3 + (subnr_str)*3)
