# 3. password strength check

Password = "pthon@123"

check_len = len(Password)>=8
check_char = "@" in Password

print("len ok:",check_len)
print("Char Ok:",check_char)
print("strong password:",check_len and check_char)
