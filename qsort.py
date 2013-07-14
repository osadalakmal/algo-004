"""This file implements a quick sort algorithm"""
import sys
import copy

def getMedian(num1, num2, num3):
    if (num1 < num2):
        if (num2 < num3):
            return num2
        elif num1 < num3:
            return num3
        else:
            return num1
    else:
        if (num3 > num1):
            return num1
        elif (num3 > num2):
            return num3
        else:
            return num2

def getPivot(start, end,pivotPos):
    """ Return the pivot point of a given array"""
    return {
        "start" : lambda start, end: start,
        "end" : lambda start, end: end,
        "med" : lambda start, end: getMedian(start, end, int((start + end + 1)/2)),
    }.get(pivotPos)(start=start, end=end)

def inplace_qsort(input, start, end, pivotPos):
    """sorts a given array in "input" and changes the array inplace"""
    if (start == end):
        return 0
    comp = (end - start)
    pivotIndex = getPivot(start, end, pivotPos)
    pivot = input[pivotIndex]
    i = start
    for j in range(i,end + 1):
        if (j == pivotIndex):
            continue
        elif input[j] < pivot:
            temp = input[j]
            input[j] = input[i]
            input[i] = temp
            i += 1
    temp = input[i]
    input[i] = pivot
    input[pivotIndex] = temp
    if (pivotPos == "start"):
        if (i-2 > start):
            comp += inplace_qsort(input, start, i-2, pivotPos)
        if (i <= end):
            comp += inplace_qsort(input, i, end, pivotPos)
    elif (pivotPos == "end"):
        if (i > start):
            comp += inplace_qsort(input, start, (i-1), pivotPos)
        if (i < end):
            comp += inplace_qsort(input, (i+1), end, pivotPos)
    return comp

def easy_qsort(input,start,end,result):
    """This routine sorts the input array in "input" list and stores the
       result in "result" array."""
    if (start == end):
        return
    lessIndex = start;
    moreIndex = end;
    pivotIndex = getPivot(start,end)
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
    temp_input = copy.copy(result)
    if(lessIndex > 1 and lessIndex > start):
        easy_qsort(temp_input,start,lessIndex-1,result)
    if (moreIndex < end):
        easy_qsort(temp_input,moreIndex+1,end,result)


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
    else:
        comp = inplace_qsort(array, 0, len(array)-1, sys.argv[2])
        result = array
    print("number of comparisons is %d" % (comp))
    for num in result:
        print(num)

if __name__ == "__main__":
    main()