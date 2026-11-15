"""
Endianness Conversion Algorithm

This module implements endianness (byte order) conversion utilities for converting
between big-endian and little-endian representations of multi-byte integers.

Endianness refers to the order of bytes in a multi-byte data type:
- Big-endian: Most significant byte first (e.g., 0x12345678 → [0x12, 0x34, 0x56, 0x78])
- Little-endian: Least significant byte first
  (e.g., 0x12345678 → [0x78, 0x56, 0x34, 0x12])

Common uses:
- Network protocols (TCP/IP uses big-endian for multi-byte fields)
- File format parsing (PNG, JPEG headers specify endianness)
- Cryptographic algorithms (MD5 uses little-endian, SHA-256 uses big-endian)
- Binary data serialization (Protocol Buffers, MessagePack)
- Hardware interfacing (ARM is bi-endian, x86 is strictly little-endian)
- Cross-platform data exchange

Real-world examples:
- IP addresses are transmitted in big-endian (network byte order)
- Modern ARM and x86 processors typically operate in little-endian mode
- Java class files use big-endian format
- Bitcoin uses little-endian for block hashes
- USB and PCI protocols use little-endian

References:
- https://en.wikipedia.org/wiki/Endianness
- RFC 1700 (Network Byte Order)
- https://tools.ietf.org/html/rfc1700
"""

def swap_endianness_16(value: int) -> int:
    """Swap the byte order of a 16-bit integer.

    Args:
        value: 16-bit integer (0 to 65,535)

    Returns:
        Integer with swapped byte order

    Raises:
        ValueError: If value is negative or exceeds 16-bit range"""
    if value < 0 or value > 65535:
        msg = f'value must be between 0 and {65535}'
        raise ValueError(msg)
    return (value & 255) << 8 | (value & 65280) >> 8

def swap_endianness_32(value: int) -> int:
    """Swap the byte order of a 32-bit integer.

    Args:
        value: 32-bit integer (0 to 4,294,967,295)

    Returns:
        Integer with swapped byte order

    Raises:
        ValueError: If value is negative or exceeds 32-bit range"""
    if value < 0 or value > 4294967295:
        msg = f'value must be between 0 and {4294967295}'
        raise ValueError(msg)
    return (value & 255) << 24 | (value & 65280) << 8 | (value & 16711680) >> 8 | (value & 4278190080) >> 24

def swap_endianness_64(value: int) -> int:
    """Swap the byte order of a 64-bit integer.

    Args:
        value: 64-bit integer (0 to 18,446,744,073,709,551,615)

    Returns:
        Integer with swapped byte order

    Raises:
        ValueError: If value is negative or exceeds 64-bit range"""
    if value < 0 or value > 18446744073709551615:
        msg = f'value must be between 0 and {18446744073709551615}'
        raise ValueError(msg)
    return (value & 255) << 56 | (value & 65280) << 40 | (value & 16711680) << 24 | (value & 4278190080) << 8 | (value & 1095216660480) >> 8 | (value & 280375465082880) >> 24 | (value & 71776119061217280) >> 40 | (value & 18374686479671623680) >> 56

def bytes_to_int_little(data: bytes) -> int:
    """Convert bytes to integer using little-endian byte order.

    Args:
        data: Byte sequence to convert (1-8 bytes)

    Returns:
        Integer representation in little-endian order

    Raises:
        TypeError: If data is not bytes
        ValueError: If data is empty or exceeds 8 bytes"""
    if not data or len(data) > 8:
        msg = 'data must be between 1 and 8 bytes'
        raise ValueError(msg)
    return int.from_bytes(data, byteorder='little')

def bytes_to_int_big(data: bytes) -> int:
    """Convert bytes to integer using big-endian byte order.

    Args:
        data: Byte sequence to convert (1-8 bytes)

    Returns:
        Integer representation in big-endian order

    Raises:
        TypeError: If data is not bytes
        ValueError: If data is empty or exceeds 8 bytes"""
    if not data or len(data) > 8:
        msg = 'data must be between 1 and 8 bytes'
        raise ValueError(msg)
    return int.from_bytes(data, byteorder='big')

def int_to_bytes_little(value: int, num_bytes: int) -> bytes:
    """Convert integer to bytes using little-endian byte order.

    Args:
        value: Integer to convert (non-negative)
        num_bytes: Number of bytes in output (1-8)

    Returns:
        Bytes representation in little-endian order

    Raises:
        ValueError: If value is negative, num_bytes invalid, or value too large"""
    if value < 0:
        msg = 'value must be non-negative'
        raise ValueError(msg)
    if num_bytes < 1 or num_bytes > 8:
        msg = 'num_bytes must be between 1 and 8'
        raise ValueError(msg)
    if value >= 1 << num_bytes * 8:
        msg = f'value {value} too large for {num_bytes} bytes'
        raise ValueError(msg)
    return value.to_bytes(num_bytes, byteorder='little')

def int_to_bytes_big(value: int, num_bytes: int) -> bytes:
    """Convert integer to bytes using big-endian byte order.

    Args:
        value: Integer to convert (non-negative)
        num_bytes: Number of bytes in output (1-8)

    Returns:
        Bytes representation in big-endian order

    Raises:
        ValueError: If value is negative, num_bytes invalid, or value too large"""
    if value < 0:
        msg = 'value must be non-negative'
        raise ValueError(msg)
    if num_bytes < 1 or num_bytes > 8:
        msg = 'num_bytes must be between 1 and 8'
        raise ValueError(msg)
    if value >= 1 << num_bytes * 8:
        msg = f'value {value} too large for {num_bytes} bytes'
        raise ValueError(msg)
    return value.to_bytes(num_bytes, byteorder='big')