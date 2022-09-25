
"""
Name        : Frederick Nathanael Thunardi
Last edited : 16/08/22
"""
def counting_sort_int(results):
    """
    Uses a stable counting sort to sort the input nested list based on the
    integer on the second index or in other words, the score.

    :Input:
    results: A nested list with each nested list containing [string (team1), string (team2), int].

    :Output, return or postcondition: returns a sorted nested list based on the integer on the
                                      second index.

    :Time complexity: O(N), where N is len(results)
    :Aux space complexity: O(1 + N), because the max length is always 100, which is constant
                           and because need to allocate N items in the count_array list. 
                           Dominated by O(N)

    :Citation: Week 2 FIT2004 2020sem01 Lecture02 p4 Sorting CountingSort
    """
    # maximum item is set to 100 since the possible integers are[0,.., 100], rather than 
    # going through N items. It's more efficient.
    # variable assignment time complexity is O(1) since it's constant
    # aux space is O(1) since it's constant
    max_item = 100

    # time needed to allocate is O(1), since it's constant
    # aux space is O(1) since it's constant
    # len(count_array) will always be 101 (constant)
    count_array = [None] * (max_item + 1)

    # len(count_array) is always 101
    # time complexity O(1) since the loop runs constant time
    # aux space is O(1) since it creates constant empty list inside each list
    # creating empty list inside each list, so that it could be stable
    for i in range(len(count_array)):
        count_array[i] = []         # O(1) time and aux           
    
    # update count array
    # Time complexity O(N), since it loops N times
    # Aux space O(N), since it needs to allocate N matches to the count_array
    for item in results:
        # index is [-item[2] - 1] so that the 
        # items are ordered in reverse (descending) based on
        # the score in the count_array
        count_array[-item[2] - 1].append(item)  # O(N) time/ aux

    index = 0
    # Time and aux O(1) since it always loops 100 times (constant)
    # Placing back all the items from count array to results in order
    for i in range(len(count_array)):
        # Time complexity O(1) * O(N) = O(N), because the inner loop runs O(N) times
        # Aux space is O(1), since it doesn't create new space
        for j in range(len(count_array[i])):
            results[index] = count_array[i][j]  
            # incrementation
            index += 1                          

    return results                              


def counting_sort_string(result, roster, key, column):
    """
    Uses a stable counting sort to sort the input nested list based on the
    team chosen (team1 or team2), and also the index of the team string.

    :Input:
    result: A nested list with each nested list containing [string (team1), string (team2), int].
    roster: An integer representing the number of possible choices of alphabets to make up a team.
            For example, if roster = 3, then the composition of a team must be made up
            from a variation of {"A", "B", "C"}.
    key   : The index to determine which team will be sorted (either team1 or team2).
    column: The index of the string to determine the column of the strings to be sorted.

    :Output, return or postcondition: returns a sorted nested list based on which team and the column.
                                      For example, if key = 0 and column = 3, it will return a sorted nested
                                      list based on every index 3 (second column) of team1.

    :Time complexity: O(roster + N), where N is len(results) and O(roster) is constant. Dominated by O(N)
    :Aux space complexity: O(roster + N). Dominated by O(N)
    """
    # O(roster) time complexity
    # O(roster) aux space
    # count_array length is set to roster automatically instead of searching
    # through the list since N will be very large and it's more efficient.
    # O(roster) is treated as a constant
    count_array = [None] * (roster)

    # O(roster), because it loops range(rooster) times
    # O(roster) aux space
    # to create empty list inside each list, so that it could be stable
    for i in range(roster):
        count_array[i] = []

    # O(N) time complexity 
    # O(N) aux space, since it needs to store N characters
    for letter in result:
        # filling up items from the input list to the count_array take O(N) steps
        # [ord(letter[key][column]) - 65] is used so that every capital letter can
        # be turned into integer using ord(), starting from the lowest which is "A" to 65-65 = 0
        count_array[ord(letter[key][column]) - 65].append(letter)

    index = 0                                   # O(1) aux and time

    # Placing back all the items from count array to results in order
    for i in range(len(count_array)):           # Time complexity O(roster), and aux O(1) since doesn't require new space
        for j in range(len(count_array[i])):    # Time complexity O(N), to go through N items
            result[index] = count_array[i][j]   # Aux space O(1)
            index += 1                          # O(1) time and aux
            
    return result                               # O(1) time and aux

