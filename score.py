Python 3.3.5 (v3.3.5:62cf4e77f785, Mar  9 2014, 10:37:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s3=r'Hello,"Bart"'
>>> print(s3)
Hello,"Bart"
>>> s4=r'''Hello,
Lisa!'''
>>> print(s4)
Hello,
Lisa!
>>> print('包含中文的str')
包含中文的str
>>> s1=72
>>> s2=85
>>> print('小明成绩提升的百分点：%.1f %%' % (s2-s1)/s1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('小明成绩提升的百分点：%.1f %%' % (s2-s1)/s1)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> s1=72
>>> s2=85
>>> print('小明成绩提升的百分点：%.1f %%' % (int(s2)-int(s1))/int(s1))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print('小明成绩提升的百分点：%.1f %%' % (int(s2)-int(s1))/int(s1))
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> s1=72
>>> s2=85
>>> print('小明成绩提升的百分点：%.1f%%' % ((int(s2)-int(s1))/int(s1)*100)
      
