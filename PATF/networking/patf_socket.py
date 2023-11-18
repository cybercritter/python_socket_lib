import socket
import struct
from ipaddress import IPv4Address


class PATFSocket:
    def __init__(self,
                 address: str, port: int,
                 multicast=False,
                 family=socket.AF_INET,
                 sock_type=socket.SOCK_DGRAM) -> None:

        """
        Initializes the PATFSocket object.

        Args:
            address (str): The IP address of the server.
            port (int): The port number for communication.
            multicast (bool): Determines if the socket is multicast or unicast. Default is False.
            family: The type of address, IPv4 or IPv6. Default is socket.AF_INET.
            sock_type: The type of socket to be created. Default is socket.SOCK_DGRAM.

        Returns:
            None
        """
        self._sock = self.create_multicast_socket() if multicast else socket.socket(family, sock_type)
        self._address = IPv4Address(address)
        self._port = port
        self._family = family
        self._sock_type = sock_type


    @property
    def multicast_group(self):
        """
        Returns the multicast group if the address is multicast, otherwise returns None.

        Returns:
            tuple or None: The multicast group as a tuple of (address, port) if the address is multicast, otherwise None.
        """
        return (str(self._address), self._port) if self._address.is_multicast else None

    def bind(self) -> None:
        """
        Binds the socket to the multicast group if the address is multicast.

        Returns:
            None
        """
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.multicast_group:
            self._sock.bind(self.multicast_group)

    def connect(self):
        """
        Placeholder method for connecting the socket.

        Returns:
            None
        """
        pass

    def close(self):
        """
        Closes the socket.

        Returns:
            None
        """
        self._sock.close()

    def send(self, snd_data) -> int:
        """
        Sends data to the multicast group.

        Args:
            snd_data: Data to be sent to the socket.

        Returns:
            int: The number of bytes sent.
        """
        return self._sock.sendto(snd_data, self.multicast_group) if self.multicast_group else 0

    def create_multicast_socket(self, timeout: float = 0.2) -> socket.socket:
        """
        Creates a socket for multicast communication.

        Args:
            timeout (float): Set the timeout for the socket. Default is 0.2.

        Returns:
            socket.socket or None: A socket object if the address is multicast, otherwise None.
        """
        if not self._address.is_multicast:
            return None
        try:
            sock = socket.socket(family=self._family, type=self._sock_type)
            sock.settimeout(timeout)
            ttl = struct.pack('b', 1)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
            return sock
        except IOError as error:
            print(f"Failed to create multicast socket: {error}")
            return None
