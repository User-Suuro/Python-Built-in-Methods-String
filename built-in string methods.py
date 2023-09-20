#string methods
#not included cuz idontknowhow2use: encode(), format_map(), isascii(),
#subdivided to -> manipulation, verificaton, positioning, managing whitespaces, scanning, managing data types, string to array, translation and transition

#string method - manipulation
print("myexample".capitalize()) #converts first char to upper
print("MyExample".lower()) #converts all string to low
print("myEXAMPLE".casefold()) #converts all string to low (even other languages such as german), it is more aggressive than lower(),
print("for example, this is an example".title()) #Converts the first character of each word to upper case
print("my EXAMPLE".swapcase()) #Make the lower case letters upper case and the upper case letters lower case
print("\n")

#string method - verification/string checker
print("helloworld".islower()) #returns True if all string is in lower case
print("MYEXAMPLE".isupper()) #returns True if all string are uppercase
print("  ".isspace()) #returns True if all string are whitespace
print("This Is My Title".istitle()) #returns True if all words starts with upper case

print("myexample".endswith("e")) #returns True of sp]=]]\ecified end string matched
print("myexample".startswith("m")) #returns True of specified first string matched
print("this is not \n printable".isprintable()) #Check if all the characters in the text are printable

print("\n")
#string method - positioning
print("myexample".center(20  , "X")) #centers string, width is the needed string lenght to be extended, while _fillchar the char the fills spaces
print("myexample".rjust(20, "X")) #	Returns a right justified version of the string
print("myexample".ljust(20, "X")) #	Returns a left justified version of the string
print("myexample".zfill(15)) # adds zeros (0) at the beginning of the string, until it reaches the specified length


print("\n")
#string method - managing whitespaces
print("     myexample      ".lstrip()) #it removes any leading whitespaces
print("     myexample      ".rstrip()) #it removes any last whitespaces
print("     my example      ".strip()) #removes any to first and last of the whitespaces tring
print("H\tE\tL\tL\tO".expandtabs(2)) #sets the tab size to the specified number of whitespaces
print("\n")

#string method - scanning
print("for example, this is my example".count("example"))# returns number of times a specified value appears in string
print("what a example position is the example word?".find("example"))# returns nearest postition where it was found (starts with 0)
print("what a example position is the example word and example?".rfind("example"))# returns farthest postition where it was found (starts with 0)
print("this is similar to find do not return -1".index("")) #almost same as find, but find returns -1 if value not found while in index throws an error
print("this is similar to find do not return -1".index("")) #almost same as rfind, but find returns -1 if value not found while in index throws an error
print("I like bananas".replace("bananas", "apples")) #Returns a string where a specified value is replaced with a specified value
print("this is the{price: .2f} price tag, and hotdog is {price_2}".format(price = 50, price_2 = "ubos na")) #format specified value in string

print("\n")

#string method - managing data types
print("specialcharactersandspacesarenotallowed123".isalnum()) #returns True if all in string are alphanumeric (e.g. a-z and 0-9), chars such as !#spaces are not alphanum
print("12345notallowed".isalpha()) #returns True if all in string are alphabets (e.g. a-z), char such as !#spaces are not alpha
print("hello_world".isidentifier()) #similar to isalnum() but also return True for underscores(_)
print("1232456".isdecimal()) #returns True if string represent numbers (e.g. 0-9)
print("1232456".isdigit()) #similar to isdecimal but also returns true for exponents (e.g. 2**3)
print("1232456".isnumeric()) #similar to isdecimal but also returns true for exponents and numerals (e.g. ½, etc.)

print("\n")

#string method - string to array conversion
print("I could eat all bananas all day".partition("all"))  #Returns a tuple where the first string is parted into three parts
print("I could eat all bananas all day".rpartition("all")) #Returns a tuple where the last string is parted into three parts
print("I could eat all bananas all day".split()) # Split a string into a list where each word is a list item
print("I could, eat all bananas, all day".rsplit(",")) # Split a string into a list using a keyword
print("I could eat all \n bananas all day".splitlines()) # Split a string into a list based on each line
print([*"AEIOU"])

print("\n")

#maketrans and translate
txt = "A B C D"
myVar = txt.maketrans("C", "P") #make it to dict first, or make the translation to ascii code
print(myVar) #67 means C in ascci code and 80 means P in ascci code
print(txt.translate(myVar)) #then translate





