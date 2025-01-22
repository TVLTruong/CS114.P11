keywords = ["% lower than in-store", "% higher than in-store"]

price = list(map(int, input().split()))

st = []
for _ in range(len(price)):
    s = input()
    st.append(s)

per = []

money = int(input())

if sum(price) > money:
    print("false")
    exit()

for text in st:
    for _ in range(2):
        position = text.find(keywords[_])

        if position != -1:
            before_keyword = text[:position].strip()

            try:
                number = float(before_keyword.split('%')[0].split()[-1])
            except (ValueError, IndexError):
                continue

            if _ == 0: 
                num = 1 + number / 100
            else:
                num = 1 - number / 100

            per.append(num)
            break  

total = 0
for i in range(len(price)):
    if i < len(per):
        total += price[i] * per[i]

if money >= total:
    print("true")
else:
    print("false")
    
    
'''
https://chatgpt.com/share/66e99297-ec90-8005-82d3-c251ecb4885a
câu 1: trong python, tôi có một chuỗi như: Contratulation that was 2.4% lower than in-store . 
Tôi biết trước sẽ có chuỗi % lower than in-store trong chuỗi lớn làm sao để xác định vị trí 
của chuỗi nhỏ để lấy ra con số liền trước chuỗi như số 2.4 

câu 2: có cách nào không dùng thư viện hay không
'''

#Sử dụng câu lệnh 14->16 của bạn Thành Trung

'''
Sử dụng câu lệnh dòng  21->24 của bạn Thành Trung thay thế cho lệnh 
number = before_keyword[last_space+1:] ban đầu
'''