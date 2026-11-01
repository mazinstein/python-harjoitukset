seasons = ("winter", "spring", "summer", "autumn")

def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return  seasons[0]
    elif month == 3 or month == 4 or month == 5:
        return  seasons[1]
    elif  month == 6 or month == 7 or month == 8:
        return seasons[2]
    elif month == 9 or month == 10 or month == 11:
        return seasons[3]
    else:
        return "Error"



user_input = int(input("Enter month number: "))
print(get_season(user_input))