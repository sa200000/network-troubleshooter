import os
import socket

# Step 1: Ping Google to check internet connectivity
def ping_test():
    # Ping Google's server (8.8.8.8) 4 times
    response = os.system("ping -n 4 8.8.8.8" if os.name == 'nt' else "ping -c 4 8.8.8.8")
    if response == 0:
        print("✅ Internet is working (ping successful)!")
    else:
        print("❌ No internet connection (ping failed).")

# Step 2: Check if DNS works (e.g., resolve "google.com")
def dns_check():
    try:
        # Get the IP address of "google.com"
        ip = socket.gethostbyname("google.com")
        print(f"✅ DNS is working! google.com resolves to {ip}.")
    except:
        print("❌ DNS failed. Can't resolve website addresses.")

# Run both tests
print("\n--- Running Network Tests ---")
ping_test()
dns_check()
print("-----------------------------")
