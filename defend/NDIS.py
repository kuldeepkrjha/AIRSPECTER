import time

# Simulate a function to check if the incoming connection is legitimate or suspicious
def is_connection_suspicious(source_ip, destination_ip):
    # Implement your logic to check for suspicious patterns in the network traffic
    # For this demonstration, we'll assume any connection from an external IP is suspicious
    return not destination_ip.startswith('192.168.')

# Function to generate an alert and take action when suspicious activity is detected
def generate_alert(source_ip, destination_ip):
    print(f"ALERT: Suspicious connection detected from {source_ip} to {destination_ip}")
    # Implement actions to block the suspicious connection or take other mitigating steps
    # For this demonstration, we'll simply print the alert message.

# Simulate network traffic and monitor connections
def monitor_network_traffic():
    while True:
        # Replace the following with real-time network traffic data
        # For this demonstration, we'll use some sample data
        incoming_connections = [
            {'source_ip': '203.0.113.45', 'destination_ip': '192.168.1.10'},
            {'source_ip': '8.8.8.8', 'destination_ip': '192.168.1.10'},
            {'source_ip': '192.168.1.20', 'destination_ip': '192.168.1.10'},
        ]

        for connection in incoming_connections:
            source_ip = connection['source_ip']
            destination_ip = connection['destination_ip']
            
            if is_connection_suspicious(source_ip, destination_ip):
                generate_alert(source_ip, destination_ip)
                # Add actions to block the suspicious connection or take other mitigating steps
                # For this demonstration, we'll assume the connection is blocked.
                print(f"INFO: Blocking the suspicious connection from {source_ip} to {destination_ip}")

        # Simulate real-time monitoring by adding a delay
        time.sleep(5)

if __name__ == "__main__":
    monitor_network_traffic()
