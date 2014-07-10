class base:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        base.count+=1
        print " init base: %s" %self.name

    def tell(self):
        print "Name:%s" ", Age:%s" %(self.name,self.age)


class teacher(base):
    count=0
    def __init__(self,name,age,salary):
        base.__init__(self,name,age)
        self.salary=salary
        print "init Teacher: %s" %self.name
        teacher.count+=1
    def tell(self):
        base.tell(self)
        print "Salary: %d" %self.salary
        print "total number of teachers %d" %self.count


class stud(base):
    count=0
    def __init__(self,name,age,mark):
        base.__init__(self,name,age)
        self.mark=mark
        stud.count+=1
    def tell(self):
        base.tell(self)
        print "mark: %d" %self.mark
        print "total number of students %d" %self.count






t1=teacher("abc",20,200)
t2=teacher("me",24,5000)

s1=stud("mm1",15,99)
s2=stud("mm2",20,100)
s3=stud("mm3", 18,70)

office=[t1,t2]
classroom=[t1,s1,s2,s3]

office[0].tell()
office[1].tell()

classroom[0].tell()
classroom[1].tell()
classroom[2].tell()
classroom[3].tell()

