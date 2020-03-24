# Age-Calculator-App
This app can calculate how old you are. It is very simple to make.
First you need a Entry for type your Birth Year
Second you need a Button for calculate your Age.
############################
Here is a Blueprint of Age Calculator App
current_year = date.today().year
birth_year = int(entry.get())
calculate = (current_year-birth_year)
print(calculate)
