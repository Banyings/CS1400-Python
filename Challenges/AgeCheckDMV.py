print("Welcome to DMV")
print("PLease use thus progtam to determine if you can apply for a driver's licencse")

while True:
    try:
        age = int(input("What is your age :")) 
        # force a number greater than zero
        if age <= 0:
            raise TypeError("Enter a number greater than zero.")
        break
    except ValueError:
        print("Invalid input. Please enter your age in numeric format.")
    except TypeError as e:
        print(e)
    except:
        print("Invalid input")

if age < 15:
    print("You can't apply.")
elif age == 15:
    print("You can apply for a permit and driver's license education courses.")
elif age > 15:
    print("You can aplly for a driver's license")