#task 1 on file creation
with open("my_file.txt", mode='w', encoding="utf-8")as file:
    file.write("welcome and lets navigate together\n")
    file.write("count: 1235\n")
    file.write("Thankyou for navigating\n")
# open in read mode
with open("my_file.txt", mode='r', encoding="utf-8") as file:
text = file.read()
print(text)
#appending 
with open("my_file.txt", mode='a', encoding="utf-8") as file:
    file.write("Feel free to ask any question.\n")
    file.write("Always available to serve you 24/7.\n")
    file.write("Youn always welcomed.\n")
#error handling
try:
    with open("my_file.txt", mode='w', encoding="utf-8") as file:
        file.write("welcome and lets navigate together\n")
        file.write("count: 1235\n")
        file.write("Thankyou for navigating\n")
except:FileNotFoundError:
    print("File is missing.")
finally:
    print("Execution completed.")
