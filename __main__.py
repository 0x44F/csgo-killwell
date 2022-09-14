# CS:GO KillWell version 4.2
# Authors: 0x44F & sand
# Description: Send instructions to CS:GO server allowing bots to target specific player

import socket, ipaddress, sys #, csgo # Will later implement CS:GO library (next update)

PAYLOAD_FIRST   = "\x56\x41\x4C\x56\x45\x5F\x53\x45\x52\x56\x45\x52\x3A\x43\x4F\x4E\x4E\x45\x43\x54\x49\x4F\x4E\x43\x4C\x49\x45\x4E\x54\x28" # Don't touch this
PAYLOAD_SECOND  = "\x29\x3A\x42\x4F\x54\x53\x5F\x41\x54\x54\x41\x43\x4B\x5F\x50\x52\x4F\x54\x4F\x54\x59\x50\x45\x5F\x30\x30\x30\x34" # Or this.

def encode_payload(steam_id: str):
    print("Encoding payload with steam ID...")
    return PAYLOAD_FIRST + steam_id + PAYLOAD_SECOND

def run_exploit(ip, s_id, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect((ip, port))
    
        sock.send(encode_payload(s_id).encode())
        sock.close()
    except:
        return False        
    
    return True

def main():
    print("CS:GO KillWell ver4.2 | [Updated 9/13/2022]\r\n")
    if len(sys.argv) != 3:
        quit("Usage: %s <server_ip> <steam_id>" % sys.argv[0])
    
    target_id = sys.argv[2]
    
    if len(target_id) < 17:
        quit("Failed to parse: %s, please enter a valid id..." % target_id)     # Check for STEAM ID length validity
    
    try:
        server_ip = ipaddress.ipaddress(sys.argv[1])     # Validate IP
    except ValueError:
        quit("Failed to validate server IP: %s, please enter a valid ip..." % _server_ip)
    except:
        quit("General error occurred, usage: %s <server_ip> <steam_id>" % sys.argv[0])
    
    if not run_exploit(server_ip, target_id, 27015):    # Hardcoded port for use on official servers only. you can change this.
        print("Exploit failed to run properly!")
        exit(-1)
    
    print("Ran exploit...")
    exit(1)
    
if __name__ == '__main__':
    main()
