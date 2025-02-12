def check_packet_size():
    packet_size = int(input("Enter the packet size in bytes: "))
    print((packet_size <= 1337 and "False - Packet To Small!") or (packet_size >= 2600 and "True - Packet Meets Requirements!"))
                      
check_packet_size()

# Sources
# The Week 3 ToolDev Walkthrough
