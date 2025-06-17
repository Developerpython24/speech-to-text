#import liberry
import speech_recognition # type: ignore
import os
from farsi import convert
#clear
os.system("cls")

# step two
r = speech_recognition.Recognizer()
#step three
mic = speech_recognition.Microphone()
#step four until ten
merge = ""
#دستسار صوتی
end = "پایان"
while True :
    with mic as mic_open :
        try:
            r.adjust_for_ambient_noise(mic_open , duration=0.5)
            print(convert(" لطفا صحبت کنید."))
            audio = r.listen(mic_open)
            my_text = r.recognize_google(audio , language = "fa-IR")
            os.system("cls")
            merge = merge +" "+ my_text
            if my_text == end :
                print("=====================")
                print(convert(merge))
                print("=====================")
                print(convert(" به امید دیدار."))
                input(convert("برای خروج یکی از کلید های  کیبورد را فشار دهید."))
                break
            
        except Exception as er :
            print(type(er))
            input(convert("برای خروج یکی از کلید های  کیبورد را فشار دهید."))
            break
        except OSError :
            print(convert(" وضعیت میکروفون خود را بررسی کنید."))
            input(convert("برای خروج یکی از کلید های  کیبورد را فشار دهید."))
            break
        except:
            print(convert(" برنامه با شکست مواجه شد."))
            input(convert("برای خروج یکی از کلید های  کیبورد را فشار دهید."))
            break