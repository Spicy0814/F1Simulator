import time

red_circle = "🔴 "
black_circle = "⚫ "

print("⚫ ⚫ ⚫ ⚫ ⚫", end="")

for x in range (0,6):
    b = "🔴 " * x
    print (b, end="\r")
    time.sleep(1)

time.sleep(2)

print("⚫ ⚫ ⚫ ⚫ ⚫")

# Red circle: 🔴    Black circle: ⚫
# python3 /Users/samuelfrodell/Desktop/Python/F1Simulator/systest.py




#    print("🔴  ", end="")
#    sys.stdout.flush()
#    time.sleep(1)
#    print('🔴  ', end="")
#    sys.stdout.flush()
#    time.sleep(1)
#    print('🔴  ', end="")
#    sys.stdout.flush()
#    time.sleep(1)
#    print('🔴  ', end="")
#    sys.stdout.flush()
#    time.sleep(1)
#    print('🔴 ')
