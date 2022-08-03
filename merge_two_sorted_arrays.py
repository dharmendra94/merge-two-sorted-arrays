import re
import sys


def mergeSortedArrays(arr1: list[int], arr2: list[int]) -> list[int]:
    arr1Length = len(arr1)
    arr2Length = len(arr2)
    result = [None] * (arr1Length + arr2Length)

    i = 0
    j = 0
    k = 0
    while i < arr1Length and j < arr2Length:
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            result[k] = arr2[j]
            k = k + 1
            j = j + 1

    while i < arr1Length:
        result[k] = arr1[i]
        k = k + 1
        i = i + 1

    while j < arr2Length:
        result[k] = arr2[j]
        k = k + 1
        j = j + 1

    return result


def parseCommandLineArgs(input: str) -> tuple[list, list]:
    regex = r'(?<=\[).+?(?=\])'
    searchStr = ''.join(input)
    result = re.findall(regex, searchStr)

    # Should throw an error if user sends command line args of length not equal to 2
    if (len(result) != 2):
        print("""
            Please pass in valid arguments like $function_name [1,2,3] [2,3,6]
        """)

    try:
        sortedArr1 = list(map(int, result[0].split(",")))
        sortedArr2 = list(map(int, result[1].split(",")))
    except:
        print(
            f"""
                Invalid input: Failed to parse the input into list of integers
                Inputs passed: Array1: {result[0]} Array2: {result[1]}
            """
        )
        raise

    return (sortedArr1, sortedArr2)


def main():
    try:
        commandLineArgs = sys.argv[1:]
        listsToMerge = parseCommandLineArgs(commandLineArgs)

        if (len(listsToMerge) == 2):
            mergedArray = mergeSortedArrays(listsToMerge[0], listsToMerge[1])
            print(mergedArray)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
