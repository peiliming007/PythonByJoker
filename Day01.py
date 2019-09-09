#1
celsius=float(input("请输入一个摄氏度:>>"))
fahrenheit=(9 / 5) *celsius + 32
print("华氏温度为：%.1f" % fahrenheit)


#2
radius=float(input("请输入圆柱体的半径:>>"))
length=float(input("请输入圆柱体的高:>>"))
area= radius*radius*3.14159265
volume=area*length
print("The area is %.4f" % area )
print("The volume is %.1f" % volume)


#3
feet=float(input("请输入需要转换的英里值:>>"))
meter=feet*0.305
print("对应的米数为: %.4f" % meter)


#4
M=float(input("Enter amount of water in kilogram: "))
initiaTemperature=float(input("Enter the initia temperature: "))
finalTemperature=float(input("Enter the final temperature: "))
Q= M *(finalTemperature -initiaTemperature)*4184
print("The energy needed is %.1f" % Q)


#5
balance=float(input("输入差额:>>"))
interestrate=float(input("输入年利率:>>"))
interestrate=balance*(interestrate/1200)
print("下月要付的利息为: %.5f" % interestrate)


#6
v0,v1,t=map(float,input('输入初始速度：,输入末速度：,输入占用的时间：').split(','))
a=(v1-v0)/t
print("平均加速度为：%.4f" % a)


#7
S=float(input("输入存款金额:>>"))
one=S *(1+0.00417)
two=(S+one)*(1+0.00417)
theer=(S+two)*(1+0.00417)
four=(S+theer)*(1+0.00417)
five=(S+four)*(1+0.00417)
six=(S+five)*(1+0.00417)
print("六个月后账户里的金额为：%.2f"% six)


#8
num=int(input("请输入一个0-1000的整数:>>"))
a=int(num%100)
b=int(a%10)
c=int(a/10)
d=int(num/100)
sum = b + c +d
print("各位数和为:", sum)
