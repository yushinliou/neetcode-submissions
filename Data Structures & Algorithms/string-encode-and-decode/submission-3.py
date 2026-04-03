class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        strs_encoded = ""
        for string in strs:
            if len(string) == 0:
                strs_encoded = strs_encoded + "%" + ","
            else:
                str_asc = ""
                for char in string:
                    str_asc = str_asc + str(ord(char)) + " "
                str_asc = str_asc.strip(" ")
                strs_encoded = strs_encoded + str_asc + ","        
        strs_encoded = strs_encoded.strip(",")
        return strs_encoded
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        decode_lst = []
        str_lst = s.split(",")
        # print(str_lst)
        for string_encode in str_lst:
            print(string_encode)
            if string_encode == "%":
                decode_lst.append('')
            else:
                string = ""
                for char in string_encode.split(" "):
                    # print(string_encode.split(" "))
                    if char.isdigit():
                        string += chr(int(char))
                decode_lst.append(string)
        return decode_lst
            


