#!/usr/bin/python3
"""Summary
"""

from PATF.networking.patf_socket import PATFSocket


if __name__ == '__main__':
    print("create a new socket")
    message = b'very import message'
    runLoop = True
    try:
        new_sock = PATFSocket(("192.168.1.1", 10000))
        new_sock.bind()

        while runLoop:
            try:
                bytes_sent = new_sock.send(message)
            except NotImplementedError as e:
                print(f"{e}")

        new_sock.close()

    except NotImplementedError as e:
        print(f"{e}")
