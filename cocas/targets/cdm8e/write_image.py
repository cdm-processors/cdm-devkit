from cocas.write_image import WriteImageInterface


class WriteImage(WriteImageInterface):
    @staticmethod
    def write_image(filename: str, arr: bytearray):
        f = open(filename, mode='wb')
        f.write(bytes("v2.0 raw\n", 'UTF-8'))
        for byte in arr:
            f.write(bytes(f'{byte:02x}\n', 'UTF-8'))
        f.close()
