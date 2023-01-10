from flask import Flask
import socket


app = Flask(__name__)

@app.route('/')
# Function to display hostname and IP address
def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print("Hostname : ", host_name)
		print("IP : ", host_ip)
	except:
		print("Unable to get Hostname and IP")
		
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0",debug=True)
