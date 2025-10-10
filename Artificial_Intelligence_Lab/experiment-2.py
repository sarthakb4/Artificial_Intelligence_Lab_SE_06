print("Welcome to career expert systems")
print("Choose your favourite subjects from Physics, Maths, Programming,Circuits,Statisitics,Biology,AIconcepts,Chemistry")
#interest=input("Enter your two interests seperated by commas(Ex : Maths,Physics)").split(,)
sub1=input("Enter your first subject : ")
sub2=input("Enter your second subject : ")
if((sub1=='Maths' and sub2=='Physics') or (sub1=='Physics' and sub2=='Maths' )):
	print("Suggested path : Mechanical engineering")
elif((sub1=='Programming' and sub2==Maths) or (sub1=='Maths' and sub2=='Programming ')):
	print("Suggested path : Computer engineering")
elif((sub1=='Chemistry' and sub2=='Biology') or (sub1=='Biology' and sub2=='Chemistry' )):
	print("Suggested path : Mechanical engineering")
elif((sub1=='Maths' and sub2=='Circuits') or (sub1=='Circuits' and sub2=='Maths' )):
	print("Suggested path : Mechanical engineering")
elif((sub1=='Programming' and sub2=='Statistics') or (sub1=='Statistics' and sub2=='Programming' )):
	print("Suggested path : Mechanical engineering")
elif((sub1=='Programming' and sub2=='AIconcepts') or (sub1=='AIconcepts' and sub2=='Programming' )):
	print("Suggested path : Mechanical engineering")
else:
	print("Enter valid input")
