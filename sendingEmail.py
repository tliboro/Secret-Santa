#Sending email to respondents
import smtplib
import getpass

def send(users, users_email, santas_name):

	#Could add more conditions s.a. try/catchs
	email = getpass.getpass(prompt="Please enter sending email: ")
	pw = getpass.getpass(prompt="Please enter password: ")

	INTRO = "Thank you for being a part of Secret Santa " 
	DECLARATION = " You will be the secret santa to "
	PRICE = "The price limit is set at a MINIMUM OF $30. "
	#REMINDER = "Remember with all the holiday deals coming up you could potentially purchase something a lot more expensive while meeting the limit. "
	KNOWLEDGE = "I am unable to trace this email and am unaware who has who (please don't ask); therefore, please text me when you receive this email. "
	#RULES = "Lastly, please do not ask any of the members involved for any advice to ensure secrecy. "
	DATE = "\n\nWe will exchange gifts with the tentative date of Tuesday, December 25th! Furthermore, do not write your name on the gift because it's also the receiver's job to try to guess who was their secret santa! "
	THANKS = "\n\n Love y'all fam,\nSanta Tyty :)"

	for x in range(len(users)):
		SUBJECT = "Family Secret Santa!"

		TEXT = INTRO + users[x] + "!" + DECLARATION + santas_name[x] + "." + "\n\n" + PRICE + "\n\n" + KNOWLEDGE + DATE + THANKS
		
		content = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()

		mail.starttls()

		mail.login(email, pw)
		mail.sendmail(email, users_email[x], content )

		mail.close()

	print("Email(s) have been sent. ")