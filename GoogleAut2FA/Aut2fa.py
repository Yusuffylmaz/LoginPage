#Verimli çalışmıyor. Stajın başlangıcında yapılmıştır
from tkinter import *
import customtkinter  #pip install customtkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image #pip install Pillow
from Aut2faSQL import *

import smtplib
import ssl
from email.message import EmailMessage

import time
import pyotp #pip install pyotp
import qrcode

customtkinter.set_appearance_mode("Light")  #system (default), light, dark
customtkinter.set_default_color_theme("blue") #blue (default), dark-blue, green


keyy= str('234567abcdefghij') #pyotp.random_base32()


class registerPage(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Kaydol")
        self.geometry("800x480")
        self.resizable(width=False, height=False)


        def verify():
            totp = pyotp.TOTP(keyy)
            print(totp.now())
            uri = pyotp.totp.TOTP(keyy).provisioning_uri(name=mailEntry.get(), issuer_name="Mavi Bilişim")
            a = 'qr.png'
            qrcode.make(uri).save(a)
            print(keyy)


            frame = customtkinter.CTkFrame(self, width=1200, height=600, fg_color="white")
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            titleLabel = customtkinter.CTkLabel(master=frame, text='Authenticator', font=('Stencil Std', 25, 'bold'))
            titleLabel.place(relx=0.32, rely=0.1)

            talimat1Label = customtkinter.CTkLabel(master=frame,
                                                   text='• Google Authenticator uygulamasını kurun',
                                                   font=('Poplar Std', 16))
            talimat1Label.place(relx=0.35, rely=0.15)

            talimat2Label = customtkinter.CTkLabel(master=frame, text='• Google Authenticator uygulamasından + öğesine dokunun',
                                                   font=('Poplar Std', 16))
            talimat2Label.place(relx=0.35, rely=0.19)

            talimat3Label = customtkinter.CTkLabel(master=frame, text="• QR kodunu tara'yı seçin",
                                                   font=('Poplar Std', 16))
            talimat3Label.place(relx=0.35, rely=0.23)

            qrImage = customtkinter.CTkImage(light_image=Image.open(a),
                                             size=(200, 200))
            qrLabel = customtkinter.CTkLabel(master=frame, text="", image=qrImage)
            qrLabel.place(relx=0.5, rely=0.45, anchor=CENTER)

            tokenLabel = customtkinter.CTkLabel(master=frame, text='TOKEN', font=('Poplar Std', 16, 'bold'),
                                                text_color="#3a7ebf")
            tokenLabel.place(relx=0.35, rely=0.612)
            qrFrame = customtkinter.CTkFrame(master=frame, height=30, width=350)
            qrFrame.place(relx=0.35, rely=0.65)
            qrLabel = customtkinter.CTkLabel(master=qrFrame, text=keyy, font=('helvetica', 16, 'bold'))
            qrLabel.place(relx=0.5, rely=0.48, anchor=CENTER)

            uyariLabel = customtkinter.CTkLabel(master=frame,
                                                text="Kurulumu bitirdikten sonra uygulamaya "
                                                     "\ngiriş yapabilirsiniz.", text_color="#3a7ebf")
            uyariLabel.place(relx=0.5, rely=0.82, anchor=CENTER)

            def tamam():
                frame.destroy()

            tamamButton = customtkinter.CTkButton(master=frame, text="Tamam", width=170, command=tamam)
            tamamButton.place(relx=0.5, rely=0.75, anchor=CENTER)


        def contract():
            cntrct = Toplevel(master)
            cntrct.title("Okudum kabul ediyorum")
            cntrct.geometry("400x250")
            cntrct.mainloop()


        def register():
            name = nameEntry.get()
            lastname = lastnameEntry.get()
            mail = mailEntry.get()
            password = passwordEntry.get()
            passwordRepeat = passwordRepeatEntry.get()
            check = checkStr.get()

            conn = sql.connect("kaydol.db")
            cursor = conn.cursor()

            findMail = "SELECT * FROM kaydol WHERE eposta = ?"
            cursor.execute(findMail, [(mailEntry.get())])
            result = cursor.fetchall()

            if name and lastname and mail and password and passwordRepeat:
                if password == passwordRepeat:
                    if result:
                        print("Bu email zaten kayıtlı.")
                    else:
                        if check == "Accepted":
                            insert(name, lastname, mail, password)
                            verify()
                            #print("Kayıt işlemi başarılı.")
                        else:
                            print("Sözleşmeyi kabul ediniz.")
                else:
                    print("Şifreniz eşleşmiyor.")
            else:
                print("Boş bırakmayın.")

        frame = Frame(self, relief=RIDGE, bd=3, width=800, height=480)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        logoLabel = Label(frame, text="Kaydol", font="Arial 24 bold")
        logoLabel.place(relx=0.44, rely=0.13)

        nameEntry = customtkinter.CTkEntry(frame, placeholder_text="İsim", width=150, height=23, border_width=0,
                                            corner_radius=3)
        nameEntry.place(relx=0.3, rely=0.3)

        lastnameEntry = customtkinter.CTkEntry(frame, placeholder_text="Soyisim", width=150, height=23, border_width=0,
                                                corner_radius=3)
        lastnameEntry.place(relx=0.55, rely=0.3)

        mailEntry = customtkinter.CTkEntry(frame, placeholder_text="E-Posta Adresiniz", width=350, height=23,
                                            border_width=0, corner_radius=3)
        mailEntry.place(relx=0.3, rely=0.4)

        passwordEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifre", width=150, height=23, border_width=0,
                                                corner_radius=3)
        passwordEntry.place(relx=0.3, rely=0.5)

        passwordRepeatEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifreyi Onaylayın", width=150, height=23,
                                                       border_width=0, corner_radius=3)
        passwordRepeatEntry.place(relx=0.55, rely=0.5)

        passwordForgetEntry = Button(frame, text="***** okudum kabul ediyorum.", borderwidth=0,
                                       font="Verdana 8 underline",command=contract)
        passwordForgetEntry.place(relx=0.325, rely=0.58)

        checkStr = StringVar(value="Not Accepted")
        checkbox = ttk.Checkbutton(frame, variable=checkStr, onvalue="Accepted", offvalue="Not Accepted")
        checkbox.place(relx=0.3, rely=0.58)

        registerButton = customtkinter.CTkButton(frame, text="Kaydol", command=register)
        registerButton.place(relx=0.564, rely=0.65)


