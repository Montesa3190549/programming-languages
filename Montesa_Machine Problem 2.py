# # # # # # # # # # 10
# # # # # # # # # 
# # # # # # # #
# # # # # # #
# # # # # #
# # # # # 5

for x in reversed(range (10)):
    for y in range (x):print("#", end = ' ')
    print(" ")
    if x == 5: break
