def  recursaoNoSet(set, subSet):
    """
    Uses recursion to evaluate each subset of a set and adds them to a matrix.

    Parameters:
    set (list): A list of numeric values with no repetitions.
    subSet (list of lists): The subsets of the original set.

    Returns:
    list of lists: The matrix containing all subsets, excluding the empty subset.
    """
    if len(set) >= 1:
        for i in set:
            copia_set = set[:]
            copia_set.remove(i)
            recursaoNoSet(copia_set, subSet)
            if set not in subSet:
                subSet.append(set)

    return subSet

def getSubSets(set, subSet):
    """
    Receives a set and returns all its subsets.

    Parameters:
    set (list): A list of numeric values with no repetitions.
    subSet (list of lists): The subsets of the original set.

    Returns:
    list of lists: A matrix containing all subsets of the set.
    """

    subSetFinal = recursaoNoSet(set, subSet)
    subSetFinal.append([])

    return subSetFinal

def main():
    """
   The function below performs the following operations:
    - Receives an input and converts it into a list
    - Calls the getSubSets function, which:
        - Iterates over each element
        - Creates a copy of the original set
        - Removes the current element from the copy
        - Recursively calls itself
        - Adds the resulting subset to the matrix if it's not already present
        - Adds the empty subset
        - Returns the matrix of subsets
    - Sorts the matrix based on the length of each subset
    - Prints the matrix
    """
    print("Enter your set by typing its elements separated by spaces. Its subsets will be returned.")
    print("Exemple: 1 2 3 4")
    entrada = input("Set: ")
    set = list(map(int, entrada.split()))
    subSet = getSubSets(set, [])
    subSetSorted = sorted(subSet, key=lambda x: len(x), reverse=True)
    print(subSetSorted)
    return 0

if __name__ == "__main__":
    main()