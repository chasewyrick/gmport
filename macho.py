# Copyright (c) 2016-2017, Grant Paul
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import struct

class Struct(object):
    @classmethod
    def format(cls, endian):
        format = endian
        for key, value in cls.FORMAT:
            format += value 
        return format

    @classmethod
    def calcsize(cls):
        format = cls.format('=')
        return struct.calcsize(format)

    def unpack(self, endian, contents, offset):
        values = struct.unpack_from(self.format(endian), contents, offset)
        for (name, format), value in zip(self.FORMAT, values):
            setattr(self, name, value)

    def pack(self, endian):
        values = []
        for name, format in self.FORMAT:
            value = getattr(self, name)
            values.append(value)
        return struct.pack(self.format(endian), *values)

FAT_MAGIC = 0xcafebabe
class fat_header(Struct):
    FORMAT = [
        ('magic', 'I'),
        ('nfat_arch', 'I'),
    ]
class fat_arch(Struct):
    FORMAT = [
        ('cputype', 'I'),
        ('cpusubtype', 'I'),
        ('offset', 'I'),
        ('size', 'I'),
        ('align', 'I'),
    ]

MH_MAGIC = 0xfeedface
MH_MAGIC_64 = 0xfeedfacf
class mach_header(Struct):
    FORMAT = [
        ('magic', 'I'),
        ('cputype', 'I'),
        ('cpusubtype', 'I'),
        ('filetype', 'I'),
        ('ncmds', 'I'),
        ('sizeofcmds', 'I'),
        ('flags', 'I'),
    ]
class mach_header_64(Struct):
    FORMAT = [
        ('magic', 'I'),
        ('cputype', 'I'),
        ('cpusubtype', 'I'),
        ('filetype', 'I'),
        ('ncmds', 'I'),
        ('sizeofcmds', 'I'),
        ('flags', 'I'),
        ('reserved', 'I'),
    ]

class dylib(Struct):
    FORMAT = [
        ('name', 'I'),
        ('timestamp', 'I'),
        ('current_version', 'I'),
        ('compatibility_version', 'I'),
    ]

S_ZEROFILL = 0x1
class section(Struct):
    FORMAT = [
        ('sectname', '16s'),
        ('segname', '16s'),
        ('addr', 'I'),
        ('size', 'I'),
        ('offset', 'I'),
        ('align', 'I'),
        ('reloff', 'I'),
        ('nreloc', 'I'),
        ('flags', 'I'),
        ('reserved1', 'I'),
        ('reserved2', 'I'),
    ]
class section_64(Struct):
    FORMAT = [
        ('sectname', '16s'),
        ('segname', '16s'),
        ('addr', 'Q'),
        ('size', 'Q'),
        ('offset', 'I'),
        ('align', 'I'),
        ('reloff', 'I'),
        ('nreloc', 'I'),
        ('flags', 'I'),
        ('reserved1', 'I'),
        ('reserved2', 'I'),
        ('reserved3', 'I'),
    ]

class load_command(Struct):
    FORMAT = [
        ('cmd', 'I'),
        ('cmdsize', 'I'),
    ]

LC_SEGMENT = 0x01
class segment_command(Struct):
    FORMAT = load_command.FORMAT + [
        ('segname', '16s'),
        ('vmaddr', 'I'),
        ('vmsize', 'I'),
        ('fileoff', 'I'),
        ('filesize', 'I'),
        ('maxprot', 'I'),
        ('initprot', 'I'),
        ('nsects', 'I'),
        ('flags', 'I'),
    ]
LC_SEGMENT_64 = 0x19
class segment_command_64(Struct):
    FORMAT = load_command.FORMAT + [
        ('segname', '16s'),
        ('vmaddr', 'Q'),
        ('vmsize', 'Q'),
        ('fileoff', 'Q'),
        ('filesize', 'Q'),
        ('maxprot', 'I'),
        ('initprot', 'I'),
        ('nsects', 'I'),
        ('flags', 'I'),
    ]

LC_LOAD_DYLIB = 0x0C
class dylib_command(Struct):
    FORMAT = load_command.FORMAT + [
    ] + dylib.FORMAT