class forgotPassword(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Şifre mi unuttum")
        self.geometry("410x250")
        self.resizable(width=False, height=False)

        def verify():
            totp = pyotp.TOTP(keyy)
            print(totp.now())
            print(keyy)

            def a():
                if verifyEntry.get() == totp.now():
                    print("Şifreniz değiştirildi")
                else:
                    print("hatalı kod")

            controlPage = Toplevel(master)
            controlPage.title("Doğrulama")
            controlPage.geometry("410x250")
            controlPage.resizable(width=False, height=False)

            verifyFrame = Frame(master=controlPage, relief=RIDGE, bd=3, width=400, height=240)
            verifyFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

            verifyEntry = customtkinter.CTkEntry(master=controlPage, placeholder_text="2FA", width=120, height=30,
                                                 border_width=0, corner_radius=3, font=("Verdana", 20))
            verifyEntry.place(relx=0.5, rely=0.35, anchor=CENTER)

            verifyLabel = customtkinter.CTkLabel(master=controlPage,
                                                 text="Authenticator adresine gelen doğrulama kodunu giriniz.",
                                                 font=("Verdana", 10))
            verifyLabel.place(relx=0.5, rely=0.85, anchor=CENTER)

            verifyButton = customtkinter.CTkButton(master=controlPage, text="Onayla", height=25, width=75,
                                                   command=a)
            verifyButton.place(relx=0.40, rely=0.50)


        def changePassword():
            password = passwordEntry.get()
            passwordRepeat = passwordRepeatEntry.get()
            mail = mailEntry.get()

            conn = sql.connect("kaydol.db")
            cursor = conn.cursor()
            findMail = "select * from kaydol where eposta=?"
            cursor.execute(findMail, [(mail)])
            result = cursor.fetchone()

            if mail and password and passwordRepeat:
                if password == passwordRepeat:
                    if result:
                        query = "update kaydol set sifre=? where eposta = ?"
                        cursor.execute(query, [password, mail])
                        conn.commit()
                        conn.close()
                        verify()
                        #print("Şifreniz değişti.")
                    else:
                        print("E-posta adresiniz yanlış.")

                else:
                    print("Şifreniz eşleşmiyor.")
            else:
                print("Boş bırakmayın.")


        frame = Frame(self, relief=RIDGE, bd=3, width=400, height=240)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        logoLabel = Label(frame, text="Yeni Şifre Oluştur", font="Arial 14 bold")
        logoLabel.place(relx=0.24, rely=0.10)

        mailEntry = customtkinter.CTkEntry(frame, placeholder_text="E-Posta Adresiniz", width=270, height=24,
                                                    border_width=0, corner_radius=3)
        mailEntry.place(relx=0.1, rely=0.30)

        passwordEntry = customtkinter.CTkEntry(frame, placeholder_text="Yeni şifre", width=120, height=24, border_width=0,
                                          corner_radius=3)
        passwordEntry.place(relx=0.1, rely=0.52)

        passwordRepeatEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifreyi doğrula", width=120, height=24,
                                                 border_width=0, corner_radius=3)
        passwordRepeatEntry.place(relx=0.48, rely=0.52)

        changeButton = customtkinter.CTkButton(frame, text="Şifreyi değiştir", command=changePassword)
        changeButton.place(relx=0.44, rely=0.72)


