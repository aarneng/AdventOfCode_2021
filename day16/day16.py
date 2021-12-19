bin_text = ""  # global var cause i don't care
sum_pack_vers = 0
indent = 0


def increase_indent():
    global indent
    indent += 4


def decrease_indent():
    global indent
    indent -= 4


def literal():
    global bin_text, sum_pack_vers, indent
    ans = ""
    stop = False
    len_removed = 0
    # print("LITERAL", bin_text)
    while not stop:
        stop = bin_text[0] == "0"
        bits, bin_text = bin_text[1:5], bin_text[5:]
        len_removed += 5
        ans += bits
    print(" " * (indent + 4), int(ans, 2))
    return len_removed


def operator():
    global bin_text, sum_pack_vers
    length_type_ID, bin_text = bin_text[:1], bin_text[1:]
    increase_indent()
    # print("OPERATOR", bin_text)
    if length_type_ID == "0":
        sub_packet_length_ID = 15
        sub_packet_length, bin_text = bin_text[:sub_packet_length_ID], bin_text[sub_packet_length_ID:]
        # print("BIN TEXT HERE", bin_text, sub_packet_length)
        # print(sub_packet_length)
        sub_packet_length = int(sub_packet_length, 2)
        sub_packet = bin_text[:sub_packet_length]#, bin_text[sub_packet_length:]
        parse_sub_level_amount_bits(sub_packet_length)
    else:
        sub_packet_length_ID = 11
        sub_packet_amt, bin_text = bin_text[:sub_packet_length_ID], bin_text[sub_packet_length_ID:]
        # print("BIN TEXT HERE 2", bin_text, sub_packet_amt)
        # print(sub_packet_amt == "")
        # print(sub_packet_amt)
        sub_packet_length = int(sub_packet_amt, 2)
        sub_packet = bin_text[:sub_packet_length]
        parse_sub_level_amount_packets(sub_packet_length)
    decrease_indent()


def parse_sub_level_amount_bits(bits_left):
    global bin_text, sum_pack_vers, indent
    # print("CALLED", bin_text)
    while bits_left and "1" in bin_text:
        packet_version, bin_text = bin_text[:3], bin_text[3:]
        type_ID, bin_text = bin_text[:3], bin_text[3:]
        print(" " * indent, "type:", int(type_ID, 2))
        # print(packet_version, type_ID, bin_text)
        sum_pack_vers += int(packet_version, 2)
        bits_left -= 6
        if type_ID == "100":
            # literal()
            bits_left -= literal()
        else:
            operator()


def parse_sub_level_amount_packets(packets_left):
    global bin_text, sum_pack_vers, indent
    # print("CALLED 2", bin_text)
    while packets_left and "1" in bin_text:
        packet_version, bin_text = bin_text[:3], bin_text[3:]
        sum_pack_vers += int(packet_version, 2)
        type_ID, bin_text = bin_text[:3], bin_text[3:]
        print(" " * indent, "type:", int(type_ID, 2))

        packets_left -= 1
        if type_ID == "100":
            lrm = literal()
        else:
            operator()


def parse_top_level():
    global bin_text, sum_pack_vers
    packet_version, bin_text = bin_text[:3], bin_text[3:]
    sum_pack_vers += int(packet_version, 2)
    type_ID, bin_text = bin_text[:3], bin_text[3:]
    print("type:", int(type_ID, 2))
    # print(packet_version, type_ID, bin_text)
    if type_ID == "100":
        literal()
    else:
        operator()


def main():
    with open("input.txt", "r") as f:
        mapping = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
        }
        global bin_text, sum_pack_vers
        lines = f.readlines()
        for text in lines:
            print(text)
            sum_pack_vers = 0
            text_as_bin = ""
            for char in text.strip():
                text_as_bin += mapping[char]
            bin_text = text_as_bin

            parse_top_level()
            print(sum_pack_vers)
            print("\n\n\n")


if __name__ == '__main__':
    main()

"""
p1

bin_text = ""  # global var cause i don't care
sum_pack_vers = 0


def literal():
    global bin_text, sum_pack_vers
    ans = ""
    stop = False
    len_removed = 0
    # print("LITERAL", bin_text)
    while not stop:
        stop = bin_text[0] == "0"
        bits, bin_text = bin_text[1:5], bin_text[5:]
        len_removed += 5
        ans += bits
    # print(int(ans, 2))
    return len_removed


def operator():
    global bin_text, sum_pack_vers
    length_type_ID, bin_text = bin_text[:1], bin_text[1:]
    # print("OPERATOR", bin_text)
    if length_type_ID == "0":
        sub_packet_length_ID = 15
        sub_packet_length, bin_text = bin_text[:sub_packet_length_ID], bin_text[sub_packet_length_ID:]
        # print("BIN TEXT HERE", bin_text, sub_packet_length)
        # print(sub_packet_length)
        sub_packet_length = int(sub_packet_length, 2)
        sub_packet = bin_text[:sub_packet_length]#, bin_text[sub_packet_length:]
        parse_sub_level_amount_bits(sub_packet_length)
    else:
        sub_packet_length_ID = 11
        sub_packet_amt, bin_text = bin_text[:sub_packet_length_ID], bin_text[sub_packet_length_ID:]
        # print("BIN TEXT HERE 2", bin_text, sub_packet_amt)
        # print(sub_packet_amt == "")
        # print(sub_packet_amt)
        sub_packet_length = int(sub_packet_amt, 2)
        sub_packet = bin_text[:sub_packet_length]
        parse_sub_level_amount_packets(sub_packet_length)


def parse_sub_level_amount_bits(bits_left):
    global bin_text, sum_pack_vers
    # print("CALLED", bin_text)
    while bits_left and "1" in bin_text:
        packet_version, bin_text = bin_text[:3], bin_text[3:]
        type_ID, bin_text = bin_text[:3], bin_text[3:]
        # print(packet_version, type_ID, bin_text)
        sum_pack_vers += int(packet_version, 2)
        bits_left -= 6
        if type_ID == "100":
            # literal()
            bits_left -= literal()
        else:
            operator()


def parse_sub_level_amount_packets(packets_left):
    global bin_text, sum_pack_vers
    # print("CALLED 2", bin_text)
    while packets_left and "1" in bin_text:
        packet_version, bin_text = bin_text[:3], bin_text[3:]
        sum_pack_vers += int(packet_version, 2)
        type_ID, bin_text = bin_text[:3], bin_text[3:]
        packets_left -= 1
        if type_ID == "100":
            lrm = literal()
        else:
            operator()


def parse_top_level():
    global bin_text, sum_pack_vers
    packet_version, bin_text = bin_text[:3], bin_text[3:]
    sum_pack_vers += int(packet_version, 2)
    type_ID, bin_text = bin_text[:3], bin_text[3:]
    # print(packet_version, type_ID, bin_text)
    if type_ID == "100":
        literal()
    else:
        operator()


def main():
    with open("input.txt", "r") as f:
        mapping = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
        }
        global bin_text, sum_pack_vers
        lines = f.readlines()
        for text in lines:
            print(text)
            sum_pack_vers = 0
            text_as_bin = ""
            for char in text.strip():
                text_as_bin += mapping[char]
            bin_text = text_as_bin

            parse_top_level()
            print(sum_pack_vers)
            print("\n\n\n")


if __name__ == '__main__':
    main()





"""