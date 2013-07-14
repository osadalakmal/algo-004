"""This file implements a quick sort algorithm"""
import sys
import copy

def getPivot(start,end):
    """ Return the pivot point of a given array"""
    return int((start + end)/2)

def inplace_qsort(input,start,end):
    """sorts a given array in "input" and changes the array inplace"""
    if (start == end):
        return
    i = start + 1
    pivotIndex = start
    pivot = input[pivotIndex]
    for j in range(i,end + 1):
        if input[j] < pivot:
            temp = input[j]
            input[j] = input[i]
            input[i] = temp
            i += 1
    temp = input[i-1]
    input[i-1] = pivot
    input[pivotIndex] = temp
    if (i-2 >= start):
        inplace_qsort(input,start,i-2)
    if (i <= end):
        inplace_qsort(input,i,end)

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
        inplace_qsort(array,0,len(array)-1)
        result = array
    for num in result:
        print(num)

if __name__ == "__main__":
    main()