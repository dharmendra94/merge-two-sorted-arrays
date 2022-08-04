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


def parseCommandLineArgs(input: str) -> tuple[list[int], list[int]]:
    # Regular expression to find the content groups between square brackets
    regex = r'\[(.*?)\]'
    result = re.findall(regex, ''.join(input))

    # Should throw an error if user sends command line args of length not equal to 2
    if (len(result) != 2):
        print("""
            Please pass in valid arguments like $function_name [1,2,3] [2,3,6]
        """)

    try:
        parseInt = lambda item: list(map(int, item.split(",")) if item != '' else [])
        sortedArr1, sortedArr2 = map(parseInt, result)
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
    
        commandLineArgs = sys.argv[1:]
        listsToMerge = parseCommandLineArgs(commandLineArgs)

        if (len(listsToMerge) == 2):
            mergedArray = mergeSortedArrays(listsToMerge[0], listsToMerge[1])
            print(mergedArray)
    


if __name__ == "__main__":
    main()
