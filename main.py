#!/usr/bin/python3
"""Summary
"""

from PATF.networking.patf_socket import PATFSocket as psock


if __name__ == '__main__':
    print("create a new socket")
    message = b'very import message'

    try:
        new_sock = psock(address="192.168.1.1", port=10000)
    except NotImplementedError as e:
        print(f"{e}")

    new_sock.bind()

    while True:
        try:
            bytes_sent = new_sock.send(message)
        except NotImplementedError as e:
            print(f"{e}")

    new_sock.close()
