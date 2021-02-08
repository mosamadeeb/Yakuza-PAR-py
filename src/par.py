from typing import List


class Header:
    big_endian: bool
    version: int

    folder_count: int
    folder_offset: int
    file_count: int
    file_offset: int


class File:
    name: str

    compression: int
    size: int
    compressed_size: int
    base_offset: int

    attributes: int
    extended_offset: int
    timestamp: int

    data: bytearray


class Folder:
    name: str

    folder_count: int
    folder_start: int
    file_count: int
    file_start: int

    attributes: int

    folders: List['Folder']
    files: List[File]


class Par:
    header: Header

    folders: List[Folder]
    files: List[File]
