# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 03
 ----------------------------
  Partner 1:  Dylan Regan
  Partner 2: Hunter Prather
  Date: 09/15/2024
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Be sure to comment your code well.
        * Not too much but enough to explain what you are doing.
        * Comment each block of code above it
        * Put comments to the right of individual statements only if they are unclear
    3. Use descriptive variable names
    4. Put any import statements at the top of the code.
    5. To get full credit: Your output must match the example - same number of digits, decimals, spacing, wording etc.  Note the extra lines between the title and results.
      
"""

# Put any import statements here, they may or may not be needed



# get user input
print("Wind Chill Warning & Clothing Selector Program\n")
temp = eval(input("Temperature (F): "))
wind_speed = eval(input("Wind speed (mph): "))

# determine if valid
valid = True

if (wind_speed < 3):
    print("\n{:.1f} mph too low. Wind Chill cannot be calculated.".format(wind_speed))
    valid = False
    if (temp < -15):
        print("{:.1f}F too cold. You are going to freeze, stay inside.".format(temp))
        
elif (wind_speed > 70):
    print("\n{:.1f} mph too high. You will get blown over, stay inside.".format(wind_speed))
    valid = False
    if (temp < -15):
        print("{:.1f}F too cold. You are going to freeze, stay inside.".format(temp))
        
elif (temp < -15):
    print("\n{:.1f}F too cold. You are going to freeze, stay inside.".format(temp))
    valid = False

# determine wind chill warning
wc_warning = ""

if (temp < -40):
    wc_warning = "Extreme"
elif (temp < -20):
    wc_warning = "Intermediate"
elif (temp < 0):
    wc_warning = "Caution"
elif (temp < 32):
    wc_warning = "Minimal"
else:
    wc_warning = "None"

# calculate wind chill
wc = 35.74 + (0.6215 * temp) - (35.75 *(wind_speed ** 0.16)) + (0.4275 * (temp * (wind_speed ** 0.16)))

# determine reccomended clothing
clothing = ""

if (wc < -20):
    clothing = "Wear a Parka and insulated pants"
elif (wc < -5):
    clothing = "Weear a parka and long underwear"
elif (wc < 10):
    clothing = "Wear a parka and heavy pants"
elif (wc < 30):
    clothing = "Wear a coat, hat and heavy pants"
elif (wc < 50):
    clothing = "Wear a jacket and hat"
elif (wc < 70):
    clothing = "Wear a pants and shirt"
elif (wc < 90):
    clothing = "Wear a shorts and t-shirt"
else:
    clothing = "Stay inside if with the A/C"

# display results
if (valid):
    print("\nWind Chill is {:.1f} with a warning of {}\nYou should {}".format(wc, wc_warning, clothing))
    

