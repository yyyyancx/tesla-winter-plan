print("=== 简单计算器 ===")
a = float(input("请输入第一个数字 a："))
op = input("请输入运算符 (+ - * /)：")
b = float(input("请输入第二个数字 b："))

if op == "+":
    print("结果 =", a + b)
elif op == "-":
    print("结果 =", a - b)
elif op == "*":
    print("结果 =", a * b)
elif op == "/":
    if b == 0:
        print("错误：除数不能为 0")
    else:
        print("结果 =", a / b)
else:
    print("错误：不支持的运算符")
