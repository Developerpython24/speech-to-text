import speech_recognition  as sr
import os
from farsi import convert

os.system("cls")

r = sr.Recognizer()

path_file = input("path/name.wav: ")
file = sr.AudioFile(path_file)


time_min = int(input("time min file: "))
time_sec = int(input("time sec file: "))
os.system("cls")
file_time = (time_min * 59) + time_sec
merge = ""
offs = 0
try:
    while offs <= file_time :
        with file as file_open:
            r.adjust_for_ambient_noise(file_open, duration= 1)
            audio = r.record(file_open, offset=offs , duration=30)
            try:
                print(convert("در حال تبدیل صدا به متن..."))
                my_text = r.recognize_google(audio, languge= "fa-IR")
                os.system("cls")
                merge = merge + " " + my_text
                print("=======================")
                print(convert(merge))
                print("=======================")
                offs = offs + 20
                if offs <= file_time :
                    print(str(offs)+ "s" + "/"+ str(file_time)+ "s")
                else:
                    print(convert(" عملیات با موفقیت انجام شد."))
            except Exception as er:# نوع خطا را در اینجا بجایاین خط میتوان نوشتن
                print(type(er))# نشان می دهند ارور از چه نوعی است.
                os.system("cls")
                print(convert("در حال تلاش مجدد...."))
                print("=======================")
                print(convert(merge))
                print("=======================")
                offs = offs + 20
                if offs <= file_time :
                    print(str(offs)+ "s" + "/"+ str(file_time)+ "s")
                else:
                    print(convert(" عملیات با موفقیت انجام شد."))
except Exception as er:
    print(type(er))