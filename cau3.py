name=input("Nhập tên đầy đủ của bạn : ")
print("Tên đầy đủ của bạn là : ",name)
def sothuannghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n, "là", sothuannghich(n));