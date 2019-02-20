import typing


def hex_to_bytes(data: list or str) -> bytes:
    return data if isinstance(data, bytes) else bytes.fromhex("".join(data))


def read_file(file: typing.IO) -> list:
    return [line.strip() for line in file.readlines()]
