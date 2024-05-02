from pyndn import Name, Face, Interest
from pyndn.security import KeyChain

# Create a Face instance to communicate with NDN network
face = Face()

# Create a KeyChain for signing and verifying packets
keychain = KeyChain()

# Define a callback for processing incoming data packets
def onData(interest, data):
    print("Received data packet with name:", data.getName().toUri())
    print("Content:", data.getContent().toRawStr())

# Register the onData callback for incoming data packets
face.setInterestFilter("/test/example", onData)  # Use a simple test NDN name

# Create an Interest packet to fetch data from the network
interest = Interest(Name("/test/example"))
face.expressInterest(interest)

# Process incoming packets in the event loop
try:
    while True:
        face.processEvents()
        # Add other processing or wait actions here
except KeyboardInterrupt:
    print("Interrupted, shutting down")
    face.shutdown()
