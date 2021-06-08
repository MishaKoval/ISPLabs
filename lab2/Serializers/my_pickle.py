from Serializers.serializer import dumps as _dumps
from Serializers.serializer import loads as _loads


def encode(data):
    data = data.replace("\n", "").replace(" ", "")
    result = [hex(ord(i)) for i in data]
    str_result = "".join(result).replace("0x", " ").upper()
    str_result = str_result[1:]
    return str_result


def decode(data):
    str_data = ""
    data = data.lower()

    while True:
        if len(data) == 0:
            break
        temp = data[:data.find(" ")]
        symbol = chr(int(temp, 16))
        if len(data) == 2:
            symbol = chr(int(data, 16))
            str_data += symbol
            break
        else:
            data = data[data.find(" ") + 1:]
        str_data += symbol

    return str_data


class PickleParser:

    def dumps(self, value_indent, value_sort):
        temp = _dumps(self, value_indent, value_sort)
        result_encode = encode(temp)
        return result_encode

    def loads(self):
        temp = decode(self)
        return _loads(temp)

    def dump(self, fp, value_indent, value_sort):
        result = encode(_dumps(self, value_indent, value_sort))
        try:
            with open(fp, "w") as file:
                file.write(result)
        except FileNotFoundError:
            raise FileNotFoundError("File doesn't exist!")

    def load(self):
        try:
            with open(fp, "r") as file:
                data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")
        result = decode(data)
        return _loads(result)
