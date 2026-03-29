# Created the age check function to verify age
def check_age():
    first_attempt = True
    while True:
        try:
            if first_attempt:
                age = int(input("Enter age: "))
                first_attempt = False
            else:
                age = int(input("Re-enter age: "))
                
            if age <= 0:
                print("Invalid age. Must be positive.")
            else:
                return age
        except ValueError:
            if first_attempt:
                print("Invalid age. Must be a number.")
                first_attempt = False
            else:
                print("Invalid age. Must be a number.")

# Created the age heigh function to verify height
def check_height():
    first_attempt = True
    while True:
        try:
            if first_attempt:
                height = float(input("Enter height in inches: "))
                first_attempt = False
            else:
                height = float(input("Re-enter height in inches: "))
                
            if height <= 0:
                print("Invalid inches value. Must be positive.")
            else:
                return height
        except ValueError:
            if first_attempt:
                print("Invalid inches value. Must be a number.")
                first_attempt = False
            else:
                print("Invalid inches value. Must be a number.")

# Created the age weight function to verify weight
def check_weight():
    first_attempt = True
    while True:
        try:
            if first_attempt:
                weight = float(input("Enter weight in pounds: "))
                first_attempt = False
            else:
                weight = float(input("Re-enter weight in pounds: "))
                
            if weight <= 0:
                print("Invalid pounds value. Must be positive.")
            else:
                return weight
        except ValueError:
            if first_attempt:
                print("Invalid pounds value. Must be a number.")
                first_attempt = False
            else:
                print("Invalid pounds value. Must be a number.")

# Calculate BMI and Fat Burning Heart Rate 
def calculate_BMI_Fat(age, height, weight):
    BMI = round(((weight * 703) / (height ** 2)), 1)
    Fat_Burn = round(((220 - age) * 70/100), 1)
    
    print()
    print(f"Age = {age}")
    print(f"Height = {height}\"")
    print(f"Weight = {weight} pounds")
    print()
    print(f"Fat Burning Heart Rate = {Fat_Burn} bpm")
    print(f"Body Mass Index = {BMI}")
    
    return BMI, Fat_Burn

# Function to create a new file
def create_file():
    filename = input("Enter the name of the file you would like to create: ")
    try:
        print(f"File '{filename}' created successfully!")
        return filename
    except Exception as e:
        print(f"Error creating file: {e}")
        return None

# Function to open existing file for appending
def open_file():
    filename = input("Enter the name of the file to open: ")
    try:
        # Check if file exists
        with open(filename, 'r') as file:
            pass
        print(f"File '{filename}' opened successfully!")
        return filename
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

# Function to read and display results from file
def read_file():
    filename = input("Enter the name of the file to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n" + content)
        return True
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False
    except Exception as e:
        print(f"Error reading file: {e}")
        return False

# Function to append results to file
def append_to_file(filename, BMI, Fat_Burn):
    
    try:
        with open(filename, 'a') as file:
            file.write(f"FBHR: {Fat_Burn} - BMI: {BMI}")
        print("Results added to file.")
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False

# Main function that handles file operations and calculations
def main():
    print("Welcome to the Weber State University Human Performance Lab!")
    print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI.")
    print("The program will also store this information in a file you choose so that it can be tracked over time.\n")
    
    filename = None
    
    while True:
        print("\nSelect:")
        print("1. Create a file")
        print("2. Open a file to add results to")
        print("3. Read results from file")
        print("4. Exit program")
        
        choice = input()
        
        if choice == "1":
            filename = create_file()
            if filename:
                # After creating file, get measurements and add to file
                print("\nPlease enter your measurements:")
                age = check_age()
                height = check_height()
                weight = check_weight()
                BMI, Fat_Burn = calculate_BMI_Fat(age, height, weight)
                append_to_file(filename, BMI, Fat_Burn)
            else:
                print("Failed to create file. Please try again.")
                
        elif choice == "2":
            filename = open_file()
            if filename:
                # After opening file, get measurements and add to file
                print("\nPlease enter your measurements:")
                age = check_age()
                height = check_height()
                weight = check_weight()
                BMI, Fat_Burn = calculate_BMI_Fat(age, height, weight)
                append_to_file(filename, BMI, Fat_Burn)
            else:
                print("Failed to open file. Please try again.")
                
        elif choice == "3":
            read_file()
            
        elif choice == "4":
            print("Thank you for using the Human Performance Lab calculator!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
    
# Run the program
if __name__ == "__main__":
    main()