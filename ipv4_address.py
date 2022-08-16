# Work In Progress
#
#
# Converts Decimal IP Address into Binary, and then into the standard 4 octets
#
def ip_converter(decimal_ip):
    if type(decimal_ip) == int:
        if 0 < decimal_ip <= 4294967295:
            bin_ip = bin(decimal_ip)
            bin_ip = bin_ip[2:]
            while len(bin_ip) != 32:
                leading_zero = "0"
                bin_ip = leading_zero + bin_ip
            n = 8
            binary_octets = [bin_ip[i:i+n] for i in range(0, len(bin_ip), n)]
            ip_octets = []
            for i in binary_octets:
                ip_octets.append(int(i, 2))
            return "{}.{}.{}.{}".format(ip_octets[0], ip_octets[1], ip_octets[2], ip_octets[3])
        else:
            return "Invalid Value"
    else: 
        return "Expected Integer"

my_decimal_ip = 3232235521
print(ip_converter(my_decimal_ip))
#
#192.168.0.1
