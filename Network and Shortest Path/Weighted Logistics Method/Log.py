#Nhập số lượng thành thố nhà phân phối sẽ phục vụ
print("Số lượng đối tượng")
SoLuong= input()
#Đặt tọa độ X và Y của nhà phân phối và Tổng dân số P
Cx= 0
Cy= 0
P=0
#Đặt lệnh lặp theo số lượng SoLuong
for i in range(int(SoLuong)):
    #Nhập dữ liệu cho từng đối tượng i + 1
    print ("Dân số địa điểm  %s"%(i + 1)) #Khi chạy chương trình lệnh for... in sẽ chạy cả khối theo từng đợt
    # dữ liệu P được lặp lại theo số lần i
    p= input()
    #Nhập tọa độ  cho thành phố i + 1
    print("Nhập tọa độ X của địa điểm thứ %s"%(i+1)) #Toán tử phần trăm của chuỗi
    X= input()
    print("Nhập tọa độ Y của địa điểm thứ %s"%(i+1))
    Y= input()
    #Tính tổng của tích Cx và Cy, P
    Cx= Cx + (int(X)*int(p))
    Cy= Cy + (int(Y)*int(p))
    P= P + int(p)
#Rút gọn số thực còn 2 chữ số thập phân
Tx= (Cx)/P
Ty= (Cy)/P
print("Tọa độ X của nhà phân phối: %0.2f"%(Tx)) #%f thể hiện số chữ số thập phân
print("Tọa độ Y của nhà phân phối: %0.2f"%(Ty))

    