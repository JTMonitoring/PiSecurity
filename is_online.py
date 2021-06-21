from pythonping import ping
from chores import mytts

def is_online(address):
    results = ping(address, size=2)
    if len(results) > 1:
        mytts("Internet is reachable", "en")

# is_online("google.com")

