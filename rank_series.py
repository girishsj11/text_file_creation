import text_file_creation
text_file_creation.creation(text_file_creation.student_count,text_file_creation.total_subjects)
all_marks = list()

def sum_of_marks():
    with open('out.txt','a+') as i_file:
        with open('in.txt','r') as o_file:
            o_lines = o_file.readlines()
            for o_line in o_lines:
                o_data = o_line.split(',')
                sum,o_line_data = 0,''
                for i in range(1,len(o_data)-1):
                    sum+=int(o_data[i])
                for i in range(0,len(o_data)-1):
                    o_line_data+=o_data[i]+','
                all_marks.append(sum)
                i_file.write(o_line_data+'total_marks:'+str(sum)+','+'\n')

def ranking_system():
    with open('out.txt','r+') as file:
        lines = file.readlines()
        with open('out.txt','w') as f:
            for line in lines:
                data_line = line.split(',')
                total_score = int(((data_line[len(data_line) - 2]).split(':'))[1])
                final_data= ''
                for i in range(0, len(data_line) - 1):
                    final_data += data_line[i]+','
                ranking = all_marks.index(total_score)+1
                f.write(final_data+'Rank:'+str(ranking)+'\n')



if __name__ == "__main__":
    sum_of_marks()
    all_marks = set(all_marks)
    all_marks = list(all_marks)
    all_marks.sort(reverse=True)
    print("\n Marks list without duplicate on sorted order out of {} : ".format((100*text_file_creation.total_subjects)), all_marks)
    ranking_system()