student_count = int(input("Enter the total number of students, which you wanted to store in a text file : "))
total_subjects = int(input("Enter the total number of subjects which each students have attended & obtained marks : "))


def creation(student_count,total_subjects):
    with open('in.txt','a+') as o_file:
        for i in range(1,student_count+1):
            name = str(input("Enter the {} name of student : ".format(i)))
            o_file.write(str(i) + '-' + name + ',')
            for x in range(1,total_subjects+1):
                subject = int(input("Enter the {} subject marks which {} obtained out of 100 : ".format(x,name)))
                o_file.write(str(subject)+',')
            o_file.write('\n')



if __name__ == "__main__" :
    creation(student_count,total_subjects)
