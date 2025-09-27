try:
    result= 10/0
except ZeroDivisionError:
    print("Error, tried to divide by 0.")

    try:
        text_to_int = int(text)
    except Exception as e:
        print("an error happened",e)

try:
    result= 10/2
except ZeroDivisionError:
    print("Error, tried to divide by 0.")
else:
    print("Division successful. Result:", result)


