if __name__ == '__main__':
    listOFStudents = []
    secondLowestGrade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record = [name, score]
        listOFStudents.append(record)
        
    listOFStudents.sort(key=lambda x: x[1])
    
    secondLowestGrade.append(listOFStudents[1])
    for i in range(2,len(listOFStudents)):
        if secondLowestGrade[0][1] == listOFStudents[i][1]:
            secondLowestGrade.append(listOFStudents[i]) 
    # print(listOFStudents)
    secondLowestGrade.sort()
    for i in range(len(secondLowestGrade)):
        print(secondLowestGrade[i][0])
    