def radix_sort_string(result, roster, key):
    """
    Uses radix sort to sort the input nested list lexicographically
    based on the team selected (team1 or team2).

    :Input:
    result: A nested list with each nested list containing [string (team1), string (team2), int].
    roster: An integer representing the number of possible choices of alphabets to make up a team.
            For example, if roster = 3, then the composition of a team must be made up
            from a variation of {"A", "B", "C"}.
    key   : The index to determine which team will be sorted (either team1 or team2).

    :Output, return or postcondition: returns a sorted nested list based on which team is selected. For 
                                      example, if the key is 0, then the nested input list will be sorted
                                      lexicographically based on team1.

    :Time complexity: O(M * roster + M * N), where M is the number of characters in a team, N is
                                           len(result), and O(roster) is constant. Dominated by O(M*N)
    :Aux space complexity: O(roster + N), which is dominated by O(N)
    """

    # O(1) time and aux since its len() function and math operations are constant
    # k is len(result[0][0]) - 1 because the radix function sorts from the back
    k = len(result[0][0]) - 1

    # Time complexity O(M)
    # The loop is used to call counting sort M times.
    while k >= 0:
        result = counting_sort_string(result, roster, key, k)   # Time complexity O(M * roster + M*N) because 
                                                                # counting sort is called M times
        k -= 1                                                  # Decrementation so that the column would go eventually to 0 and terminate the loop
    return result                                               # O(1) time and aux

def counting_sort_team(string, roster):
    """
    Uses a stable counting sort to sort the input string into alphabetical 
    order. For example: turns "CAB" to "ABC".

    :Input:
    string: a string which is team1 or team2.
    roster: An integer representing the number of possible choices of alphabets to make up a team.
            For example, if roster = 5, then the composition of a team must be made up
            from a variation of {"A", "B", "C", "D", "E"}.
    :Output, return or postcondition: returns a team with the string composition sorted,
                                      For example: "CCA" will output "ACC"

    :Time complexity: O(roster + M), where M is the number of characters in the string or len(string), 
                      and O(roster) is constant. Dominated by O(M)
    :Aux space complexity: O(roster + M). Dominated by O(M)
    """
    # O(roster) time complexity
    # O(roster) aux space is used
    # Instead of finding the maximum alphabet in the string,
    # it will be more efficient to set the maximum automatically to roster
    count_array = [None] * (roster)

    # O(roster) time complexity
    for i in range(roster): 
        count_array[i] = []

    # O(M) time complexity
    for letter in string:
        # [ord(letter) - 65] is used so that the letters can be turned into integers
        # using ord(). This makes the lowest capital letter "A" to 0, "B" to 1, etc.
        count_array[ord(letter) - 65].append(ord(letter))   # O(M) aux space allocated

    final = ""

    # O(M) time complexity
    for i in range(len(count_array)):
        # O(roster) time complexity because it will enter the loop O(roster) times
        for j in range(len(count_array[i])):
            # Loop through the count_array from the front and concatenate the strings
            final += chr(count_array[i][j])
            
    return final

def remove_duplicate(result):
    """
    Removes all the duplicates from a sorted nested list by using an inplace
    linear algorithm. This is done by using a pointer i and j, by the end of the loop, 
    the first item on the list until the jth item on the list will be unique. 

    :Input:
    result: A nested list with each nested list containing [string (team1), string (team2), int].

    :Output, return or postcondition: returns result which is a sorted nested list without duplicates.

    :Time complexity: O(MN), where N is len(result), and M is the number of characters in a team.
    :Aux space complexity: O(1), since it is inplace.

    :Citation: Week 3 FIT2004 2022sem01 Studio03 Q6 Sorting Application
    """
    i = 0
    j = 0

    # loops O(N) times so that both pointers can go through the list
    for _ in range(len(result) - 1):
        # for each comparison, costs O(M) time complexity to compare the strings
        # the comparison is repeated O(N) times
        # time complexity will be O(M*N)
        if result[j] == result[i+1]:
            i += 1
        else: # result[j] != result[i+1]
            result[j+1], result[i + 1] = result[i+1], result[j+1] # performs a swap between result[j+1] and result[i + 1]
            i += 1
            j += 1
    return result[:j + 1]       # returns a unique sorted list up to index j

