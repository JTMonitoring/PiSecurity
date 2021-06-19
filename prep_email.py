import smtplib, ssl

def send_email(result):
	#read data from config.txt and store in variables
	file = open("src/config.txt", "r")
	lines = file.readlines()
	smtp_server = lines[0]
	port = lines[1]
	sender_email = lines[2]
	password = lines[3]
	receiver_email = lines[4]

	#decrypt sender, password, recip
	sender_email = fernet.decrypt(sender_email).decode()
	password = fernet.decrypt(password).decode()
	receiver_email = fernet.decrypt(receiver_email).decrypt()
	
	print("Building email...")
	# port = 465  # For SSL
	# smtp_server = "smtp.gmail.com"
	# sender_email = "testcamping000@gmail.com"  # Sender Email. if you change this you have to use gmail, and enable less secure apps
	# receiver_email = ""  # add User IP
	# password = "Password!?"

	print("SMTP Server: "+smtp_server)
	print("Port: "+port)
	print("Sender Email: "+sender_email.decode("utf-8"))
	print("Recipient Email: "+receiver_email.decode("utf-8"))
	# print password as *
	pass_len = len(password)
	for i in range(0, pass_len):
		stars = ""
		stars +=str("*")
	print("Password: "+stars)





	message = """\
	Subject: Camera Status

	IP : Status\n"""

	# message = "Subject: Cam Update\nBody: IP  :  Status\n"
	for key in result.keys():
		message += key
		message += "  :  "
		message += str(result[key])
		message += "\n"

	# # message = str(result)
	print(message)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
		print("Sending email...")

