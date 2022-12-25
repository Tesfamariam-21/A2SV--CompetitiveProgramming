# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    testCase = int(input())
    possible = []
    
    
    for _ in range(testCase):
        numOfCubes = int(input())
        sideLengths = list(map(int, input().split()))

        size = len(sideLengths)
        leftPointer = 0
        rightPointer = size - 1
        prev = sideLengths[leftPointer]if sideLengths[leftPointer] > sideLengths[rightPointer]else sideLengths[rightPointer]
        
        while(leftPointer <= rightPointer):
            if(leftPointer == rightPointer):
                print('Yes')
                break

            if(sideLengths[leftPointer] <= prev 
            and sideLengths[leftPointer] >= sideLengths[rightPointer]):
                prev = sideLengths[leftPointer]
                leftPointer += 1
            elif(sideLengths[rightPointer] <= prev
            and sideLengths[leftPointer] < sideLengths[rightPointer]):
                prev = sideLengths[rightPointer]
                rightPointer -= 1
            else:
                print('No')
                break
    
