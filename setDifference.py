englishStudents = int(input())
englishStudentsSet = set(map(int, input().split()))
frenchStudents = int(input())
frenchStudentsSet = set(map(int, input().split()))

onlyEnglish = englishStudentsSet.difference(frenchStudentsSet)

print(len(onlyEnglish))
