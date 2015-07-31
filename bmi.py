#height = 1.83
#weight =95
#bmi = weight/(height*height)
ht = input("请输入您的身高(单位：米)：")
wt = input("请输入您的体重(单位：公斤):")
ht = float(ht)
wt = float(wt)
bmi = wt/(ht**2)
print("bmi = %.2f" % bmi)
if bmi < 18.5:
	print("过轻")
elif bmi < 25 or bmi == 25:
    print("正常")	
elif bmi < 28 or bmi == 28:
	print("过重")
elif bmi < 32 or bmi == 32:
	print("肥胖")
else:
	print("严重肥胖")