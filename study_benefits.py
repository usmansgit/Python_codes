inp_benefits = input("Enter the amount of the study benefits: ")
inp_benefits = float(inp_benefits)
percentage = ((1.17 / 100)*inp_benefits)
benefits = inp_benefits + percentage
scnd_percent = ((1.17 / 100)*benefits)
scnd_benifit = benefits + scnd_percent
print("If the index raise is 1.17 percent, the study benefit,"
"\nafter a raise, would be" ,benefits, "euros"
"\nand if there was another index raise, the study"
"\nbenefits would be as much as",scnd_benifit, "euros")
