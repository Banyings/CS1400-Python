dkey = 0
while True:
    try:
        print("Please enter the key used to decrypt the file")
        dkey = int(input())
        break
    except ValueError:
        print("Please enter a number.")
        print("Please try again.")

while True:
    try:
        print("Please enter the file you would like to decrypt")
        fileName = input()

        # attempt to open the file to read from it
        f = open(fileName, "r")

        # create a file to write the decrypted text
        decryptedFile = open("decrypted.txt", "w") 

        for line in f:
            for i in range(len(line)):
                # Getting each character in the string
                letter = line[i]
                # getting the value of the letter
                chValue = ord(letter)
                # Subtracting the decryption key
                chValue -= dkey
                # Converting value back to letter
                letter = chr(chValue)
                # Writing to the file
                decryptedFile.write(letter)
        break
    except FileNotFoundError:
        print("File does not exist. Please enter the correct file name.")
    except Exception as e:
        print(f"Error occurred: {e}")

print("File was decrypted to decrypted.txt")

# Close the files
f.close()
decryptedFile.close()