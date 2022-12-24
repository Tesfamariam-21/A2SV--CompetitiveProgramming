
def aver(zipped, subjects, numOfStudents):
    av= []
    for i in range(numOfStudents):
        av.append(sum(zipped[i])/subjects)
    return av

    
if __name__ == "__main__":
    numOfStundents, subjects = map(int, input().split())
    
    score =[]
    for i in range(subjects):
        score.append(list(map(float, input().split())))
        
    ziped = zip(*score)    
    av = aver(list(ziped), subjects, numOfStundents)
    
    for i in range(len(av)):
        print(av[i])
    
