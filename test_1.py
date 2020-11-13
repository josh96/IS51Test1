


"""
The program is determing which payment option earns more money.
The first payment option is 100 dollars per day for 10 days.
The second payment option offers 1 dollar the first day and then 
the amount doubles each day for 10 days. There will be two functions
to determine the pay rate of each option.

function1 will output 100 * 10 days.
function2 will loop 10 times, doubling the amount each time and wil add to the total

if the amount is equal, we output to the user "option 1 and option 2 pays the same"
if the option1 is better, we output to the user "option 1 is better"
if the option2 is better, we output to the user "option 2 is better"
"""

"""
# option1
  return 100 * 10

#option2
 amount = 1
 list1 = []
 loop 10 times
   add amount to list1
   amount *= 2
  return amount
# main
  var1 = option1
  var2 = option2

  if var1 = var2
    "option 1 and option 2 pays the same"
  if var1 < var2
    "option 2 is better"
  else
    "option 1 is better"

main
"""

def option1():
  return 100 * 10

def option2():
  amount = 1
  list1 = []
  for i in range(0,10):
    list1.append(amount)
    amount = 2
   print("list1", list1)
   total = sum(list1)
   return total

   def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    print("from main: var1", var1, "var2", var2)
    if var1 == var2:
      answer = "option 1 and option 2 pay the same"
    if var1 < var2:
      answer = "option 2 is better"
    else:
      answer = "option 1 is better"
    print (answer)

main()
