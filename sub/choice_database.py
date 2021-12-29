# sub.choice_database.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from sub.h2_config import H2Config
from sub.postgresql_config import PostgresqlConfig
from sub.ini_config import *

# Radiobutton Globals
var_db_1 = "Postgresql"
var_db_2 = "H2"
var_db_3 = "Maria"


class ChoiceDatabase:

    def __init__(self, parent, *args, **kwargs):
        self.myParent = parent
        self.sub_win = tk.Toplevel()
        self.sub_win.resizable(False, False)
        self.sub_win.title('Database 선택')

        self.frm_main = tk.Frame(self.sub_win, borderwidth=10, width=250)
        self.frm_main.pack(side="top", fill="both")

    # Database 선택
    def choice_database(self):

        """
        버튼 영역
        """
        # 종료 버튼 클릭
        def on_close():
            yn = messagebox.askquestion(title="Exit Application", message="프로그램을 종료 하시겠습니까 ?.", parent=self.sub_win)
            if yn == 'yes':
                self.myParent.main_destroy()
            else:
                return

        # 확인 버튼 클릭
        def on_confirm():
            if not str_ip.get():
                messagebox.showwarning(title="경고", message="Host IP 은(는) 필수 입력 항목 입니다.", parent=self.sub_win)
                return
            if not str_port.get():
                messagebox.showwarning(title="경고", message="Port 은(는) 필수 입력 항목 입니다.", parent=self.sub_win)
                return
            if not str_id.get():
                messagebox.showwarning(title="경고", message="User ID 은(는) 필수 입력 항목 입니다.", parent=self.sub_win)
                return
            if not str_pw.get():
                messagebox.showwarning(title="경고", message="Password 은(는) 필수 입력 항목 입니다.", parent=self.sub_win)
                return
            if not str_nm.get():
                messagebox.showwarning(title="경고", message="DB Name 은(는) 필수 입력 항목 입니다.", parent=self.sub_win)
                return

            var_rdo_sel = rdo_db_type.get()
            test = None
            if var_rdo_sel == 1:
                test = PostgresqlConfig(str_ip.get(), str_port.get(), str_id.get(), str_pw.get(), str_nm.get())
            elif var_rdo_sel == 2:
                test = H2Config(str_ip.get(), str_port.get(), str_id.get(), str_pw.get(), str_nm.get())
            elif var_rdo_sel == 3:
                # todo test = MariaConfig(str_ip.get(), str_port.get(), str_id.get(), str_pw.get(), str_nm.get())
                messagebox.showinfo(title="메시지", message="미구현", parent=self.sub_win)
                return

            yn = test.connection_test()
            if yn:
                messagebox.showinfo(title="메시지", message="접속 성공.", parent=self.sub_win)
                self.myParent.set_data_info(str_ip.get(), str_port.get(), str_id.get(), str_pw.get(), str_nm.get())
                self.sub_win.destroy()
            else:
                messagebox.showinfo(title="메시지", message="접속 실패.", parent=self.sub_win)
                return

        btn_confirm = tk.Button(self.frm_main, text="확인", overrelief="solid", width=15, command=on_confirm)
        btn_confirm.pack(side="top", fill="none", anchor="e")
        btn_close = tk.Button(self.frm_main, text="종료", overrelief="solid", width=15, command=on_close)
        btn_close.pack(side="top", fill="none", anchor="e")

        '''
        DB 를 선택한다.
        '''
        # We are creating a container frame to hold all other widgets
        mighty1 = ttk.LabelFrame(self.frm_main, text=' Database 선택 하세요 ')
        mighty1.pack(side="top", fill="both", padx=5, pady=10, ipadx=10, ipady=5)

        # Radiobutton Callback
        def radio_call():
            var_rdo_sel = rdo_db_type.get()
            db_info = None
            if var_rdo_sel == 1:
                db_info = get_ini_config(var_db_1)          # config - Database 정보 Call
            elif var_rdo_sel == 2:
                db_info = get_ini_config(var_db_2)          # config - Database 정보 Call
            elif var_rdo_sel == 3:
                db_info = get_ini_config(var_db_3)          # config - Database 정보 Call

            str_ip.set(db_info["ip"])
            str_port.set(db_info["port"])
            str_nm.set(db_info["name"])
            str_id.set(db_info["user"])
            str_pw.set(db_info["passwd"])

        # create three Radio buttons using one variable
        rdo_db_type = tk.IntVar()

        rad1 = tk.Radiobutton(mighty1, text=var_db_1, variable=rdo_db_type, value=1, command=radio_call, width=20)
        rad1.grid(column=0, row=0)

        rad2 = tk.Radiobutton(mighty1, text=var_db_2, variable=rdo_db_type, value=2, command=radio_call, width=20)
        rad2.grid(column=1, row=0)

        rad3 = tk.Radiobutton(mighty1, text=var_db_3, variable=rdo_db_type, value=3, command=radio_call, width=20)
        rad3.grid(column=2, row=0)

        '''
        DB 정보를 등록한다.
        '''
        # We are creating a container frame to hold all other widgets
        mighty2 = ttk.LabelFrame(self.frm_main, text=' Database 정보 ')
        mighty2.pack(side="top", fill="both", padx=5, pady=5, ipadx=10, ipady=10)

        lbl_temp_1 = ttk.Label(mighty2, width=20)
        lbl_temp_1.pack(side="left")
        lbl_temp_2 = ttk.Label(mighty2)
        lbl_temp_2.pack(side="left")

        # Modify adding a Label using mighty as the parent instead of win
        lbl_ip = ttk.Label(lbl_temp_1, text="Host IP : ")
        lbl_ip.pack(side="top", anchor="e", padx=5, pady=5)
        lbl_port = ttk.Label(lbl_temp_1, text="Port : ")
        lbl_port.pack(side="top", anchor="e", padx=5, pady=5)
        lbl_nm = ttk.Label(lbl_temp_1, text="DB Name : ")
        lbl_nm.pack(side="top", anchor="e", padx=5, pady=5)
        lbl_id = ttk.Label(lbl_temp_1, text="User ID : ")
        lbl_id.pack(side="top", anchor="e", padx=5, pady=5)
        lbl_pw = ttk.Label(lbl_temp_1, text="Password : ")
        lbl_pw.pack(side="top", anchor="e", padx=5, pady=5)

        # Adding a Textbox Entry widget
        str_ip = tk.StringVar()
        str_ip_entered = ttk.Entry(lbl_temp_2, textvariable=str_ip, width=40)
        str_ip_entered.pack(side="top", fill="both", padx=5, pady=5)
        str_port = tk.StringVar()
        str_port_entered = ttk.Entry(lbl_temp_2, textvariable=str_port, width=40)
        str_port_entered.pack(side="top", fill="both", padx=5, pady=5)
        str_nm = tk.StringVar()
        str_nm_entered = ttk.Entry(lbl_temp_2, textvariable=str_nm)
        str_nm_entered.pack(side="top", fill="both", padx=5, pady=5)
        str_id = tk.StringVar()
        str_id_entered = ttk.Entry(lbl_temp_2, textvariable=str_id)
        str_id_entered.pack(side="top", fill="both", padx=5, pady=5)
        str_pw = tk.StringVar()
        str_pw_entered = ttk.Entry(lbl_temp_2, textvariable=str_pw)
        str_pw_entered.pack(side="top", fill="both", padx=5, pady=5)

        self.sub_win.attributes('-topmost', 'true')
        self.sub_win.grab_set()
