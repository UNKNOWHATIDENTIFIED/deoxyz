import tkinter as tk
from tkinter import scrolledtext
import webbrowser

qa_data = {
    "xin chào": "Chào bạn! Mình rất vui khi được hỗ trợ bạn hôm nay. Bạn cần tư vấn gì nào?",
    "chào": "Xin chào! Bạn khỏe không? Nếu cần trợ giúp, mình luôn sẵn sàng lắng nghe.",
    "bạn tên gì": "Mình là trợ lý ảo do chính bạn tạo ra. Bạn có thể gọi mình là 'người bạn y tế' của bạn!",
    "cảm ơn": "Không có gì đâu! Mình luôn ở đây nếu bạn cần giúp đỡ 💡.",
    "hẹn gặp lại": "Tạm biệt nhé! Chúc bạn luôn mạnh khỏe và vui vẻ! 💖",

    "mất ngủ": "Mất ngủ do stress, thiết bị điện tử hoặc lo âu. Hãy thư giãn, hạn chế caffeine và thử nghe nhạc nhẹ khi đi ngủ.",
    "mệt mỏi": "Bạn nên kiểm tra giấc ngủ, chế độ ăn và tâm lý. Nếu kéo dài, có thể do thiếu máu, tuyến giáp hoặc trầm cảm.",
    "đau đầu": "Có thể do căng thẳng, mất ngủ, huyết áp. Nếu đau kèm theo buồn nôn, hoa mắt, nên kiểm tra y tế.",
    "chóng mặt": "Có thể do thiếu máu, huyết áp thấp, rối loạn tiền đình. Hãy nghỉ ngơi và uống đủ nước.",
    "buồn nôn": "Có thể do tiêu hóa, đau đầu, hoặc dấu hiệu có thai. Nếu kéo dài, nên kiểm tra dạ dày.",
    "run tay": "Run tay có thể do stress, hạ đường huyết hoặc Parkinson. Nếu liên tục, nên gặp bác sĩ thần kinh.",
    "co giật": "Đây là triệu chứng nghiêm trọng. Có thể liên quan đến động kinh hoặc tổn thương thần kinh – cần cấp cứu.",
    "sốt" :"đây là triệu chứng bị bệnh do nhiều nguyên nhân nên đi tới bệnh viện gần nhất để khám",
    "huyết áp cao": "Bạn nên kiểm tra huyết áp thường xuyên. Hạn chế muối, tránh stress và tập thể dục đều đặn.",
    "huyết áp thấp": "Có thể gây chóng mặt, mệt mỏi. Uống nước đủ, ăn mặn hơn và tránh thay đổi tư thế đột ngột.",
    "đánh trống ngực": "Có thể do hồi hộp, caffeine hoặc rối loạn nhịp tim. Nếu kéo dài, nên đo điện tâm đồ.",
    "đau ngực": "Nếu đau ngực lan ra tay trái, cổ, kèm khó thở – có thể là cơn đau tim. Gọi cấp cứu ngay.",
    
    "ho khan": "Ho khan kéo dài có thể là viêm họng, viêm phế quản hoặc hậu COVID. Nên uống nước ấm, hạn chế nói nhiều.",
    "ho có đờm": "Cần theo dõi màu đờm. Nếu vàng/xanh hoặc có máu, nên đi khám hô hấp.",
    "viêm phổi": "Triệu chứng gồm ho, sốt cao, khó thở. Cần kháng sinh theo chỉ định và nghỉ ngơi nhiều.",
    "viêm họng": "Khó nuốt, đau rát. Ngậm nước muối, uống nước ấm và tránh đồ lạnh.",
    "nghẹt mũi": "Có thể do cảm lạnh, viêm xoang. Xông mũi bằng nước nóng, uống nước ấm sẽ đỡ.",
    "sổ mũi": "Đừng xì mũi quá mạnh. Nghỉ ngơi, giữ ấm, tránh gió lạnh.",
    
    "đau bụng": "Có thể do rối loạn tiêu hóa, viêm ruột, hoặc ăn uống không hợp vệ sinh. Theo dõi triệu chứng kèm theo.",
    "nôn ói": "Cẩn thận với ngộ độc thực phẩm. Uống từng ngụm nước, nghỉ ngơi.",
    "tiêu chảy": "Bổ sung oresol để tránh mất nước. Tránh sữa, đồ dầu mỡ.",
    "táo bón": "Ăn nhiều rau, uống nhiều nước, tăng cường vận động.",
    "đầy hơi": "Tránh đồ uống có ga, ăn chậm nhai kỹ, có thể dùng men tiêu hóa.",
    "ợ nóng": "Cảm giác nóng rát vùng ngực do axit dạ dày trào ngược. Hạn chế thức ăn cay, nằm kê cao gối.",
    "viêm dạ dày": "Đau vùng thượng vị, ợ chua, khó tiêu. Cần ăn uống đúng giờ và hạn chế stress.",
    "trào ngược dạ dày": "Khó chịu vùng ngực, buồn nôn. Nên ăn ít một, tránh nằm ngay sau ăn.",
    
    "đau lưng": "Ngồi sai tư thế, mang vác nặng hoặc thoái hóa cột sống là nguyên nhân thường gặp.",
    "đau vai gáy": "Thường do ngồi máy tính lâu hoặc stress. Xoa bóp nhẹ và vận động thường xuyên sẽ giúp.",
    "đau khớp": "Có thể do viêm khớp, thoái hóa hoặc chấn thương. Giữ ấm, tránh vận động mạnh.",
    "tê tay chân": "Tê thường do chèn ép dây thần kinh, thiếu máu hoặc tiểu đường. Nếu kéo dài nên khám chuyên khoa thần kinh.",
    
    "đường huyết cao": "Cảnh báo nguy cơ tiểu đường. Hạn chế tinh bột, tăng cường vận động và kiểm tra đường huyết thường xuyên.",
    "đường huyết thấp": "Gây run rẩy, vã mồ hôi. Hãy uống nước ngọt hoặc ăn nhẹ chứa đường ngay.",
    "suy giáp": "Mệt mỏi, lạnh, tăng cân. Cần xét nghiệm máu để điều chỉnh hormone.",
    "cường giáp": "Tim đập nhanh, sút cân, lo âu. Bệnh cần được bác sĩ nội tiết kiểm soát.",

    "sốt ở trẻ em": "Theo dõi nhiệt độ, cho uống nước nhiều, lau mát và dùng hạ sốt khi trên 38.5°C.",
    "ho ở trẻ": "Cho trẻ uống nước ấm, giữ ấm cổ. Không nên tự ý dùng thuốc ho nếu chưa có chỉ định.",
    "nôn ở trẻ em": "Thường do rối loạn tiêu hóa. Tránh ép ăn, cho uống nước từ từ.",
    "tiêu chảy ở trẻ": "Nguy hiểm nếu mất nước. Bù oresol, cho ăn cháo loãng, tránh đồ tanh.",

    "đau chân": "Đau chân có thể do vận động quá mức, giãn tĩnh mạch, hoặc chèn ép thần kinh. Nghỉ ngơi, chườm lạnh, và nâng cao chân có thể giúp. Nếu kéo dài, nên đi khám xương khớp.",
    "đau đầu gối": "Có thể do viêm khớp, chấn thương sụn hoặc thoái hóa. Tránh gập gối quá lâu và nên chườm nóng/lạnh tùy tình trạng.",
    "đau mắt cá chân": "Thường là do bong gân, va chạm hoặc chấn thương cơ học. Nên nghỉ ngơi, chườm lạnh trong 48h đầu và băng cố định.",
    "đau gót chân": "Có thể là viêm cân gan chân – thường đau nhất khi mới ngủ dậy. Đi giày mềm, chườm lạnh và giãn cơ sẽ giúp.",
    "chuột rút": "Chuột rút do mất khoáng (magie, kali), mất nước hoặc vận động nhiều. Hãy duỗi cơ nhẹ nhàng và uống nước điện giải.",
    "tê chân": "Tê có thể do ngồi lâu, thiếu máu ngoại biên hoặc chèn ép dây thần kinh tọa. Nếu kéo dài, bạn cần khám chuyên khoa thần kinh.",
    "tê tay": "Tê tay thường do hội chứng ống cổ tay, tiểu đường hoặc thiếu máu não. Tránh làm việc máy tính quá nhiều, nên xoa bóp nhẹ.",
    "đau tay": "Đau tay có thể do viêm khớp, gân, hoặc dây chằng. Nếu đau kèm tê, có thể liên quan đến chèn ép thần kinh cổ.",
    "viêm khớp": "Viêm khớp thường gây sưng, nóng, đỏ, đau vùng khớp. Cần được bác sĩ chẩn đoán và dùng thuốc phù hợp.",
    "thoái hóa khớp": "Là quá trình lão hóa sụn, hay gặp ở đầu gối, cột sống, gây đau nhức khi vận động. Vật lý trị liệu và chế độ sinh hoạt là rất cần thiết.",
    "viêm dây chằng": "Đau khi cử động hoặc căng cơ. Nghỉ ngơi, chườm lạnh và tránh vận động mạnh là ưu tiên ban đầu.",
    "gãy xương": "Nếu có sưng to, đau dữ dội, không cử động được thì cần cố định và đến bệnh viện ngay để chụp X-quang.",
    "trật khớp": "Khớp bị lệch khỏi vị trí bình thường. Không nên cố nắn lại nếu không có chuyên môn – hãy đến bác sĩ chỉnh hình.",
    "bong gân": "Chấn thương gân nhẹ, thường gặp ở cổ chân, cổ tay. Cần băng ép, chườm lạnh, nghỉ ngơi và nâng cao chi bị thương.",
    "đau cột sống": "Thường là dấu hiệu của thoát vị đĩa đệm, gai cột sống hoặc tư thế sai. Cần tập vật lý trị liệu và kiểm tra hình ảnh học nếu cần.",
    "thoát vị đĩa đệm": "Đau lưng lan xuống chân, kèm tê, yếu cơ. Hạn chế cúi, mang vác nặng, nên đi MRI để chẩn đoán chính xác.",
    "đau thần kinh tọa": "Cơn đau lan từ thắt lưng xuống mông và mặt sau chân. Có thể do chèn ép thần kinh – cần điều trị sớm để tránh teo cơ.",
    "đau hông": "Đau vùng chậu hoặc bên hông thường do viêm khớp háng, dây chằng hoặc thần kinh tọa. Nên tránh gập người sâu và khám chuyên khoa.",
    "đau cổ": "Ngồi máy tính sai tư thế hoặc ngủ sai có thể gây căng cơ cổ. Chườm nóng, xoa bóp nhẹ và tránh xoay mạnh đầu.",
    "vẹo cột sống": "Hay gặp ở tuổi học sinh do tư thế xấu. Nên theo dõi bằng chụp X-quang và tập vật lý trị liệu đúng cách.",

    "giãn tĩnh mạch": "Biểu hiện là đau, tê mỏi chân, nổi gân xanh. Tránh đứng lâu, nâng chân khi nghỉ, mang vớ y khoa nếu cần.",
    "ho": "cảm hoặc bị đau họng không nên uống nước lạnh và nên uống nước ấm",
    "phù chân": "Chân bị phù có thể do bệnh tim, thận, hoặc tĩnh mạch. Nếu phù kéo dài hoặc kèm khó thở, nên đến bệnh viện.",
    "chảy máu chân răng": "Có thể do viêm lợi, thiếu vitamin C hoặc vệ sinh răng không đúng cách. Đừng bỏ qua – hãy đi khám nha khoa.",
    "da tím tái": "Nếu da tay chân tím, lạnh – có thể do thiếu oxy hoặc tuần hoàn kém. Nếu kéo dài, cần kiểm tra tim phổi ngay.",
}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword in qa_data:
        if keyword in user_input:
            return qa_data[keyword]
    return "Mình chưa rõ triệu chứng đó. Bạn có thể mô tả cụ thể hơn không?"

