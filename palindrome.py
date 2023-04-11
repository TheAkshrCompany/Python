
string = input("Enter a string ")
anotherString = string[::-1] #reversing the string
if anotherString == string:
	print("Yes, its a palindrome")
else:
	print("No, its not a palindrome")
