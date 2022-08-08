#Write a Python program to accept a filename from the user and print the extension of that
fname=(input("Input the filename:"))
f_extension=fname.split(".")
print("The extension on the file is:" +repr(f_extension[-1]))
