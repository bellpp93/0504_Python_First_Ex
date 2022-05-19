"""
    고객 정보 관리 시스템 구축(메뉴 방식)
"""
from tkinter import Tk, Menu, Frame, PanedWindow, ttk, messagebox
from tkinter.ttk import LabelFrame, Label, Entry, Button
import tkinter.font as tkFont

win = Tk()  # 객체 생성
win.title('고객정보관리 시스템')
win.geometry('%dx%d+%d+%d' %(800, 600, 10, 10))  # 넓이x높이+x축+y축

menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='열기')
filemenu.add_command(label='저장')
filemenu.add_separator()  # 줄 넣기
filemenu.add_command(label='닫기')

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...')

win.config(menu=menubar)

topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100)

panedwindow = PanedWindow(relief='raised', bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=200, height=400)

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=470)

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

buttonFrame = Frame(win)
buttonFrame.pack(side='bottom')
buttonFrame.config(width=800, height=30)

# leftFrame에 Entry 위젯 추가
lable_frame = LabelFrame(leftFrame, text='기본 정보 입력')
lable_frame.pack()

lbl_name = Label(lable_frame, text='이름')
lbl_phone = Label(lable_frame, text='전화번호')
lbl_email = Label(lable_frame, text='이메일')

entry_name = Entry(lable_frame)
entry_phone = Entry(lable_frame)
entry_email = Entry(lable_frame)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, padx=5, pady=5)

lbl_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

lbl_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1, padx=5, pady=5)

panedwindow = PanedWindow(buttonFrame, relief='raised', bd=0)
panedwindow.pack()

btn_output = Button(panedwindow, text='전체보기')
btn_input = Button(panedwindow, text='추가')
btn_search = Button(panedwindow, text='이름 검색')
btn_modify = Button(panedwindow, text='수정')
btn_delete = Button(panedwindow, text='삭제')

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)

# rightFrame에 목록 추가하기
header_list = ['no', 'name', 'phone number', 'e-mail']
data_list = []

# Treeview는 그리드표를 출력하는데 유용한 위젯이다. => 행과 열로 구성된 표를 생성할 수 있다.
tree = ttk.Treeview(rightFrame, columns=header_list, show='headings')
tree.pack()

for i, col in enumerate(header_list):
    tree.heading(col, text=col.title())

# Treeview의 각 필드 너비 설정
tree.column(0, width=50)
tree.column(1, width=80)
tree.column(2, width=150)
tree.column(3, width=250)

# 앱 타이틀 라벨 추가
fontStyle = tkFont.Font(family='궁서체', size=28)
lbl_title = Label(topFrame, text='고객 정보 관리 시스템', font=fontStyle)
lbl_title.place(relx=0.5, rely=0.5, anchor='center')

if __name__ == '__main__':  # 메인 함수 선언, '시작'을 의미함.
    # 생성한 윈도우 내부에서 수행되는 마우스 클릭 같은 이벤트들이 발생하게끔 유지해주는 함수이다.
    win.mainloop()