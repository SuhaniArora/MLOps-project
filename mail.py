import smtplib
import urllib.request as urllib
# Senders email
sender_email = "arorasuhani1511@gmail.com"
# Receivers email
rec_email = "arorasuhani1511@gmail.com"

message = "Best Modelcreated..."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("arorasuhani1511@gmail.com", "Password")
print("Login Success!")
# Send Email
server.sendmail("Suhani Arora", "arorasuhani1511@gmail.com", message)