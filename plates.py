def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
#Check the lenght of the plate
  if len(s)<2 or len(s)>6:
        return(False)
#Check if the first 2 characters are letters
  if s[0].isalpha()==False:
      return(False)
  if s[1].isalpha()==False:
      return(False)
#check if there are only letters and number, no other characters
  for elem in s:
      if elem.isalpha()==False and elem.isdigit()==False:
          return(False)
#Create the objects needed after to verify the numbers
  number=False
  firstnumberindex=0
#finding the first number in the string and its index
  for i in range (len(s)):
      if s[i].isdigit()==True:
          number=True
          firstnumberindex=i
          break
#if number in the plate, check if the first one isnt "0"
  if number==True:
      if s[firstnumberindex]=="0":
          return(False)
#And that there is no letters between first  number and the end
      for i in range((firstnumberindex),(len(s))):
          if s[i].isalpha()==True:
              return(False)
#if none of the rules are broken , then it returns "True"
  return(True)
main()
# to verify : check50 cs50/problems/2022/python/plates

