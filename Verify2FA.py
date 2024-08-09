from tkinter import *
import customtkinter  #pip install customtkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image #pip install Pillow
import qrcode
from VerifySQL import *


customtkinter.set_appearance_mode("Light")  #system (default), light, dark
customtkinter.set_default_color_theme("blue") #blue (default), dark-blue, green

bg= "#ebebeb"
StartTimedUpdates() #kişiye özel olan 'code' değerini 30 saniyede bir veritabanında günceller

class MainPage(customtkinter.CTk):
    def __init__(self,master=None):
        super().__init__()
        self.title("XXX Authenticator")
        self.geometry("840x480")
        self.resizable(width=False, height=False)
        #self.iconbitmap('assets/2fa16.ico')

        def VerifyCode():
            def UserCode():
                def Quit():
                    self.destroy()

                verifyFrame = Frame(master, relief=RIDGE, width=1280, height=720, bg=bg)
                verifyFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

                title1=customtkinter.CTkLabel(verifyFrame, text="XXX AUTHENTICATOR",font=("Arial", 22))
                title1.place(relx=0.5, rely=0.25, anchor=CENTER)

                name, lastname = UserNamePrint(mail)
                label1=customtkinter.CTkLabel(verifyFrame, text=f"Hoşgeldin {name} {lastname}",font=("Poplar Std", 18))
                label1.place(relx=0.5, rely=0.28, anchor=CENTER)

                xLogo = customtkinter.CTkImage(light_image=Image.open('assets/usera.png'),
                                        size=(162, 162))
                label2 = customtkinter.CTkLabel(verifyFrame, text="", image=xLogo)
                label2.place(relx=0.5, rely=0.435,anchor=CENTER)


                label3 = customtkinter.CTkLabel(verifyFrame, text=mail.lower(), font=('Poplar Std', 16, 'bold'))
                label3.place(relx=0.365, rely=0.548)

                label4Frame = customtkinter.CTkFrame(master=verifyFrame, height=30, width=350)
                label4Frame.place(relx=0.5, rely=0.61,anchor=CENTER)
                label4 = customtkinter.CTkLabel(label4Frame, text=UserCodePrint(mail,id),font=("Verdana", 22))
                label4.configure(text=UserCodePrint(mail,id))
                label4.place(relx=0.5, rely=0.5, anchor=CENTER)

                button = customtkinter.CTkButton(verifyFrame, text="Uygulamadan Çık",command=Quit)
                button.place(relx=0.5, rely=0.67, anchor=CENTER)

                directionLabel5 = customtkinter.CTkLabel(master=verifyFrame,
                                                    text="2FA kod ile uygulamaya giriş"
                                                         "\n yapabilirsiniz.", text_color="#3a7ebf")
                directionLabel5.place(relx=0.5, rely=0.72, anchor=CENTER)

                self.after(1000, UserCode)


            mail = mailEntry.get()
            id = idEntry.get()
            if mail and id:
                if VerifyID(mail,id):
                    print("Giriş başarılı.")
                    UserCode()
                else:
                    print("Doğrulama kodunuz veya E-Posta adresiniz yanlış.")
                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                     fg_color="#eae5ec")
                    wFrame.place(relx=0.4, rely=0.7, anchor=CENTER)
                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#e0d8e2")
                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#e0d8e2")
                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                    wLabel = customtkinter.CTkLabel(wFrame, text="Kurulum anahtarız veya E-Posta \nadresiniz yanlış.",
                                                     text_color="#584d5c")
                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
            else:
                print("Boş bırakmayın.")
                wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                fg_color="#eae5ec")
                wFrame.place(relx=0.4, rely=0.7, anchor=CENTER)
                wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#e0d8e2")
                wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#e0d8e2")
                wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                wLabel = customtkinter.CTkLabel(wFrame, text="Boş bırakmayın.",
                                                text_color="#584d5c")
                wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)


        frame = Frame(self, width=1280, height=720)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        logoImage = customtkinter.CTkImage(light_image=Image.open('assets/2fa.png'),
                                           size=(198, 198))
        logoLabel = customtkinter.CTkLabel(frame, text="", image=logoImage)
        logoLabel.place(relx=0.65, rely=0.5, anchor=CENTER)

        mailLabel = ttk.Label(frame, text="E-Posta", font="Arial 12 bold")
        mailLabel.place(relx=0.370, rely=0.38)

        mailEntry = ttk.Entry(frame,  font=("Arial 10"), width=35)
        mailEntry.place(relx=0.4, rely=0.43,anchor=CENTER)

        idLabel = ttk.Label(frame, text="Kurulum Anahtarı", font="Arial 12 bold")
        idLabel.place(relx=0.340, rely=0.5)

        idEntry = ttk.Entry(frame,  font=("Arial 10"), width=35, show="*")
        idEntry.place(relx=0.4, rely=0.55,anchor=CENTER)

        button = customtkinter.CTkButton(frame, text="Onayla",command=VerifyCode)
        button.place(relx=0.4, rely=0.6,anchor=CENTER)


if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
