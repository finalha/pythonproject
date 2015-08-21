__author__ = '16101210-15'
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score =score

    def printscore(self):
        print('%s : %s' % self.name,self.score)

'''
    if __name__ == '__main()__':
        lily = Student('lily','100')
        lily.printscore();
'''