class mainPage(customtkinter.CTk):
    def __init__(self,master=None):
        super().__init__()
        self.title("Giriş Yap")
        self.geometry("800x480")
        self.resizable(width=False, height=False)


        def verify():
            totp = pyotp.TOTP(keyy)
            print(totp.now())
            print(keyy)

            def a():
                if verifyEntry.get() == totp.now():
                    print("giriş başarılı")
                else:
                    print("hatalı kod")

            controlPage = Toplevel(master)
            controlPage.title("Doğrulama")
            controlPage.geometry("410x250")
            controlPage.resizable(width=False, height=False)

            verifyFrame = Frame(master=controlPage, relief=RIDGE, bd=3, width=400, height=240)
            verifyFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

            verifyEntry = customtkinter.CTkEntry(master=controlPage, placeholder_text="2FA", width=120, height=30,
                                                 border_width=0, corner_radius=3, font=("Verdana", 20))
            verifyEntry.place(relx=0.5, rely=0.35, anchor=CENTER)

            verifyLabel = customtkinter.CTkLabel(master=controlPage,
                                                 text="Authenticator adresine gelen doğrulama kodunu giriniz.",
                                                 font=("Verdana", 10))
            verifyLabel.place(relx=0.5, rely=0.85, anchor=CENTER)

            verifyButton = customtkinter.CTkButton(master=controlPage, text="Onayla", height=25, width=75,
                                                   command=a)
            verifyButton.place(relx=0.40, rely=0.50)




        def login():
            conn = sql.connect("kaydol.db")
            cursor = conn.cursor()

            find_mail = "SELECT * FROM kaydol WHERE eposta = ? and sifre = ?"
            cursor.execute(find_mail, [(usernameStr.get()), passwordStr.get()])
            result = cursor.fetchall()

            username = usernameStr.get()
            password = passwordStr.get()
            if username and password:
                if result:
                    verify()
                    #print('Giriş başarılı.')
                else:
                    print("Kullanıcı adınız veya şifreniz yanlış.")
            else:
                print("Kullanıcı adı ve şifrenizi doldurunuz.")

        usernameStr = StringVar()
        passwordStr = StringVar()
        self.rememberInt = IntVar()

        frame = Frame(master, relief=RIDGE, bd=3, width=800, height=480)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        mailLabel = ttk.Label(frame, text="Kullanıcı Adı", font="Arial 12 bold")
        mailLabel.place(relx=0.3, rely=0.3)

        mailEntry = ttk.Entry(frame, textvariable=usernameStr, font=("Arial 10"), width=40)
        mailEntry.place(relx=0.3, rely=0.35)


        passwordLabel = ttk.Label(frame, text="Şifre", font="Arial 12 bold")
        passwordLabel.place(relx=0.3, rely=0.48)

        passwordEntry = ttk.Entry(frame, textvariable=passwordStr, font=("Arial 10"), width=40, show="*")
        passwordEntry.place(relx=0.3, rely=0.53)


        rememberBox = ttk.Checkbutton(frame, text="Beni Hatırla", variable=self.rememberInt, onvalue=1, offvalue=0)
        rememberBox.place(relx=0.3, rely=0.58)

        passwordForget = Button(frame, text="Şifre mi unuttum", borderwidth=0, font="Verdana 8 underline",
                                 command=forgotPassword)
        passwordForget.place(relx=0.534, rely=0.58)

        registerButton = ttk.Button(frame, text="Kaydol", command=registerPage)
        registerButton.place(relx=0.3, rely=0.655)

        loginButton = customtkinter.CTkButton(frame, text="Giriş Yap", command=login)
        loginButton.place(relx=0.486, rely=0.65)



if __name__ == "__main__":
    app = mainPage()
    app.mainloop()
