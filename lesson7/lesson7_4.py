import random
import pyinputplus as pypi

while(True):
    min:int = 1
    max:int = 10
    count:int = 0

    target:int = random.randint(min,max)
    print(target)
    print("==========猜數字遊戲========\n")
    while(True):
        keyin:int = pypi.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)
        print(keyin)
        count += 1
        if keyin == target:
            print(f"bingo, 答案是:{keyin}")
            print(f"你猜了{count}次")
            break
        elif(keyin > target):
            print(f"再小一點")
            max = keyin - 1 
        elif(keyin < target):
            print(f"再大一點")
            min = keyin + 1
        print(f"您已經猜了{count}次")
    play_again:str = pypi.inputYesNo("請問還要繼續嗎?(y,n)")
    if play_again == "no":
        break

print("遊戲結束")