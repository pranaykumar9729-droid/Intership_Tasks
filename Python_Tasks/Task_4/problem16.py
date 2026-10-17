problem : Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    grades = []
    for student in students:
        grades.append(student[1])
        
    uni_grades = set(grades)
    sort_grades = sorted(uni_grades)
    sec_grades = sort_grades[1]
    
    names = []
    for student in students:
        if sec_grades == student[1]:
            names.append(student[0])
            
    for name in sorted(names):
        print(name)
    
    
    
    
        
        
            

    
        
        
