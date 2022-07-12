import time
from tkinter import *
from tkinter.filedialog import askopenfile
from googletrans import Translator
import speech_recognition as sr


class Transcriber:

    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.stopper = None
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration=1)

    def start_rec(self, ln):
        print("recording")

        with self.mic as source:
            audio = self.r.listen(source, phrase_time_limit=10)

        print('processing')
        # Process label

        t = self.r.recognize_google(audio, language=ln)
        print(t)
        return t

    def audio_transcribe(self, path, ln):
        audio_file = sr.AudioFile(path)
        with audio_file as source:
            self.r.adjust_for_ambient_noise(source, duration=1)
            audio = self.r.record(source)
        t = self.r.recognize_google(audio, language=ln)
        print(t)
        return t

trans = Transcriber()
translator = Translator()

root = Tk()
root.title("Transcription App")
root.configure(bg="#495C83")
languages = {"English": "en-IN", "Hindi": "hi-IN", "Spanish": "es-US", "Japanese": "ja-JP", "French": "fr-FR"}
i_lang = "en-IN"
d_lang = "en-IN"
i_2lang = "en-IN"
d_2lang = "en-IN"
fpath = None


def ilCB(s):
    global i_lang
    i_lang = languages[s]
    print(i_lang)


def dlCB(s):
    global d_lang
    d_lang = languages[s]
    print(d_lang)


def il2CB(s):
    global i_2lang
    i_2lang = languages[s]
    print(i_2lang)


def dl2CB(s):
    global d_2lang
    d_2lang = languages[s]
    print(d_2lang)


def open_file():
    global fpath
    file_path = askopenfile(mode='r', filetypes=[('mp3 audio', '*.mp4'),("wav audio","*.wav")])
    if file_path is not None:
        fpath = file_path.name


# heading
heading = Label(root, text="TRANSCRIBER APPLICATION", bg="#495C83", pady=20, padx=100, fg="#A8A4CE")
heading.grid(row=0, column=0, columnspan=6)
heading.configure(font=("castellar", 20, "underline", "bold"))

#
# microphone
#
mic_frame = LabelFrame(root, text="Microphone", height=230, width=445, bg="#7A86B6")
mic_frame.configure(font=("elephant", 16))
mic_frame.grid(row=1, column=0, columnspan=3)
mic_frame.grid_propagate(False)

space_lab = Label(mic_frame, padx=70, bg="#7A86B6")
space_lab.grid(row=2, column=0)

# input-menu
input_click = StringVar()
input_click.set("Select Any Language")

input_label = Label(mic_frame, text="Language to speak", fg="#2E4053", bg="#7A86B6")
input_label.configure(font=("cambria", 12))
input_label.grid(row=2, column=1)

input_lang = OptionMenu(mic_frame, input_click, *list(languages.keys()), command=ilCB)
input_lang.configure(bg="#C8B6E2")
input_lang.grid(row=3, column=1)

# space
space1 = Label(mic_frame, pady=5, bg="#7A86B6")
space1.grid(row=4, column=1)

# output-menu
output_click = StringVar()
output_click.set("Select Any Language")

input_label1 = Label(mic_frame, text="Language for output", fg="#2E4053", bg="#7A86B6")
input_label1.configure(font=("cambria", 12))
input_label1.grid(row=5, column=1)

output_lang = OptionMenu(mic_frame, output_click, *list(languages.keys()), command=dlCB)
output_lang.configure(bg="#C8B6E2")
output_lang.grid(row=6, column=1)

#
# audio-file
#
aud_frame = LabelFrame(root, text="Audio File", height=230, width=445, bg="#7A86B6")
aud_frame.configure(font=("elephant", 16))
aud_frame.grid(row=1, column=3, columnspan=3)
aud_frame.grid_propagate(False)

space_lab = Label(aud_frame, padx=70, bg="#7A86B6")
space_lab.grid(row=2, column=5)

# upload button
upload_label = Label(aud_frame, text="Select audio file", fg="#2E4053", bg="#7A86B6")
upload_label.configure(font=("cambria", 12))
upload_label.grid(row=2, column=6)

myButton = Button(aud_frame, command=open_file, text="Upload", bg="#C8B6E2")
myButton.grid(row=3, column=6)

# space
space2 = Label(aud_frame, pady=5, bg="#7A86B6")
space2.grid(row=4, column=6)

# input-menu
input_click2 = StringVar()
input_click2.set("Select Any Language")

input_label = Label(aud_frame, text="Language of Audio File", fg="#2E4053", bg="#7A86B6")
input_label.configure(font=("cambria", 12))
input_label.grid(row=5, column=6)

input_lang2 = OptionMenu(aud_frame, input_click2, *list(languages.keys()), command=il2CB)
input_lang2.configure(bg="#C8B6E2")
input_lang2.grid(row=6, column=6)

# output-menu
output_click2 = StringVar()
output_click2.set("Select Any Language")

output_label = Label(aud_frame, text="Language for output", fg="#2E4053", bg="#7A86B6")
output_label.configure(font=("cambria", 12))
output_label.grid(row=7, column=6)

output_lang2 = OptionMenu(aud_frame, output_click2, *list(languages.keys()),  command=dl2CB)
output_lang2.configure(bg="#C8B6E2")
output_lang2.grid(row=8, column=6)

# Output button
final_btn1 = Button(root,  text="Mic Capturing", fg="#2E4053", bg="#7A86B6", padx=100)
final_btn1.configure(font=("elephant", 12))
final_btn1.grid(row=8, column=0, columnspan=3)

# Output button aud-file
final_btn = Button(root, text="Audio-file Capturing", fg="#2E4053", bg="#7A86B6", padx=100)
final_btn.configure(font=("elephant", 12))
final_btn.grid(row=8, column=3, columnspan=3)
#

# trc text
src_frame = LabelFrame(root, text="Source text", height=175, width=445, bg="#7A86B6")
src_frame.configure(font=("elephant", 16))
src_frame.grid(row=11, column=0)
src_frame.grid_propagate(False)

src_text = Label(src_frame, text="Your source transcription will display here", wraplength=400, justify="left",
                 bg="#7A86B6", padx=20)
src_text.configure(font=("", 12, ""))
src_text.grid(row=11, column=0, sticky=W + E)

# dest text
dest_frame = LabelFrame(root, text="Destination Text", height=175, width=445, bg="#7A86B6")
dest_frame.configure(font=("elephant", 16))
dest_frame.grid(row=11, column=3)
dest_frame.grid_propagate(False)

dest_text = Label(dest_frame, text="Your destined transcription will display here", wraplength=400, justify="left",
                  bg="#7A86B6", padx=20)
dest_text.configure(font=("", 12, ""))
dest_text.grid(row=11, column=0, sticky=W + E)
# dest_text.pack()

# exit button
btn_exit = Button(root, text="EXIT", command=root.quit, padx=100, pady=10, fg="#2E4053", bg="#7A86B6")
btn_exit.configure(font=("elephant", 12))
btn_exit.grid(row=12, column=0, columnspan=6)

root.mainloop()