def update_links(keyword):
    link_listbox.delete(0, tk.END)
    query = keyword.replace(" ", "+")
    links = [
        f"https://www.google.com/search?q={query}",
        f"https://medlatec.vn/tim-kiem-thong-tin?keyword={query}&type=bai-viet",
        f"https://youmed.vn/tin-tuc/?s={query}",
        f"https://www.youtube.com/results?search_query={query}+triệu+chứng",
    ]
    for link in links:
        link_listbox.insert(tk.END, link)

def open_link(event):
    try:
        selected = link_listbox.get(link_listbox.curselection())
        webbrowser.open(selected)
    except:
        pass

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, f"Bạn: {user_input}\n", "user")
    entry.delete(0, tk.END)

    if user_input.lower() in ["thoát", "exit", "bye"]:
        chat_window.insert(tk.END, "Bác sĩ ảo: Chúc bạn mau khỏe! Tạm biệt nhé.\n", "bot")
        entry.config(state="disabled")
        send_button.config(state="disabled")
        return

    response = get_response(user_input)
    chat_window.insert(tk.END, f"Bác sĩ ảo: {response}\n", "bot")
    chat_window.yview(tk.END)
    update_links(user_input)

root = tk.Tk()
root.title("Chatbot Tư Vấn Bệnh")
root.geometry("900x500")
root.configure(bg="#0909ff")


# Frame chính chia trái/phải
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# LEFT – Chatbot
left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


chat_window = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry = tk.Entry(left_frame, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(left_frame, text="Gửi", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# RIGHT – Link tham khảo
right_frame = tk.Frame(main_frame, bg="#f0f0f0", width=300)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

tk.Label(right_frame, text="🔗 Tham khảo thêm:", font=("Arial", 12, "bold"), bg="#f31919").pack(pady=10)
link_listbox = tk.Listbox(right_frame, font=("Arial", 10), bg="#ffffff", height=20, width=45)
link_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
link_listbox.bind("<Double-Button-1>", open_link)

# Khởi động lời chào
chat_window.insert(tk.END, "Bác sĩ ảo: Xin chào! Bạn đang gặp vấn đề gì về sức khỏe? (Gõ 'thoát' để rời đi)\n", "bot")

root.mainloop()
