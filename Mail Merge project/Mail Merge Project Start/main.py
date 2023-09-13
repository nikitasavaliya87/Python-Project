#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name=[]
file=open("C:\\python\\Angelia\\Day_24_Mail Merge project\\Mail Merge Project Start\\Input\\Names\\invited_names.txt")
name=file.readlines()
print(name)

f2=open("Angelia\Day_24_Mail Merge project\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode="r")
txt=f2.read()
print(txt)
x=len(name)
for l in range(0,x):
    c=txt.replace("[name]",name[l].strip("\n"))
    filename="letter_for_"+name[l].strip("\n")+".txt"
    with open(f"C:\python\Angelia\Day_24_Mail Merge project\Mail Merge Project Start\Output\ReadyToSend\{filename}", mode="w") as new_file:
        new_file.write(c)



    # print(filename)
# for lines in file:
#     name=file.readlines()
# #name=file.readline(12)
   
