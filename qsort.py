"""This file implements a quick sort algorithm"""
import sys

def getPivot(array,start,end):
    return array[int((start + end)/2)]

def easy_qsort(input,start,end,result):
    if (start == end):
        return
    lessIndex = start;
    moreIndex = end;
    pivotIndex = getPivot(input,start,end)
    pivot = input[pivotIndex]
    for index in range(start,end+1):
        if (index == pivotIndex):
            continue
        if(input[index] < pivot):
            result[lessIndex] = input[index]
            lessIndex += 1
        else:
            result[moreIndex] = input[index]
            moreIndex -= 1
    result[lessIndex] = pivot
    if(lessIndex > 1):
        easy_qsort(result,start,lessIndex-1,result)
    if (moreIndex > 1):
        easy_qsort(result,moreIndex+1,end,result)


def main():
    if (len(sys.argv) < 2):
        sys.stderr.write('Please enter a valid file name to read array from\n')
        exit
    array = []
    with open(sys.argv[1],'r') as f:
        for line in f.readlines():
            array.append(int(line))
    result = [None] * len(array)
    if (sys.argv[2] == "easy"):
        easy_qsort(array,0,len(array)-1,result)
    for num in result:
        print(num)

if __name__ == "__main__":
    main()