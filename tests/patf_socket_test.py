import pytest
import socket
from PATF.networking.patf_socket import PATFSocket

# Constants for testing
VALID_IP = "224.0.0.1"
VALID_PORT = 5004
INVALID_IP = "999.999.999.999"
INVALID_PORT = -1

#
# @pytest.mark.parametrize("address, port, multicast, family, sock_type, expected_group", [
#     # ID: Test-Happy-Path-1
#     (VALID_IP, VALID_PORT, True, socket.AF_INET, socket.SOCK_DGRAM, (VALID_IP, VALID_PORT)),
#     # ID: Test-Happy-Path-2
#     ("239.255.255.250", 1900, True, socket.AF_INET, socket.SOCK_DGRAM, ("239.255.255.250", 1900)),
# ])
# def test_patf_socket_init_happy_path(address, port, multicast, family, sock_type, expected_group, mocker):
#     # Arrange
#     mocker.patch('socket.socket')
#
#     # Act
#     patf_socket = PATFSocket(address, port, multicast, family, sock_type)
#
#     # Assert
#     assert str(patf_socket._address) == expected_group[0]
#     assert patf_socket._port == expected_group[1]
#     if multicast:
#         assert patf_socket._multicast_group == expected_group
#
#
# @pytest.mark.parametrize("address, port, multicast, family, sock_type, exception", [
#     # ID: Test-Edge-Case-Invalid-IP
#     (INVALID_IP, VALID_PORT, False, socket.AF_INET, socket.SOCK_DGRAM, ValueError),
#     # ID: Test-Edge-Case-Invalid-Port
#     (VALID_IP, INVALID_PORT, False, socket.AF_INET, socket.SOCK_DGRAM, OverflowError),
# ])
# def test_patf_socket_init_edge_cases(address, port, multicast, family, sock_type, exception):
#     # Act & Assert`
#     with pytest.raises(exception):
#         PATFSocket(address, port, multicast, family, sock_type)
#
#
# @pytest.mark.parametrize("address, port, multicast, family, sock_type, error, mocker_method, mocker_args", [
#     # ID: Test-Error-Case-Socket-Creation-Failure
#     (VALID_IP, VALID_PORT, True, socket.AF_INET, socket.SOCK_DGRAM, IOError, 'socket.socket', {'side_effect': IOError}),
# ])
# def test_patf_socket_init_error_cases(address, port, multicast, family, sock_type, error, mocker_method, mocker_args, mocker):
#     # Arrange
#     mocker.patch(mocker_method, **mocker_args)
#
#     # Act & Assert
#     with pytest.raises(error):
#         PATFSocket(address, port, multicast, family, sock_type)


# @pytest.mark.parametrize("address, port, multicast, family, sock_type, snd_data, expected_bytes", [
#     # ID: Test-Happy-Path-Send-1
#     (VALID_IP, VALID_PORT, True, socket.AF_INET, socket.SOCK_DGRAM, b"Test Data", len(b"Test Data")),
#     # ID: Test-Happy-Path-Send-2
#     (VALID_IP, VALID_PORT, True, socket.AF_INET, socket.SOCK_DGRAM, b"", 0),
# ])
# def test_patf_socket_send_happy_path(address, port, multicast, family, sock_type, snd_data, expected_bytes, mocker):
#     # Arrange
#     mocker.patch('socket.socket')
#     patf_socket = PATFSocket(address, port, multicast, family, sock_type)
#     mocker.patch.object(patf_socket._sock, 'sendto', return_value=expected_bytes)
#
#     # Act
#     bytes_sent = patf_socket.send(snd_data)
#
#     # Assert
#     assert bytes_sent == expected_bytes
#     patf_socket._sock.sendto.assert_called_with(snd_data, patf_socket._multicast_group)
#
#
# @pytest.mark.parametrize("address, port, multicast, family, sock_type, snd_data, exception", [
#     # ID: Test-Error-Case-Send-Failure
#     (VALID_IP, VALID_PORT, True, socket.AF_INET, socket.SOCK_DGRAM, b"Test Data", socket.error),
# ])
# def test_patf_socket_send_error_cases(address, port, multicast, family, sock_type, snd_data, exception, mocker):
#     # Arrange
#     mocker.patch('socket.socket')
#     patf_socket = PATFSocket(address, port, multicast, family, sock_type)
#     mocker.patch.object(patf_socket._sock, 'sendto', side_effect=exception)
#
#     # Act & Assert
#     with pytest.raises(exception):
#         patf_socket.send(snd_data)


def test_create_multicast_socket():

    """
    The test_create_multicast_socket function tests the create_multicast_socket function in PATFSocket.
    It does this by creating a new PATFSocket object and then calling the create_multicast_socket function on it.
    If the socket is created successfully, then it will not be None.

    :return: A socket object
    """
    new_sock_obj = PATFSocket(("227.1.1.1", 10000))
    sock = new_sock_obj.create_multicast_socket()
    assert sock is not None