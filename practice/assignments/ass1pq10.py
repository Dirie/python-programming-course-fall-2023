
sugar = 1.5/48
floower = 2.75/48
buter = 1/48

number_of_cookies = int(input("Enter number of cookies that you want to make: "))
required_sugar = sugar * number_of_cookies
required_floower = floower * number_of_cookies
required_buter = buter * number_of_cookies

print("To make " + str(number_of_cookies) + " cookies, you need the following ingredients: \nsugar: " + str(required_sugar) + "\nfloower: " + str(required_floower) + "\nbuter: " + str(required_buter) )
