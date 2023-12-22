import socket
import struct
from ipaddress import IPv4Address


class PATFSocket:
    """
    This class provides the ability to create specialized
    sockets for the PATF library
    """
    def __init__(self,
                 multicast_group=("0.0.0.0", -1),
                 family=socket.AF_INET,
                 sock_type=socket.SOCK_DGRAM):
        self.multicast_group = multicast_group
        self.is_multicast = IPv4Address(self.multicast_group[0]).is_multicast
        self._family = family
        self._sock_type = sock_type

        self._sock = self.create_multicast_socket() if self.is_multicast else socket.socket(family, sock_type)

    def bind(self):
        """
        The bind function is used to associate the socket with a specific network interface and port number.
        The bind function takes two arguments: an IP address and a port number. The IP address can be either
        an IPv4 or IPv6 address, or it can be set to INADDR_ANY to indicate that the server should listen on all
        available interfaces. The port number is an integer value in the range 1-65535.

        :param self: Allow an object to refer to itself inside of the class
        :return: Nothing
        """
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.multicast_group:
            self._sock.bind(self.multicast_group[0])

    def connect(self):
        """
        Placeholder method for connecting the socket.

        Returns:
            None
        """
        pass

    def close(self):
        """
        The close function closes the socket connection.


        :param self: Represent the instance of the class
        :return: Nothing
        """
        self._sock.close()

    def send(self, snd_data):
        """
        The send function sends data to the multicast group.


        :param self: Represent the instance of the class
        :param snd_data: Send data to the multicast group
        :return: The number of bytes sent
        """
        return self._sock.sendto(snd_data, self.multicast_group) if self.multicast_group else 0

    def create_multicast_socket(self, timeout: float = 0.2):
        """
        The create_multicast_socket function creates a socket for multicast communication.

        :param self: Refer to the current instance of a class
        :param timeout: float: Set the timeout for the socket
        :return: A socket
        """
        if not self.is_multicast:
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
