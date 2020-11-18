from enum import Enum


class ReadResult(Enum):
    Success = 0
    WrongFormat = 1
    WrongDataType = 2
    ReadError = 3


class BinaryReader:
    def __init__(self, sz_address):
        print("start constructor")

        self.m_szAddr = sz_address
        self.m_ReadResult = ReadResult.Success
        self.m_nDimension = 0
        self.m_lsDimension = []
        self.m_HeaderOffset = 0

        file = open(sz_address, "rb")

        # read first 4 bytes for checking the format
        magic_num = int.from_bytes(file.read(4), byteorder='big')

        if magic_num >> 16 is not 0x00:
            # first 8 bits should be 0x0000
            self.m_ReadResult = ReadResult.WrongFormat

        if magic_num >> 8 & 0xff is not 0x08:
            # should be unsigned byte
            self.m_ReadResult = ReadResult.WrongDataType

        # 0x01 for vector, 0x02 for matrix
        self.m_nDimension = magic_num & 0xff

        # read 4 bytes for each dimension
        for i in range(self.m_nDimension):
            self.m_lsDimension.append(int.from_bytes(file.read(4), byteorder='big'))

        # header offset = magic num + dimension
        self.m_HeaderOffset = 4 + self.m_nDimension * 4

        # close the file
        file.close()

    def GetOneData(self, nInd):
        file = open(self.m_szAddr, "rb")
        matls = []
        if self.m_nDimension is 0x01:
            file.seek(self.m_HeaderOffset + nInd)
            matls.append(int.from_bytes(file.read(1), byteorder='big'))

        elif self.m_nDimension is 0x03:
            mat_ele_size = self.m_lsDimension[1] * self.m_lsDimension[2]
            file.seek(self.m_HeaderOffset + nInd * mat_ele_size)
            for i in range(mat_ele_size):
                matls.append(int.from_bytes(file.read(1), byteorder='big'))

        file.close()
        return matls

    def GetAllData(self):
        lsData = []
        file = open(self.m_szAddr, "rb")

        file.seek(self.m_HeaderOffset)

        if self.m_nDimension is 0x01:
            # read vectors
            for i in range(self.m_lsDimension[0]):
                lsData.append(int.from_bytes(file.read(1), byteorder='big'))

        elif self.m_nDimension is 0x03:
            # read 2d matrix
            for i in range(self.m_lsDimension[0]):
                matlist = []
                for j in range(self.m_lsDimension[1] * self.m_lsDimension[2]):
                    matlist.append(int.from_bytes(file.read(1), byteorder='big'))

                # append the matrix list to data
                lsData.append(matlist)

        file.close()
        return lsData
