try:
    sum = 0
    #open the numbers.txt file
    numbersFile = open('challenges/numbers.txt', 'r', encoding='utf-8-sig')  # Add encoding parameter

    #complete the for loop to continue reading so long as the file has more values
    for n in numbersFile:
        #complete the num statement below to store the next int in the file into num
        #remember by default the number will come from the file as a string and need to be converted to an int
        num = int(n.strip())
        #this line prints out the num to make sure it is working
        print(num)
        #this line of code sums up all the numbers
        sum += num

    #displays the sum of the numbers
    print(f"\nThe sum of all numbers is: {sum}")

    #close the file
    numbersFile.close()

except Exception as err:
    print(err)