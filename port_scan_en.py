from termcolor import colored
import socket

def fanc1():
    color_a = colored("[+] ", 'green')
    print("~"*50)
    host = input(color_a + "Host --> ")
    port = int(input(color_a + "Port --> "))
    print("~"*50)

    scan = socket.socket()

    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    try:
        scan.connect((host, port))
    except socket.error:
        print(color_b + "Port -- ", port, " -- [CLOSED]")
    else:
        print(color_c + "Port -- ", port, " -- [OPEN]")

def fanc2():
    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    host = input(color_a + "Host --> ")
    print("\n")
    port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80]

    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(color_b + "Port -- ", i, " -- [CLOSED]")
        else:
            print(color_c + "Port -- ", i, " -- [OPEN]")

print("~"*50)

print("\t[1] --- scan specific port")
print("\t[2] --- scan list of ports")

print("~"*50, "\n")
text_a = input("[scan]--> ")

if text_a == "1":
    fanc1()
elif text_a == "2":
    fanc2()
else:
    print(colored("Invalid", 'red'))