def binary_search(result, score):
    """
    Search a target score inside the sorted result nested list using a modified binary search.
    If score is not found in the list, it will take the next biggest item instead, but if there
    is none, then will return an empty list. It will also return all the elements with the targeted score,
    not only one of the elements with equal targeted score.

    :Input:
    result: A sorted nested list with each nested list containing [string (team1), string (team2), int].
    score : A target score.

    :Output, return or postcondition: Returns a nested list containing matches with the same score
                                      as the target score. But, if the target score is not found, 
                                      then it will return matches with the next biggest score. But,
                                      if there is no socre bigger than the target, and the target is not
                                      found, it will return an empty list. 

    :Time complexity: O(N + log N), where N is len(result). Dominated by O(N)
    :Aux space complexity: O(N), worst case if all the items in the list contains equal scores
    """

    # variables assingment
    low = 0                     # used to determine the lower index area of the binary search
    high = len(result) - 1      # used to determine the higher index area of the binary search
    mid_point = 0               # used to determine the middle index area of the binary search
    not_found = True            # not_found = False -> the target score is not found within the list
    res = []                    # res for the final answer

    if score > result[0][2]:    # to check if the score is bigger than the biggest possible score in the list 
                                # because the list is sorted
        return res              # if it is bigger, then return an empty list. This will reduce the best case time complexity.
                                # which is when the target score is > than the biggest score on the list
    
    # O(log N) time complexity since the loop runs log N times.
    while low <= high:    
        
        # mid point is the median index between low and high
        mid_point = (high + low) // 2
 
        # if the score of result[mid_point] is bigger than the target:
        if result[mid_point][2] > score:
            # ignore the left side of the binary search area and
            # move the lower index to be mid_point + 1
            low = mid_point + 1
 
        # if the score of result[mid_point] is smaller than the target:
        elif result[mid_point][2] < score:
            # ignore the right side of the binary search area and
            # move the higher index to be mid_point - 1
            high = mid_point - 1
 
        # if the score is found at result[mid_point][2]
        else: 
            # this loop is to check continously to the left of the item if there is any duplicate
            # if no duplicate is found, it will stop the loop
            # For example: [['AAA', 'AAA', 90], ['AAC', 'AAE', 65], ['BBB', 'CCC', 65], ['CCC', 'CDE', 65], ['CEE', 'CAA, 10]]
            # if the target score is 65, the mid_point will land on the second index
            # then it will loop until the index become 1, since ['AAC', 'AAE', 65] is the leftmost item with the same score as target
            # O(N) time complexity
            while mid_point > 0 and result[mid_point][2] == result[mid_point - 1][2]:
                mid_point -= 1
            
            # append the left most match with the target score to the final answer
            res.append(result[mid_point])

            # after the left most match with the same score is found, now the second loop will loop to the right until
            # no more match with the same score is found
            # For example: [['AAA', 'AAA', 90], ['AAC', 'AAE', 65], ['BBB', 'CCC', 65], ['CCC', 'CDE', 65], ['CEE', 'CAA', 10]]
            # After looping to the left until index is one, it will loop to the right until index is 3, which is ['CCC', 'CDE', 65]
            # It will append the matches one by one as it loops.
            # so the final ans will be [['AAC', 'AAE', 65], ['BBB', 'CCC', 65], ['CCC', 'CDE', 65]]
            # O(N) time complexity worst case when all the items in the list has the same score
            while mid_point < len(result) -1 and result[mid_point][2] == result[mid_point + 1][2]:
                # iterator to keep going right
                mid_point += 1
                res.append(result[mid_point])

            # means that a match with the target score is found
            not_found = False
            
            # exits the while loop so that it stops after entering the else statement
            break
    
    # a scenario where there is no match with the target score in the nested list
    # if this happens, the code takes the match with the next biggest score
    # which is the high index
    if not_found:
        # same idea as the loop on the else statement, the difference is it takes the high index instead of mid_point.
        # For exaple: [['AAA', 'AAA', 90], ['AAC', 'AAE', 65], ['BBB', 'CCC', 65], ['CCC', 'CDE', 65], ['CEE', 'CAA', 10]]
        # if the target score is 63, the high index will land on index 3, the loop will loop through until its 1 which is ['AAC', 'AAE', 65]
        while high > 0 and result[high][2] == result[high - 1][2]:
            high -= 1
        
        # append the far most left item in the list with the closest big score from the target
        res.append(result[high])

        # loop to the right until it reaches index 3
        # final answer will be ['AAC', 'AAE', 65], ['BBB', 'CCC', 65], ['CCC', 'CDE', 65]
        while high < len(result) -1 and result[high][2] == result[high + 1][2]:
                high += 1
                res.append(result[high])
                
    return res
    
