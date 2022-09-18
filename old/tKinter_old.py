from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.scrolledtext as st


if __name__ == "__main__":
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir='./src',title='파일선택', filetypes=(('exel files','*.xlsx'),('txt files','*.txt'),('all files','*.*')))
    root.title("DrSong Crawling Tool")
    root.geometry('1000x600')
    root.resizable(0, 0)

    frame_main = Label(root, text="닥터송 크롤링 툴")
    frame_main.pack(side="top", fill="both", expand=True)
    frame_main.pack_propagate(0)

    frame_left = LabelFrame(frame_main, text="frame_left")
    frame_left.pack(side="left", fill="both", expand=True)
    frame_left.pack_propagate(0)


    frame_right = LabelFrame(frame_main, text="frame_right")
    frame_right.pack(side="left", fill="both", expand=True)
    frame_right.pack_propagate(0)

####################################################  frame_basic   ####################################################


    frame_basic = Frame(frame_left, height=100)
    frame_basic.pack(side="top", fill="both")
    frame_basic.pack_propagate(0)

    ####################################################

    # frame_basic_1 = LabelFrame(frame_basic, text='frame_basic_1', width=10)
    # frame_basic_1.pack(side="left", fill="both")
    # # frame_basic_1.config(highlightbackground='black', highlightthickness=1)
    #
    # label_basic_1 = Label(frame_basic_1, text="기본 모델 ", width = 5, borderwidth=2)
    # label_basic_1.pack()
    #
    # label_basic_2 = Label(frame_basic_1, text="학습 모델 ", width= 5)
    # label_basic_2.pack()

    ####################################################

    frame_basic_2 = Frame(frame_basic)
    frame_basic_2.pack(side="left", fill="both")

    frame_basic_2_top = Frame(frame_basic_2)
    frame_basic_2_top.pack(side="top", fill="both")

    label_basic_1 = Label(frame_basic_2_top, text="기본 모델 ", width=5, borderwidth=2)
    label_basic_1.pack(side='left')

    entry1 = Entry(frame_basic_2_top)
    entry1.pack(side='left')

    btn1 = Button(frame_basic_2_top, text="신규", fg='black', command=cmd, width=4)
    btn1.pack(side='left')

    frame_basic_2_bot = Frame(frame_basic_2)
    frame_basic_2_bot.pack(side="top", fill="both")

    label_basic_2 = Label(frame_basic_2_bot, text="학습 모델 ", width=5)
    label_basic_2.pack(side='left')

    entry2 = Entry(frame_basic_2_bot)
    entry2.pack(side='left')

    btn2 = Button(frame_basic_2_bot, text="리네임", fg='black', command=cmd, width=4)
    btn2.pack(side='left')

    ####################################################

    # frame_basic_3 = LabelFrame(frame_basic, text="frame_basic_3")
    # frame_basic_3.pack(side="left", fill="both")

    ####################################################

    frame_basic_4 = Frame(frame_basic)
    frame_basic_4.pack(side="left", fill="both")
    # frame_basic_4.pack_propagate(0)

    label_basic_4 = st.ScrolledText(frame_basic_4, wrap=tk.WORD)
    label_basic_4.config(highlightbackground='black', highlightthickness=1)
    label_basic_4.pack(expand=True)

    #################################################### frame_type   ####################################################

    frame_type = LabelFrame(frame_left, text="전처리 옵션 설정", height=50)
    frame_type.pack(side="top", fill="both")

    ####################################################

    frame_type_data = Frame(frame_type)
    frame_type_data.pack(side="top", fill="both", expand=True)

    CheckVar1=IntVar()
    CheckVar2=IntVar()
    CheckVar3=IntVar()
    CheckVar4=IntVar()
    CheckVar5=IntVar()

    c1 = Checkbutton(frame_type_data, text="html 태그 제거", variable=CheckVar1)
    c1.pack(side="left")

    c2 = Checkbutton(frame_type_data, text="특수문자 제거", variable=CheckVar2)
    c2.pack(side="left")

    c3 = Checkbutton(frame_type_data, text="단어 분리", variable=CheckVar3)
    c3.pack(side="left")

    c4 = Checkbutton(frame_type_data, text="불용어 제거", variable=CheckVar4)
    c4.pack(side="left")

    c5 = Checkbutton(frame_type_data, text="어간 추출", variable=CheckVar5)
    c5.pack(side="left")



    ####################################################

    frame_type_stopW = Frame(frame_type)
    frame_type_stopW.pack(side="bottom", fill="both", expand=True)

    label_type_stop = Label(frame_type_stopW, text='불용어 입력 (예: 이, 있)')
    label_type_stop.pack(side="left")

    entry_stop = Entry(frame_type_stopW, width=20)
    entry_stop.pack(side="left")

    ####################################################

    frame_type_training = Frame(frame_type_stopW)
    frame_type_training.config(highlightthickness=1, highlightbackground='gray')
    frame_type_training.pack(side="right", fill="both")

    CheckVar2 = IntVar()
    CheckVar3 = IntVar()

    c2 = Checkbutton(frame_type_training, text="Fine Tuning", variable=CheckVar2)
    c2.pack()
    c3 = Checkbutton(frame_type_training, text="Class Matching", variable=CheckVar3)
    c3.pack()

    # #################################################### frame_param ####################################################

    frame_param = LabelFrame(frame_left, text="frame_param", height=10)
    frame_param.pack(side="top", fill="both")

    frame_param_option = Frame(frame_param)
    frame_param_option.pack(side="left", fill="both")

    frame_param_option_right = Frame(frame_param)
    frame_param_option_right.pack(side="left", fill="both")

    # #################################################### frame_param_option ####################################################

    frame_param_option_top = Frame(frame_param_option)
    frame_param_option_top.pack(side="top", fill="both")

    label_param_option_epoch = Label(frame_param_option_top, text='Epoch #')
    label_param_option_epoch.pack(side="left")

    entry_epoch = Entry(frame_param_option_top, width=5)
    entry_epoch.pack(side="right")


    # ####################################################

    frame_param_option_bot = Frame(frame_param_option)
    frame_param_option_bot.pack(side="top", fill="both")

    label_param_option_batch = Label(frame_param_option_bot, text='BatchSize')
    label_param_option_batch.pack(side="left")

    entry_batch = Entry(frame_param_option_bot, width=5)
    entry_batch.pack(side="right")

    # ####################################################

    frame_param_option_right_top = Frame(frame_param_option_right)
    frame_param_option_right_top.pack(side="top", fill="both")

    label_param_option_min_word = Label(frame_param_option_right_top, text='minium word count')
    label_param_option_min_word.pack(side="left")

    entry_min_word = Entry(frame_param_option_right_top, width=5)
    entry_min_word.pack(side="right")

    frame_param_option_right_bot = Frame(frame_param_option_right)
    frame_param_option_right_bot.pack(side="top", fill="both")

    label_param_option_feature = Label(frame_param_option_right_bot, text='feature')
    label_param_option_feature.pack(side="left")

    entry_feature = Entry(frame_param_option_right_bot, width=5)
    entry_feature.pack(side="right")

    # ####################################################

    frame_param_button = Frame(frame_param)
    frame_param_button.pack(side="left", fill="both", expand=True)

    # frame_param_button_1 = LabelFrame(frame_param_button, text="frame_param_button_1", width=5)
    # frame_param_button_1.pack(side="left", fill="both")

    # param_button_1 = Button(frame_param_button_1, text="도움말", fg='black', command=cmd, width=5)
    # param_button_1.pack()
    # param_button_2 = Button(frame_param_button_1, text="설정열기", fg='black', command=cmd, width=5)
    # param_button_2.pack()
    # param_button_3 = Button(frame_param_button_1, text="설정저장", fg='black', command=cmd, width=5)
    # param_button_3.pack()

    frame_param_button_2 = LabelFrame(frame_param_button, text="frame_param_button_2")
    frame_param_button_2.pack(side="left", fill="both")

    param_button_4 = Button(frame_param_button, text="도움말", fg='black', command=cmd, width=5)
    param_button_4.pack()
    param_button_5 = Button(frame_param_button, text="학습시작", fg='black', command=cmd, width=5)
    param_button_5.pack()
    param_button_6 = Button(frame_param_button, text="학습중지", fg='black', command=cmd, width=5)
    param_button_6.pack()

    # #################################################### frame_log   ####################################################

    frame_log = LabelFrame(frame_left, text="frame_log", height=100)
    frame_log.pack(side="top", fill="both")

    label_log = st.ScrolledText(frame_log, wrap=tk.WORD)
    label_log.config(highlightbackground='black', highlightthickness=1)
    label_log.pack(expand=True)

    # ####################################################  fram_data   ####################################################


    frame_data = Frame(frame_right)
    frame_data.pack(side="top", fill="both")

    frame_data_text = LabelFrame(frame_data, text="frame_data_text")
    frame_data_text.pack(side="left", fill="both")

    label_data = st.ScrolledText(frame_data_text, width=30, height=15, wrap=tk.WORD)
    label_data.config(highlightbackground='black', highlightthickness=1)
    label_data.pack()

    frame_data_graph = LabelFrame(frame_data, text="frame_data_graph")
    frame_data_graph.pack(side="left", fill="both", expand=True)

    image = PhotoImage(file="../images/img_1.png")  # 경로를 따로 지정하지 않으면 파일이 있는 위치를 가리킴.
    label_image = Label(frame_data_graph, image=image)
    label_image.pack()

    # ####################################################  frame_option  ####################################################


    frame_tmp = LabelFrame(frame_right, text="frame_option")
    frame_tmp.pack(side="top", fill="both")

    overlayCheck = IntVar()
    heatmapCheck = IntVar()
    saveCheck = IntVar()

    c_over = Checkbutton(frame_tmp, text="Overlay", variable=overlayCheck)
    c_over.pack(side="left")

    c_heat = Checkbutton(frame_tmp, text="Heatmap", variable=heatmapCheck)
    c_heat.pack(side="left")

    label_tmp = Label(frame_tmp, text='Result:')
    label_tmp.pack(side="left")

    label_result = Label(frame_tmp, text='total 40, wrong 23 [57.5%]')
    label_result.pack(side="left")

    c_heat = Checkbutton(frame_tmp, text="결과 저장", variable=saveCheck)
    c_heat.pack(side="right")


    # ####################################################  frame_visual ####################################################


    frame_visual = LabelFrame(frame_right, text="frame_visual")
    frame_visual.pack(side="top", fill="both")

    w2v = PhotoImage(file="../images/word2vec.png")  # 경로를 따로 지정하지 않으면 파일이 있는 위치를 가리킴.
    label_image = Label(frame_visual, image=w2v)
    label_image.pack(expand=True)

    root.mainloop()
