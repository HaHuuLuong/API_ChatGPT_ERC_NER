import re
data = open("C:/Users/LENOVO/Desktop/crawl_data/ChatGPT_API/input.txt",encoding="utf-8").read().splitlines()
# for item in data:
#     # pattern = r"\([^()]*\)" # matches anything inside parentheses
#     repl = "" # empty string
#     pattern1 = "-\d+" # biểu thức chính quy cho số âm
#     pattern2 = "\(\d{2}/\d{2}/\d{4} \d{1,2}:\d{1,2}:\d{1,2} [ap]m\)" # biểu thức chính quy cho ngày giờ
#     result = re.sub(pattern1 + "|" + pattern2, repl, item) # trả về một chuỗi mới sau khi đã được xử lý
#     print(result) # print the result
# file = open("output.txt", "w") # mở file output.txt ở chế độ ghi
# file.write(result) # ghi chuỗi mới vào file
# file.close() # đóng file
with open("result_regex.txt", "w", encoding="utf-8") as f:
    for item in data:
        repl = ""
        pattern1 = "-\d+"
        pattern2 = "\(\d{2}/\d{2}/\d{4} \d{1,2}:\d{1,2}:\d{1,2} [ap]m\)"
        result = re.sub(pattern1 + "|" + pattern2, repl, item)
        f.write(result + "\n")

