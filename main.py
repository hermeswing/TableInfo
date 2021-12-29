# main.py
import tkinter as tk
from tkinter import ttk

from sub.choice_database import ChoiceDatabase
from sub.postgresql_config import PostgresqlConfig


class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.tree_1 = None
        self.tree_2 = None
        self.database = None
        self.parent = parent
        parent.resizable(True, True)
        parent.geometry('1000x700+100+100')

        popup = ChoiceDatabase(self)
        popup.choice_database()

    def on_double_click(self, event):
        item = self.tree_1.selection()
        for i in item:
            print("you clicked on", self.tree_1.item(i, "values")[0])

            rows = self.database.get_column_list(self.tree_1.item(i, "values")[0])
            for row in rows:
                print(row)
                self.tree_2.insert("", "end", values=row)

    # todo 일단 Postgresql에만 연결.
    def set_data_info(self, ip, port, user_id, pass_word, nm):
        # Main Frame 생성
        top_frame = tk.Frame(self.parent, borderwidth=5)
        top_frame.pack(side="top", fill="both")
        # Main Frame > Left Frame 생성
        left_frame = tk.Frame(top_frame, borderwidth=5)
        left_frame.pack(side="left", fill="none")

        self.tree_1 = ttk.Treeview(left_frame, columns=["1"], displaycolumns=[1], show='headings')
        self.tree_1.heading(1, text="Table")
        self.tree_1.column(1, anchor="w")

        self.tree_1.pack()

        self.database = PostgresqlConfig(ip, port, user_id, pass_word, nm)
        rows = self.database.get_table_list()
        for row in rows:
            print(row)
            self.tree_1.insert("", "end", values=row)

        self.tree_1.bind("<Double-1>", self.on_double_click)

        # Main Frame > Right Frame 생성
        right_frame = tk.Frame(top_frame, borderwidth=5)
        right_frame.pack(side="right", fill="none")

        self.tree_2 = ttk.Treeview(right_frame, columns=["1", "2", "3", "4", "5"], displaycolumns=[1, 2, 3, 4, 5],
                                   show='headings')
        self.tree_2.heading(1, text="No")
        self.tree_2.column(1, anchor="w")
        self.tree_2.heading(2, text="Column")
        self.tree_2.column(2, anchor="w")
        self.tree_2.heading(3, text="Type")
        self.tree_2.column(3, anchor="w")
        self.tree_2.heading(4, text="Length")
        self.tree_2.column(4, anchor="w")
        self.tree_2.heading(5, text="Comment")
        self.tree_2.column(5, anchor="w")
        self.tree_2.pack()

    # Main 창 닫기
    def main_destroy(self):
        self.parent.destroy()


# 함수 선언과 구분을 위해 2줄 띄워야 함.
if __name__ == "__main__":
    main = tk.Tk()
    # main.title = "테이블 정보"
    MainApp(main).pack()
    main.mainloop()
