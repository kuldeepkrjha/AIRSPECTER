#!/bin/bash

# Function to check if an IP address is in the target list
check_ip() {
    local ip="$1"
    for target_ip in "${TARGET_IPS[@]}"; do
        if [ "$ip" == "$target_ip" ]; then
            return 0
        fi
    done
    return 1
}

# Read user input for the IP addresses text file
read -p "Enter the path to the IP addresses text file (separated by comma): " IP_FILE
IFS=',' read -ra TARGET_IPS <<< "$(cat "$IP_FILE")"

# Intrusion detection flags
FLAG_THRESHOLD=5  # Number of allowed violations before alert
FLAG_INTERVAL=10  # Time interval in seconds for resetting flags

# Initialize intrusion detection counters and timestamp
FLAG_COUNTER=0
LAST_ALERT=0

# Run the script in the background
while true; do
    CURRENT_TIME=$(date +%s)
    if [ "$((CURRENT_TIME - LAST_ALERT))" -ge "$FLAG_INTERVAL" ]; then
        # Replace "INTRUSION_IP" with the actual intrusion IP address
        if check_ip "INTRUSION_IP"; then
            FLAG_COUNTER=$((FLAG_COUNTER + 1))
            if [ "$FLAG_COUNTER" -ge "$FLAG_THRESHOLD" ]; then
                # Generate alert notification using notify-send
                notify-send "Intrusion Detected, we should start device encryption" "More than $FLAG_THRESHOLD violations."
                LAST_ALERT=$CURRENT_TIME
                FLAG_COUNTER=0  # Reset the counter
            fi
        else
            FLAG_COUNTER=0  # Reset the counter if IP is not in the list
        fi
    fi
    sleep 1  # Wait for 1 second before checking again
done &
