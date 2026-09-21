class resullt:
    name="karthik"
    rollno="05"
    sub1=20
    sub2=35
    sub3=25
    def calculate(self):
        total_marks=self.sub1+self.sub2+self.sub3
        print(total_marks)
    def average(self):
            average=(total_marks)/100
            print(average)
    def grade(self):
    if total_marks>90:
        print("grade A")
    else if total_marks>=75:
        print("grade B")
    else if total_marks>60:
        print("grade C")
    else if total_marks<59:
        print("fail")

