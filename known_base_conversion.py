import tkinter as tk
from tkinter import messagebox


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("590x100")
    root.title("known_base_conversion")
    conversion_heading_chinese = tk.Label(root, text="四个基本进制转换", fg="black", font=("黑体", 20))
    conversion_heading_english = tk.Label(root, text="four foundational jinzhi conversion", fg="black",
                                          font=("黑体", 10))
    conversion_heading_chinese.pack()  # 汉语标题
    conversion_heading_english.pack()  # 英语标题


    # -----------------------------------------------------------------------------------------------------二进制------------
    def binary_system(input_num, option):
        if option == "二进制/binary":
            binary = input_num
            return binary
        elif option == "八进制/octal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
                """将整数部分给left_part,可能存在的小数部分给right_part,不存在则right_part赋值为None"""
            engit_list = []
            for digit in left_part:
                binary_digit = bin(int(digit))[2:].zfill(3)
                engit_list.append(binary_digit)
            binary = "".join(engit_list)
            if right_part is not None:
                bin_fractional_part = ' '
                for digit in right_part:
                    bin_fractional_part += bin(int(digit, 8))[2:].zfill(3)
                binary = binary + '.' + bin_fractional_part
                return binary
            else:
                return binary
        elif option == "十进制/decimal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
                """将整数部分给left_part,可能存在的小数部分给right_part,不存在则right_part赋值为None"""
            binary = bin(int(left_part))[2:]
            if right_part is not None:
                bin_fractional_part = ' '
                while right_part:
                    right_part, remainder = str(float(right_part) * 2).split('.')
                    bin_fractional_part = str(int(remainder)) + bin_fractional_part
                binary = binary + '.' + bin_fractional_part
                return binary
            else:
                return binary
        elif option == "十六进制/hexadecimal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            binary = bin(int(left_part, 16))[2:]
            if right_part is not None:
                bin_fractional_part = ' '
                while right_part:
                    right_part, remainder = str(float(right_part) * 2).split('.')
                    bin_fractional_part = str(int(remainder)) + bin_fractional_part
                binary = binary + '.' + bin_fractional_part
                return binary
            else:
                return binary


    # -----------------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------八进制-------------------
    def octal_system(input_num, option):
        if option == "八进制/octal":
            octal = input_num
            return octal
        elif option == "二进制/binary":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
                integer_octal = int(left_part, 2)
                fractional_octal = '.' + ''.join(format(int(bit, 2), '03') for bit in right_part)
                octal = f"{integer_octal}{fractional_octal}"
                return octal
            else:
                octal = oct(int(input_num))
                return octal[2:]
        elif option == "十进制/decimal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            octal = oct(int(left_part))[2:]
            if right_part is not None:
                decimal_value = 0.0
                for bit in reversed(right_part):
                    decimal_value += int(bit) * (2 ** -len(right_part))
                while decimal_value > 0:
                    octal_digit = int(decimal_value * 8)
                    decimal_value -= octal_digit / 8
                octal = octal + '.' + right_part
                return octal
            else:
                return octal
        elif option == "十六进制/hexadecimal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            octal = oct((int(left_part, 16)))[2:]
            if right_part is not None:
                oct_fractional_part = ' '
                while right_part:
                    right_part, remainder = str(float(right_part) * 8).split('.')
                    oct_fractional_part = str(int(remainder)) + oct_fractional_part
                octal = octal + '.' + oct_fractional_part
                return octal
            else:
                return octal
    # -----------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------十进制---------------
    def decimal_system(input_num, option):
        if option == "十进制/decimal":
            decimal = input_num
            return decimal
        elif option == "二进制/binary":
            input_num = input_entry.get()
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            decimal = int(left_part, 2)
            if right_part is not None:
                rdecimal = 0
                for bit in right_part:
                    rdecimal = int(bit) * (2 ** -len(right_part))
                decimal = f"{decimal}.{rdecimal}"
                return decimal
            else:
                return decimal
        elif option == "八进制/octal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            decimal = int(left_part, 8)
            if right_part is not None:
                fraction = 0.0
                for bit in reversed(right_part):
                    fraction += int(bit) * (8 ** -len(right_part))
                decimal += fraction
                return decimal
            else:
                return decimal
        elif option == "十六进制/hexadecimal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            decimal = int(left_part, 16)
            if right_part is not None:
                dec_fractiona = 0
                for i, digit in enumerate(right_part):
                    dec_fractiona += int(digit, 16) * (16 ** (-i - 1))
                decimal = decimal + dec_fractiona
                return decimal
            else:
                return decimal
    # -------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------十六进制-------
    def hexadecimal_system(input_num, option):
        if option == "十六进制/hexadecimal":
            hexadecimal = input_num
            return hexadecimal
        elif option == "二进制/binary":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            hexadecimal = bin(int(left_part, 16))[2:]
            if right_part is not None:
                fraction = ' '
                while right_part:
                    fraction += str(int(fraction[-1], 16))
                    right_part = right_part[:-1]
                hexadecimal = hexadecimal + '.' + right_part
                return hexadecimal
            else:
                return hexadecimal
        elif option == "八进制/octal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            hexadecimal = oct(int(left_part, 16))[2:]
            if right_part is not None:
                fraction = ' '
                while right_part:
                    fraction += str(int(right_part[-1], 16))
                    right_part = right_part[:-1]
                hexadecimal = hexadecimal + '.' + right_part
                return hexadecimal
            else:
                return hexadecimal
        elif option == "十进制/decimal":
            if '.' in input_num:
                left_part, right_part = input_num.split(".")
            else:
                left_part = input_num
                right_part = None
            hexadecimal = int(left_part, 16)
            if right_part is not None:
                fraction = sum(int(digit, 16) * (16 ** -i) for i, digit in enumerate(right_part[::-1]))
                hexadecimal = f"{hexadecimal}.{fraction}"
                return hexadecimal
            else:
                return hexadecimal
    # ------------------------------------------------------------------------------------------------------------------
    def start_jinzhi_conversion(input_num, option):
        top = tk.Toplevel(root)  # 执行后新的显示结果的活动窗口
        try:
            label = tk.Label(top, text=f"""
                    二进制为/binary:  {binary_system(input_num, option)}
                    八进制为/octal:  {octal_system(input_num, option)}
                    十进制为/decimal:  {decimal_system(input_num,option)}
                    十六进制为/hexadecimal:  {hexadecimal_system(input_num,option)}""", justify="left")  # 输出结果
            label.pack()
        except ValueError:
            messagebox.showinfo("错误/error", "请重新输入/Please re-enter")

    cishuwei = tk.Label(root, text="输入的数为/The input number is：")
    var = tk.StringVar()
    var.set("十进制/decimal")
    jiantou = tk.Label(root, text="→", fg="black")
    menu = tk.OptionMenu(root, var, '二进制/binary', '八进制/octal', '十进制/decimal', '十六进制/hexadecimal')
    cishuwei.pack(side="left")
    menu.pack(side="left")
    jiantou.pack(side="left", padx=2)

    input_entry = tk.Entry()

    enter = tk.Button(root, text="确认/Enter",
                      command=lambda: start_jinzhi_conversion(input_entry.get(), var.get()))  # 输入数据后的确认执行按钮

    input_entry.pack(side="left")
    enter.pack(side="left", padx=10)

    root.mainloop()
