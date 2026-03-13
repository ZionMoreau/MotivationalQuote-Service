import random
import zmq

port = 5002
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://*:{port}")

print(f"Motivational Quote Service running on port {port} ")

quotes = [

]

while True:
    request = socket.recv_string()
    if request == "Motivational Quote":
        selectedQuote = random.choice(quotes)
        socket.send_string(selectedQuote)
    else:
        response = "Error"
        socket.send_string(response)