#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter the temperature in Fahenheit: "))

  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = round((tempF-32)* 5/9, 1)

  #Output converted temperature.
  
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
