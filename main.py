import customtkinter as ctk
from tkinter import colorchooser
from colormath.color_objects import CMYKColor, LabColor, HSVColor
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor

# Функции для перевода
def cmyk_to_lab_hsv(cmyk_color):
    lab = convert_color(cmyk_color, LabColor)
    hsv = convert_color(cmyk_color, HSVColor)
    return lab, hsv

def hsv_to_cmyk_lab(hsv_color):
    cmyk = convert_color(hsv_color, CMYKColor)
    lab = convert_color(hsv_color, LabColor)
    return cmyk, lab

def lab_to_cmyk_hsv(lab_color):
    cmyk = convert_color(lab_color, CMYKColor)
    hsv = convert_color(lab_color, HSVColor)
    return cmyk, hsv

# Приложение
class ColorConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Color Converter App")
        self.geometry("600x600")
        
        # Кнопки выбора цветовых систем (расположены в одну строку)
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)
        
        self.cmyk_btn = ctk.CTkButton(self.button_frame, text="CMYK", command=self.set_cmyk)
        self.cmyk_btn.grid(row=0, column=0, padx=10)

        self.hsv_btn = ctk.CTkButton(self.button_frame, text="HSV", command=self.set_hsv)
        self.hsv_btn.grid(row=0, column=1, padx=10)

        self.lab_btn = ctk.CTkButton(self.button_frame, text="Lab", command=self.set_lab)
        self.lab_btn.grid(row=0, column=2, padx=10)

        # Цветовое колесо
        self.color_wheel_btn = ctk.CTkButton(self, text="Выбрать цвет", command=self.choose_color)
        self.color_wheel_btn.pack(pady=10)

        # Ползунки для каждой системы
        self.sliders_frame = ctk.CTkFrame(self)
        self.sliders_frame.pack(pady=20)

        self.slider1 = ctk.CTkSlider(self.sliders_frame, from_=0, to=1, command=self.update_color_from_sliders)
        self.slider1_label = ctk.CTkLabel(self.sliders_frame, text="Параметр 1")
        self.slider1_label.grid(row=0, column=0, padx=10)
        self.slider1.grid(row=0, column=1, padx=10)

        self.slider2 = ctk.CTkSlider(self.sliders_frame, from_=0, to=1, command=self.update_color_from_sliders)
        self.slider2_label = ctk.CTkLabel(self.sliders_frame, text="Параметр 2")
        self.slider2_label.grid(row=1, column=0, padx=10)
        self.slider2.grid(row=1, column=1, padx=10)

        self.slider3 = ctk.CTkSlider(self.sliders_frame, from_=0, to=1, command=self.update_color_from_sliders)
        self.slider3_label = ctk.CTkLabel(self.sliders_frame, text="Параметр 3")
        self.slider3_label.grid(row=2, column=0, padx=10)
        self.slider3.grid(row=2, column=1, padx=10)

        self.slider4 = ctk.CTkSlider(self.sliders_frame, from_=0, to=1, command=self.update_color_from_sliders)
        self.slider4_label = ctk.CTkLabel(self.sliders_frame, text="Параметр 4 (только CMYK)")
        self.slider4_label.grid(row=3, column=0, padx=10)
        self.slider4.grid(row=3, column=1, padx=10)

        # Текстовые поля для ввода значений
        self.text_inputs_frame = ctk.CTkFrame(self)
        self.text_inputs_frame.pack(pady=10)

        self.text1 = ctk.CTkEntry(self.text_inputs_frame, placeholder_text="Параметр 1", width=100)
        self.text1.grid(row=0, column=0, padx=10)
        self.text1.bind('<KeyRelease>', self.update_sliders_from_text)

        self.text2 = ctk.CTkEntry(self.text_inputs_frame, placeholder_text="Параметр 2", width=100)
        self.text2.grid(row=0, column=1, padx=10)
        self.text2.bind('<KeyRelease>', self.update_sliders_from_text)

        self.text3 = ctk.CTkEntry(self.text_inputs_frame, placeholder_text="Параметр 3", width=100)
        self.text3.grid(row=0, column=2, padx=10)
        self.text3.bind('<KeyRelease>', self.update_sliders_from_text)

        self.text4 = ctk.CTkEntry(self.text_inputs_frame, placeholder_text="Параметр 4 (только CMYK)", width=100)
        self.text4.grid(row=0, column=3, padx=10)
        self.text4.bind('<KeyRelease>', self.update_sliders_from_text)

        # Лейбл для вывода результата
        self.result_label = ctk.CTkLabel(self, text="Результаты перевода", justify='left')
        self.result_label.pack(pady=20, side="bottom")

    def set_cmyk(self):
        # Устанавливаем настройки для CMYK
        self.slider1_label.configure(text="C (Cyan)")
        self.slider2_label.configure(text="M (Magenta)")
        self.slider3_label.configure(text="Y (Yellow)")
        self.slider4_label.configure(state="normal", text="K (Black)")
        self.slider1.configure(from_=0, to=1)
        self.slider2.configure(from_=0, to=1)
        self.slider3.configure(from_=0, to=1)
        self.slider4.configure(from_=0, to=1)
        self.text4.configure(state="normal")

    def set_hsv(self):
        # Устанавливаем настройки для HSV
        self.slider1_label.configure(text="H (Hue)")
        self.slider2_label.configure(text="S (Saturation)")
        self.slider3_label.configure(text="V (Value)")
        self.slider4_label.configure(state="disabled", text="N/A")
        self.slider1.configure(from_=0, to=360)
        self.slider2.configure(from_=0, to=1)
        self.slider3.configure(from_=0, to=1)
        self.text4.configure(state="disabled")

    def set_lab(self):
        # Устанавливаем настройки для Lab
        self.slider1_label.configure(text="L (Lightness)")
        self.slider2_label.configure(text="a (Red-Green)")
        self.slider3_label.configure(text="b (Blue-Yellow)")
        self.slider4_label.configure(state="disabled", text="N/A")
        self.slider1.configure(from_=0, to=100)
        self.slider2.configure(from_=-128, to=127)
        self.slider3.configure(from_=-128, to=127)
        self.text4.configure(state="disabled")

    

    def choose_color(self):
        # Выбор цвета через цветовое колесо
        rgb_color = colorchooser.askcolor()[0]  # Возвращает RGB в формате (R, G, B)
        
        if rgb_color:
            r, g, b = rgb_color

            # Преобразуем RGB в объект sRGBColor
            srgb = sRGBColor(r/255, g/255, b/255)

            # Преобразование из sRGB в CMYK, HSV и Lab
            cmyk = convert_color(srgb, CMYKColor)
            hsv = convert_color(srgb, HSVColor)
            lab = convert_color(srgb, LabColor)

            # Формируем текст для вывода результатов
            result_text = (f"RGB: {int(r)}, {int(g)}, {int(b)}\n"
                        f"CMYK: {round(cmyk.cmyk_c, 2)}, {round(cmyk.cmyk_m, 2)}, {round(cmyk.cmyk_y, 2)}, {round(cmyk.cmyk_k, 2)}\n"
                        f"HSV: {round(hsv.hsv_h, 2)}, {round(hsv.hsv_s, 2)}, {round(hsv.hsv_v, 2)}\n"
                        f"Lab: {round(lab.lab_l, 2)}, {round(lab.lab_a, 2)}, {round(lab.lab_b, 2)}")

            # Обновляем текст результата
            self.result_label.configure(text=result_text)

    def update_color_from_sliders(self, value=None):
        # Обновление текста в зависимости от изменения ползунков
        self.text1.delete(0, 'end')
        self.text1.insert(0, str(round(self.slider1.get(), 2)))

        self.text2.delete(0, 'end')
        self.text2.insert(0, str(round(self.slider2.get(), 2)))

        self.text3.delete(0, 'end')
        self.text3.insert(0, str(round(self.slider3.get(), 2)))

        if self.slider4_label.cget('state') != "disabled":
            self.text4.delete(0, 'end')
            self.text4.insert(0, str(round(self.slider4.get(), 2)))

        self.update_result()

    def update_sliders_from_text(self, event=None):
        # Обновление ползунков в зависимости от изменения текста
        try:
            self.slider1.set(float(self.text1.get()))
            self.slider2.set(float(self.text2.get()))
            self.slider3.set(float(self.text3.get()))

            if self.text4.cget('state') != "disabled":
                self.slider4.set(float(self.text4.get()))
        except ValueError:
            pass

        self.update_result()

    def update_result(self):
        try:
            # Получаем значения слайдеров
            param1 = float(self.text1.get())
            param2 = float(self.text2.get())
            param3 = float(self.text3.get())
            param4 = float(self.text4.get()) if self.text4.cget('state') != "disabled" else None

            if self.slider1_label.cget("text").startswith("C"):
                # CMYK -> Lab и HSV
                cmyk = CMYKColor(param1, param2, param3, param4)
                lab, hsv = cmyk_to_lab_hsv(cmyk)
                result_text = (f"CMYK: {round(param1, 2)}, {round(param2, 2)}, {round(param3, 2)}, {round(param4, 2)}\n"
                            f"Lab: {round(lab.lab_l, 2)}, {round(lab.lab_a, 2)}, {round(lab.lab_b, 2)}\n"
                            f"HSV: {round(hsv.hsv_h, 2)}, {round(hsv.hsv_s, 2)}, {round(hsv.hsv_v, 2)}")

            elif self.slider1_label.cget("text").startswith("H"):
                # HSV -> CMYK и Lab
                hsv = HSVColor(param1, param2, param3)
                cmyk, lab = hsv_to_cmyk_lab(hsv)
                result_text = (f"HSV: {round(param1, 2)}, {round(param2, 2)}, {round(param3, 2)}\n"
                            f"CMYK: {round(cmyk.cmyk_c, 2)}, {round(cmyk.cmyk_m, 2)}, {round(cmyk.cmyk_y, 2)}, {round(cmyk.cmyk_k, 2)}\n"
                            f"Lab: {round(lab.lab_l, 2)}, {round(lab.lab_a, 2)}, {round(lab.lab_b, 2)}")

            elif self.slider1_label.cget("text").startswith("L"):
                # Lab -> CMYK и HSV
                lab = LabColor(param1, param2, param3)
                cmyk, hsv = lab_to_cmyk_hsv(lab)
                result_text = (f"Lab: {round(param1, 2)}, {round(param2, 2)}, {round(param3, 2)}\n"
                            f"CMYK: {round(cmyk.cmyk_c, 2)}, {round(cmyk.cmyk_m, 2)}, {round(cmyk.cmyk_y, 2)}, {round(cmyk.cmyk_k, 2)}\n"
                            f"HSV: {round(hsv.hsv_h, 2)}, {round(hsv.hsv_s, 2)}, {round(hsv.hsv_v, 2)}")

            # Обновляем текст результата
            self.result_label.configure(text=result_text)

        except ValueError:
            # Если введены некорректные значения
            self.result_label.configure(text="Ошибка: введите правильные числовые значения.")


# Запуск приложения
app = ColorConverterApp()
app.mainloop()