def compliment(result):
    """
    Returns a nested list containing the orginal version and the compliment version
    of the elements inside the list. For example, the compliment version of ["ABC", "BCC", 60]
    is ["BCC", "ABC", 100-60 = 40]. This is done by appending the compliment version inside the original
    list.

    :Input:
    result: A nested list with each nested list containing [string (team1), string (team2), int].

    :Output, return or postcondition: returns a nested list containing the original version of the
                                      elements of the nested list, and the compliment versions. For example,
                                      an input list of [['AAA', 'AAA', 65], ['BBB', 'CCC', 65]] will return
                                      [['AAA', 'AAA', 65], ['BBB', 'CCC', 65], ['AAA', 'AAA', 35], 
                                      ['CCC', 'BBB', 35]].

    :Time complexity: O(MN), where N is len(result), and where M is the length of characters in a team.
    :Aux space complexity: O(MN).
    """

    # O(N) time because it loops N times
    for index in range(len(result)):
        # O(N) * O(M) time complexity 
        # needs O(N) aux space for the new empty lists for the compliment version
        # need O(M)* O(N) aux space for the strings of the compliment version
        result.append([result[index][1], result[index][0], 100 - result[index][2]])  
    return result


def analyze(results, roster, score):
    """
    Sorts an input list of ['string'(team1 with capital letters), 'string'(team2 with capital letters), 'integer' (0-100)]
    based on the integer, team1, and finally team2 on the priority level. This function uses both radix and counting sort.
    The string of each team are also ordered: For example "CBA" will be "ABC". Duplicates are also removed from the input.
    Function also accepts a target score which will print out a match with the same/ closest score from the target score.
    Main purpose of this function is to process the data gathered from a video game called Diablo Immortal Gacha so that it is organized.

    :Input:
    result: A nested list with each nested list containing [string (team1), string (team2), int].
    roster: An integer representing the number of possible choices of alphabets to make up a team.
            For example, if roster = 5, then the composition of a team must be made up
            from a variation of {"A", "B", "C", "D", "E"}.
    score : a target score to find in the nested list

    :Output, return or postcondition: Returns the top 10 matches in the sorted nested list without duplicates 
                                      in the order of score, team1, team2, as priority with each teams alphabetically
                                      ordered. It also return matches with the same score as the target, 
                                      or the next biggest score if the target is not on the nested list.
                                      
    :Time complexity: O(MN + N + log N), where N is len(result), and M is the number of characters in a team. 
                      Dominated by O(MN), since O(N) > O(log N) and O(MN) > O(N).
    :Aux space complexity: O(MN), since the function with the maximum aux space is O(MN), therefore
                           the maximum extra space needed/ aux space is O(MN).
    """
    # to go through each match and order the team1 and team2 composition
    # for example: "EDE" to "DEE"
    # Time complexity O(N)
    for i in range(len(results)):
        # Time complexity O(N) * O(2M) which is O(MN) because it runs N times and is called 2 times per iteration
        # Aux space is O(M) since it's needed for the counting_sort_team() function
        results[i][0], results[i][1] = counting_sort_team(results[i][0], roster), counting_sort_team(results[i][1], roster)

    # mutate the input list so that it could have all the compliment version of each match in the nested list
    # O(MN) time 
    # O(MN) aux space
    results =  compliment(results)

    # sorts the nested list lexicographically based on team2 using radix sort.
    # O(MN) time complexity
    # O(N) aux space needed for the function
    results = radix_sort_string(results, roster, 1)

    # sorts the nested list lexicographically based on team1 using radix sort.
    # O(MN) time complexity
    # O(N) aux space needed for the function
    results = radix_sort_string(results, roster, 0)

    # sorts the nested list based on the score of each match.
    # O(N) time complexity
    # O(N) aux space needed for the function
    results = counting_sort_int(results)

    # removes all the duplicates in the sorted nested list
    # O(MN) time complexity
    # O(1) aux space
    results = remove_duplicate(results)
    
    # performs a modified binary search to the sorted input list to find the target score
    # O(N + log N) time complexity
    # O(N) aux space
    target = binary_search(results, score)

    # if there is more than 10 matches in the final list, then only return the top 10
    if len(results) > 10:
        return [results[:10], target]
    # if there is less than or equal to ten matches in the list, return list
    return [results, target]

