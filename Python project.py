python 

#1เขียนโปรแกรมเพื่อรับ input เป็น string และแสดงผลเป็น string นั้นในลำดับที่กลับกัน เช่น
input: HELLO
output: OLLEH

str = "HELLO"
new_str = str[::-1]
print(new_str)

OLLEH

#2 เขียนโปรแกรมเพื่อคำนวณลำดับฟิโบนัคชี (Fibonacci) โดยรับ input เป็นจำนวนของลำดับและแสดงผลตามจำนวนนั้น (เริ่มนับจาก 0) เช่น
#input: 5
#output: 0, 1, 1, 2, 3
#หมายเหตุ 
#(1)  ลำดับฟิโบนัคชีสามารถคำนวณได้จากสูตร Fn = Fn-1 + Fn-2 โดย F0 = 0 และ F1 = 1
#(2) ข้อนี้มีคะแนนพิเศษสำหรับการเขียนโปรแกรมแบบ recursive function

#Fibonacci
#Fn : 0 , 1, 1, 2, 3 , 5
# n : 0 1 2 3 4 5
#Fn = Fn-2 + Fn-1

def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib(n-1) + fib(n-2)

print( fib(5) )
for n  in range(0,5):
    print( fib(n) )

5
0
1
1
2
3

#3. เขียนโปรแกรมโดยรับ input เป็นขนาดของ pattern เป็นจำนวนคี่ แสดงผล pattern ที่สัมพันธ์กับขนาดที่ได้รับ 

def p_pattern(size):
    for a in range(size):
        for b in range(size):
            if a == b or a + b == size -1:
                print("*", end="")
            else:
                print("-", end="")
        print()

# pattern
size = int(input("pattern size : "))

if size % 2 == 0 :
        print("pattern size")
else:
        p_pattern(size)

pattern size : 7
*-----*
-*---*-
--*-*--
---*---
--*-*--
-*---*-
*-----*

#เขียนโปรแกรมเพื่อแสดงผลตัวอักษร A และ B โดยรับ input เป็นจำนวนของตัวอักษร A และ B จากนั้นแสดงผลตัวอักษรทั้งสองตามจำนวนที่ได้รับ
def str(no_a, no_b):
    result = ""
    if abs(no_a - no_b) > 2:
        return "error"
    elif no_a >= no_b:
        while no_a > 0 or no_b > 0:
            if no_a > no_b and no_a > 0:
                result += "A"
                no_a -= 1
            elif no_b > 0:
                result += "B"
                no_b -= 1
            if no_a > no_b and no_a > 0:
                result += "A"
                no_a -= 1
            elif no_b > 0:
                result += "B"
                no_b -= 1
    else:
        while no_a > 0 or no_b > 0:
            if no_b > no_a and no_b > 0:
                result += "B"
                no_b -= 1
            elif no_a > 0:
                result += "A"
                no_a -= 1
            if no_b > no_a and no_b > 0:
                result += "B"
                no_b -= 1
            elif no_a > 0:
                result += "A"
                no_a -= 1
    return result

no_a = int(input("จำนวนตัว A: "))
no_b = int(input("จำนวนตัว B: "))

output = str(no_a, no_b)
print("output:", output)

จำนวนตัว A: 5
จำนวนตัว B: 3
output: AABABABA
