# student who score max marks
grades = {"Amit": 85, "Riya": 92, "Karan": 78, "Neha": 88}

# method1
grades = {"Amit": 85, "Riya": 92, "Karan": 78, "Neha": 88}
marks_list = []
for student in grades:
    print(grades[student])
    marks_list.append(grades[student])
print(marks_list)
print(max(marks_list))
for student in grades:
    if (grades[student]) == max(marks_list):
        print(student)

# method2:
# find student with highest mark
max_marks = max(grades.values())
print(max_marks)

for student in grades:
    if (grades[student]) == max_marks:
        print(student)

# class average
# method1:
grades = {"Amit": 85, "Riya": 92, "Karan": 78, "Neha": 88}
marks_list=[]
for student in grades:
    # print(student)
    # print(grades[student])
    marks = grades[student]
    marks_list.append(marks)
    
print(marks_list)
avg = sum(marks_list)/len(marks_list)
print(avg)

# method2:
# claculate class average
grades = {"Amit": 85, "Riya": 92, "Karan": 78, "Neha": 88}
marks_sum = sum(grades.values())
no_marks = len(grades)

average = marks_sum / no_marks
print(f"average is : {average}")


# word frequency 

sentence = "apple banana apple orange banana apple"
sentence_split = sentence.split()
print(sentence_split)
wf = {}
for word in sentence_split:
    if word in wf:
        wf[word] = wf[word] + 1
    else:
        wf[word] = 1
        
print(wf)        
        
    