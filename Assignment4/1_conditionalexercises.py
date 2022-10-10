# Conditional exercises

# 1. Response + messages
# If the response is "1" or "2", print OK. 
# If the response is "NaN" (empty), print a "subject did not respond" message. 
# If the response is anything else, print "subject pressed the wrong key".

response = '1'

if response == '1' or response == '2':
    print("OK")
elif response == 'NaN':
    print("subject did not respond")
else: print("subject pressed the wrong key")

# 2. Nested "if" 
# If the response is "1", print "Correct!". 
# If the response is "2", print "Incorrect!"

response = '1'

if response == '1' or response == '2':
    print("OK")
    if response == '1':
        print("Correct!")
    if response == '2':
        print("Incorrect!")
elif response == 'NaN':
    print("subject did not respond")
else: print("subject pressed the wrong key")