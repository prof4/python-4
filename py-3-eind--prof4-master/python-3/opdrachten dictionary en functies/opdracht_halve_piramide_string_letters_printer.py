def printen_van_letters(string):
  aantal = len(string) +1
  for x in range(aantal):
      print(string[x-1:x]* x)


string = input("wat is uw zin of woord: ")
printen_van_letters(string)
