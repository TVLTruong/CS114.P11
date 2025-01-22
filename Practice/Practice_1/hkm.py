#input có sử dụng GPT để sửa lỗi runtime
gia_onl = list(map(int, input().split()))
thongbao = [input() for _ in range(len(gia_onl))]
tien = int(input())

tong_online = sum(gia_onl)
if tong_online <= tien:
    print("true")
    exit()
else:
    n = len(gia_onl)
    #cách tạo danh sách gia_ch có tham khảo GPT, prompt: "cách tạo danh sách trống python"
    gia_ch = [0] * n
    for i in range(n):
        #cách trích dữ liệu số từ input câu có tham khảo GPT dùng nhiều prompt/comment để chỉnh sửa
        if "higher than in-store" in thongbao[i]:
            try:
                phan_tram = float(thongbao[i].split('%')[0].split()[-1])
                gia_ch[i] = gia_onl[i] * (1 + phan_tram / 100)
            except (ValueError, IndexError):
                continue
        elif "lower than in-store" in thongbao[i]:
            try:
                phan_tram = float(thongbao[i].split('%')[0].split()[-1])
                gia_ch[i] = gia_onl[i] * (1 - phan_tram / 100)
            except (ValueError, IndexError):
                continue

    tong_ch = sum(gia_ch)
    if tong_ch <= tien:
        print("true")
        exit()
    else:
        print("false")
        exit()