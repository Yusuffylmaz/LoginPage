from tkinter import *
import customtkinter  # pip install customtkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image  # pip install Pillow
import qrcode #pip install qrcode
from VerifySQL import *
import re


customtkinter.set_appearance_mode("Light")  # system (default), light, dark
customtkinter.set_default_color_theme("blue")  # blue (default), dark-blue, green
bg = "#ebebeb"
wColor = "grey"
#StartTimedUpdates() #Kişiye özel olan 'code' değerini 30 saniyede bir günceller. Sadece 7/24 açık olacak olan sayfada bu kodun aktif olması gerekiyor.

def ValidateMail(mail):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pattern, mail):
        return True
    else:
        return False

class mainPage(customtkinter.CTk):
    def __init__(self, master=None):
        super().__init__()
        self.title("Anasayfa")
        self.geometry("1280x720")
        self.iconbitmap('assets/main.ico')
        self.resizable(width=False, height=False)

########################################################################################################################
#                                           R E G I S T E R                                                            #
#                                           R E G I S T E R                                                            #
#                                           R E G I S T E R                                                            #
########################################################################################################################
        def SegmentedRegister():
            def Register():
                name = nameEntry.get()
                lastname = lastnameEntry.get()
                mail = mailEntry.get()
                password = passwordEntry.get()
                passwordRepeat = passwordRepeatEntry.get()
                check = checkStr.get()

                conn = sql.connect(db)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE eposta = ?", (mailEntry.get(),))
                result = cursor.fetchall()

                if name and lastname and mail and password and passwordRepeat:
                    if password == passwordRepeat:
                        if ValidateMail(mail):
                            if result:
                                print("Bu E-Mail zaten kayıtlı.")
                                wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                                fg_color="#b2bfdb")
                                wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                                wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                                wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                                wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                                wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                                wLabel = customtkinter.CTkLabel(wFrame, text="Bu E-Posta adresi zaten kayıtlı.",
                                                                 text_color=wColor)
                                wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                            else:
                                if check == "Accepted":
                                    Generate2FACode(name, lastname, mail, password)
                                    VerifyTwoFA()
                                    print("Kayıt işlemi başarılı.")
                                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                                    fg_color="#b2bfdb")
                                    wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                                    wLabel = customtkinter.CTkLabel(wFrame, text="Kayıt işlemi başarılı.",
                                                                     text_color=wColor)
                                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                                else:
                                    print("Sözleşmeyi kabul ediniz.")
                                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                                    fg_color="#b2bfdb")
                                    wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                                    wLabel = customtkinter.CTkLabel(wFrame, text="Sözleşmeyi kabul ediniz.",
                                                                     text_color=wColor)
                                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                        else:
                            print("Geçerli E-Mail adresi giriniz.")
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame, text="Geçerli E-Mail adresi giriniz.",
                                                            text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                    else:
                        print("Şifreniz eşleşmiyor.")
                        wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                        fg_color="#b2bfdb")
                        wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                        wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                        wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                        wLabel = customtkinter.CTkLabel(wFrame, text="Şifreniz eşleşmiyor.",
                                                         text_color=wColor)
                        wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                else:
                    print("Boş bırakmayın.")
                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                    fg_color="#b2bfdb")
                    wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                    wLabel = customtkinter.CTkLabel(wFrame, text="Boş bırakmayın.",
                                                     text_color=wColor)
                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

            def Contract():
                contract = Toplevel(master)
                contract.title("Okudum kabul ediyorum")
                contract.geometry("400x250")
                contract.mainloop()


            def VerifyTwoFA():
                verifyFrame = Frame(self, width=600, height=400, bg=bg)
                verifyFrame.place(relx=0.7, rely=0.5, anchor=CENTER)

                titleLabel = customtkinter.CTkLabel(master=verifyFrame, text='Authenticator',
                                                    font=('Stencil Std', 25, 'bold'))
                titleLabel.place(relx=0.31, rely=0.155, anchor=CENTER)

                directionLabel1 = customtkinter.CTkLabel(master=verifyFrame,
                                                         text='• XXX Authenticator uygulamasını kurun',
                                                         font=('Poplar Std', 12))
                directionLabel1.place(relx=0.2, rely=0.19)

                directionLabel2 = customtkinter.CTkLabel(master=verifyFrame,
                                                         text='• XXX Authenticator uygulamasından + öğesine dokunun',
                                                         font=('Poplar Std', 12))
                directionLabel2.place(relx=0.2, rely=0.24)

                directionLabel3 = customtkinter.CTkLabel(master=verifyFrame, text="• QR kodunu tara'yı seçin",
                                                         font=('Poplar Std', 12))
                directionLabel3.place(relx=0.2, rely=0.29)

                userCodeQR = 'userCode.png'
                qrcode.make(UserCodeLabel(mailEntry.get())).save(userCodeQR)
                qrImage = customtkinter.CTkImage(light_image=Image.open(userCodeQR),
                                                 size=(128, 128))
                qrLabel = customtkinter.CTkLabel(master=verifyFrame, text="", image=qrImage, bg_color=bg)
                qrLabel.place(relx=0.45, rely=0.53, anchor=CENTER)

                tokenLabel = customtkinter.CTkLabel(master=verifyFrame, text='TOKEN', font=('Poplar Std', 16, 'bold'),
                                                    text_color="#3a7ebf")
                tokenLabel.place(relx=0.2, rely=0.672)
                qrFrame = customtkinter.CTkFrame(master=verifyFrame, height=30, width=320)
                qrFrame.place(relx=0.2, rely=0.73)

                codeLabel = customtkinter.CTkLabel(master=qrFrame, text=UserCodeLabel(mailEntry.get()),
                                                   font=('helvetica', 16, 'bold'))
                codeLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                directionLabel4 = customtkinter.CTkLabel(master=verifyFrame,
                                                         text="Kurulumu bitirdikten sonra uygulamaya "
                                                              "\ngiriş yapabilirsiniz.", text_color="#3a7ebf")
                directionLabel4.place(relx=0.475, rely=0.85, anchor=CENTER)

            frame = customtkinter.CTkFrame(self,  width=1280, height=540, fg_color=bg)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            logoImage = customtkinter.CTkImage(light_image=Image.open('assets/sign.png'),
                                               size=(246, 246))
            logoLabel = customtkinter.CTkLabel(frame, text="", image=logoImage)
            logoLabel.place(relx=0.75, rely=0.48, anchor=CENTER)

            nameImage = customtkinter.CTkImage(light_image=Image.open('assets/user1.png'),
                                               size=(18, 18))
            nameLabel = customtkinter.CTkLabel(frame, text="", image=nameImage)
            nameLabel.place(relx=0.2, rely=0.35, anchor=CENTER)

            nameEntry = customtkinter.CTkEntry(frame, placeholder_text="İsim", width=135, height=23, border_width=0,
                                               corner_radius=3)
            nameEntry.place(relx=0.262, rely=0.35, anchor=CENTER)

            lastnameEntry = customtkinter.CTkEntry(frame, placeholder_text="Soyisim", width=135, height=23,
                                                   border_width=0,
                                                   corner_radius=3)
            lastnameEntry.place(relx=0.38, rely=0.35, anchor=CENTER)

            mailEntry = customtkinter.CTkEntry(frame, placeholder_text="E-Posta Adresiniz", width=284, height=23,
                                               border_width=0, corner_radius=3)
            mailEntry.place(relx=0.32, rely=0.43, anchor=CENTER)

            mailImage = customtkinter.CTkImage(light_image=Image.open('assets/license.png'),
                                               size=(18, 18))
            mailLabel = customtkinter.CTkLabel(frame, text="", image=mailImage)
            mailLabel.place(relx=0.2, rely=0.43, anchor=CENTER)

            passwordImage = customtkinter.CTkImage(light_image=Image.open('assets/password1.png'),
                                                   size=(18, 18))
            passwordLabel = customtkinter.CTkLabel(frame, text="", image=passwordImage)
            passwordLabel.place(relx=0.2, rely=0.51, anchor=CENTER)

            passwordEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifre", width=135, height=23,
                                                   border_width=0,
                                                   corner_radius=3)
            passwordEntry.place(relx=0.262, rely=0.51, anchor=CENTER)

            passwordRepeatEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifreyi Onaylayın", width=135,
                                                         height=23,
                                                         border_width=0, corner_radius=3)
            passwordRepeatEntry.place(relx=0.38, rely=0.51, anchor=CENTER)

            contractEntry = Button(frame, text="Kaydolma şartlarını okudum kabul ediyorum.", borderwidth=0,
                                   font="Verdana 8 underline", command=Contract, bg=bg)
            contractEntry.place(relx=0.325, rely=0.558, anchor=CENTER)

            checkStr = StringVar(value="Not Accepted")
            checkbox = ttk.Checkbutton(frame, variable=checkStr, onvalue="Accepted", offvalue="Not Accepted")
            checkbox.place(relx=0.216, rely=0.56, anchor=CENTER)

            registerButton = customtkinter.CTkButton(frame, text="Kaydol", command=Register)
            registerButton.place(relx=0.377, rely=0.62, anchor=CENTER)

########################################################################################################################
#                                        F O R G O T   P A S S W O R D                                                 #
#                                        F O R G O T   P A S S W O R D                                                 #
#                                        F O R G O T   P A S S W O R D                                                 #
########################################################################################################################
        def SegmentedForgotPassword():
            def LoginStateT():
                mailEntry.configure(state=DISABLED)
                passwordEntry.configure(state=DISABLED)
                passwordRepeatEntry.configure(state=DISABLED)
                button.configure(state=DISABLED)

            def LoginStateF():
                mailEntry.configure(state=NORMAL)
                passwordEntry.configure(state=NORMAL)
                passwordRepeatEntry.configure(state=NORMAL)
                button.configure(state=NORMAL)

            def VerifyTwoFA():
                def VerifyCodeFrame():
                    def VerifyCode():
                        verify= verifyEntry.get()
                        if Verify(mail,verify):
                            conn = sql.connect(db)
                            cursor = conn.cursor()
                            cursor.execute("UPDATE users SET sifre=? WHERE eposta=?", (password, mail))
                            conn.commit()
                            conn.close()

                            wFrame = customtkinter.CTkFrame(verifyFrame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.5, rely=0.7, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame, text="Şifreniz değiştirildi.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                            verifyEntry.configure(state=DISABLED)
                            verifyButton.configure(state=DISABLED)
                        else:
                            LoginStateF()
                            verifyFrame.destroy()
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame,
                                                             text="Doğrulama kodunuz yanlış. Lütfen \ntekrar giriş yapınız.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                    verifyFrame = customtkinter.CTkFrame(self, width=650, height=500, fg_color=bg)
                    verifyFrame.place(relx=0.75, rely=0.5, anchor=CENTER)

                    verifyImage = customtkinter.CTkImage(light_image=Image.open('assets/protection.png'),
                                                         size=(128, 128))
                    verifyLabel = customtkinter.CTkLabel(verifyFrame, text="", image=verifyImage)
                    verifyLabel.place(relx=0.62, rely=0.46, anchor=CENTER)

                    verifyImage = customtkinter.CTkImage(light_image=Image.open('assets/id.png'),
                                                         size=(28, 28))
                    verifyImageLabel = customtkinter.CTkLabel(verifyFrame, text="", image=verifyImage)
                    verifyImageLabel.place(relx=0.4, rely=0.45, anchor=CENTER)

                    verifyEntry = customtkinter.CTkEntry(verifyFrame, placeholder_text="2FA", width=90, height=28,
                                                         border_width=0, corner_radius=3, font=("Verdana", 20), )
                    verifyEntry.place(relx=0.5, rely=0.45, anchor=CENTER)

                    verifyLabel = customtkinter.CTkLabel(verifyFrame, text="XXX Autheticator Kodunu giriniz.",
                                                         font=("Verdana", 10), text_color="#584d5c")
                    verifyLabel.place(relx=0.5, rely=0.61, anchor=CENTER)

                    verifyButton = customtkinter.CTkButton(verifyFrame, text="Onayla", height=25, width=75,
                                                           command=VerifyCode)
                    verifyButton.place(relx=0.5, rely=0.56, anchor=CENTER)


                mail = mailEntry.get()
                password = passwordEntry.get()
                passwordRepeat = passwordRepeatEntry.get()

                conn = sql.connect(db)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE eposta=?", (mail,))
                result = cursor.fetchone()

                if mail and password and passwordRepeat:
                    if password == passwordRepeat:
                        if result:
                            VerifyCodeFrame()
                            LoginStateT()
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame,
                                                             text="Giriş başarılı. Doğrulama kodunu giriniz.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                        else:
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame, text=f" {mail} adında kayıtlı E-Mail \nadresi bulunmamakta.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                    else:
                        wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                        fg_color="#b2bfdb")
                        wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                        wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                        wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                        wLabel = customtkinter.CTkLabel(wFrame,
                                                         text="Şifreniz eşleşmiyor.",
                                                         text_color=wColor)
                        wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                else:
                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                    fg_color="#b2bfdb")
                    wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                    wLabel = customtkinter.CTkLabel(wFrame,
                                                     text=f"Lütfen boş bırakmayın.",
                                                     text_color=wColor)
                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)



            frame = customtkinter.CTkFrame(self,  width=1280, height=540, fg_color=bg)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            logoImage = customtkinter.CTkImage(light_image=Image.open('assets/security.png'),
                                               size=(246, 246))
            logoLabel = customtkinter.CTkLabel(frame, text="", image=logoImage)
            logoLabel.place(relx=0.75, rely=0.48, anchor=CENTER)

            mailEntry = customtkinter.CTkEntry(frame, placeholder_text="E-Posta Adresiniz", width=285, height=24,
                                               border_width=0, corner_radius=3)
            mailEntry.place(relx=0.32, rely=0.43, anchor=CENTER)

            mailImage = customtkinter.CTkImage(light_image=Image.open('assets/license.png'),
                                               size=(18, 18))
            mailIcon = customtkinter.CTkLabel(frame, text="", image=mailImage)
            mailIcon.place(relx=0.2, rely=0.43, anchor=CENTER)

            passwordImage = customtkinter.CTkImage(light_image=Image.open('assets/password1.png'),
                                                   size=(18, 18))
            passwordIcon = customtkinter.CTkLabel(frame, text="", image=passwordImage)
            passwordIcon.place(relx=0.2, rely=0.51, anchor=CENTER)

            passwordEntry = customtkinter.CTkEntry(frame, placeholder_text="Yeni Şifre", width=135, height=23,
                                                   border_width=0,
                                                   corner_radius=3)
            passwordEntry.place(relx=0.262, rely=0.51, anchor=CENTER)

            passwordRepeatEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifreyi Onaylayın", width=135,
                                                         height=23,
                                                         border_width=0, corner_radius=3)
            passwordRepeatEntry.place(relx=0.38, rely=0.51, anchor=CENTER)

            button = customtkinter.CTkButton(frame, text="Şifreyi Değiştir",command=VerifyTwoFA)
            button.place(relx=0.377, rely=0.62, anchor=CENTER)

########################################################################################################################
#                                              L O G I N                                                               #
#                                              L O G I N                                                               #
#                                              L O G I N                                                               #
########################################################################################################################
        def SegmentedLogin():
            def LoginStateT():
                mailEntry.configure(state=DISABLED)
                passwordEntry.configure(state=DISABLED)
                loginButton.configure(state=DISABLED)
                rememberBox.configure(state=DISABLED)
                showButton.configure(state=DISABLED)

            def LoginStateF():
                mailEntry.configure(state=NORMAL)
                passwordEntry.configure(state=NORMAL)
                loginButton.configure(state=NORMAL)
                rememberBox.configure(state=NORMAL)
                showButton.configure(state=NORMAL)


            def VerifyTwoFA():
                def VerifyCode():
                    mail = mailEntry.get()
                    verify = verifyEntry.get()
                    if Verify(mail, verify):

                        print("Giriş başarılı.")
                        verifyEntry.configure(state=DISABLED)
                        verifyButton.configure(state=DISABLED)
                        wFrame = customtkinter.CTkFrame(verifyFrame, width=225, height=40, border_width=1,
                                                        fg_color="#b2bfdb")
                        wFrame.place(relx=0.5, rely=0.7, anchor=CENTER)
                        wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                        wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                        wLabel = customtkinter.CTkLabel(wFrame, text="Giriş başarılı.",
                                                         text_color=wColor)
                        wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                    else:
                        verifyFrame.destroy()
                        LoginStateF()
                        print("Doğrulama kodunuz yanlış.")
                        wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                        fg_color="#b2bfdb")
                        wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                        wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                        wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                        wLabel = customtkinter.CTkLabel(wFrame,
                                                         text="Doğrulama kodunuz yanlış. Lütfen \ntekrar giriş yapınız.",
                                                         text_color=wColor)
                        wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                verifyFrame = customtkinter.CTkFrame(self, width=650, height=500, fg_color=bg)
                verifyFrame.place(relx=0.75, rely=0.5, anchor=CENTER)

                verifyImage = customtkinter.CTkImage(light_image=Image.open('assets/protection.png'),
                                                     size=(128, 128))
                verifyLabel = customtkinter.CTkLabel(verifyFrame, text="", image=verifyImage)
                verifyLabel.place(relx=0.62, rely=0.46, anchor=CENTER)

                verifyImage = customtkinter.CTkImage(light_image=Image.open('assets/id.png'),
                                                     size=(28, 28))
                verifyImageLabel = customtkinter.CTkLabel(verifyFrame, text="", image=verifyImage)
                verifyImageLabel.place(relx=0.4, rely=0.45, anchor=CENTER)

                verifyEntry = customtkinter.CTkEntry(verifyFrame, placeholder_text="2FA", width=90, height=28,
                                                     border_width=0, corner_radius=3, font=("Verdana", 20), )
                verifyEntry.place(relx=0.5, rely=0.45, anchor=CENTER)

                verifyLabel = customtkinter.CTkLabel(verifyFrame, text="XXX Autheticator Kodunu giriniz.",
                                                     font=("Verdana", 10), text_color="#584d5c")
                verifyLabel.place(relx=0.5, rely=0.61, anchor=CENTER)

                verifyButton = customtkinter.CTkButton(verifyFrame, text="Onayla", height=25, width=75,
                                                       command=VerifyCode)
                verifyButton.place(relx=0.5, rely=0.56, anchor=CENTER)

            def Login():
                conn = sql.connect(db)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE eposta = ? and sifre = ?",
                               (usernameStr.get(), passwordStr.get()))
                result = cursor.fetchall()

                username = usernameStr.get()
                password = passwordStr.get()
                if username and password:
                    if result:
                        VerifyTwoFA()
                        LoginStateT()
                        wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                        fg_color="#b2bfdb")
                        wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                        wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                        wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                        wLabel = customtkinter.CTkLabel(wFrame, text="Giriş başarılı. Doğrulama kodunu giriniz.",
                                                         text_color=wColor)
                        wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                        # print('Giriş başarılı.')
                    else:
                        print("Kullanıcı adınız veya şifreniz yanlış.")
                        wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                        fg_color="#b2bfdb")
                        wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                        wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                        wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                        wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                        wLabel = customtkinter.CTkLabel(wFrame, text="Kullanıcı adınız veya şifreniz yanlış.",
                                                         text_color=wColor)
                        wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                else:
                    print("Kullanıcı adı ve şifrenizi doldurunuz.")
                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                    fg_color="#b2bfdb")
                    wFrame.place(relx=0.32, rely=0.75, anchor=CENTER)
                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                    wLabel = customtkinter.CTkLabel(wFrame, text="Kullanıcı adı ve şifrenizi doldurunuz.",
                                                     text_color=wColor)
                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)


            usernameStr = StringVar()
            passwordStr = StringVar()
            self.rememberInt = IntVar()

            frame = customtkinter.CTkFrame(self,  width=1280, height=540, fg_color=bg)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            logoImage = customtkinter.CTkImage(light_image=Image.open('assets/profile.png'),
                                               size=(256, 256))
            logoLabelLogin = customtkinter.CTkLabel(frame, text="", image=logoImage)
            logoLabelLogin.place(relx=0.75, rely=0.48, anchor=CENTER)

            mailLabel = customtkinter.CTkLabel(frame, text="Kullanıcı Adı", font=("Arial", 16,"bold"),bg_color=bg)
            mailLabel.place(relx=0.248, rely=0.313, anchor=CENTER)

            mailEntry = ttk.Entry(frame, textvariable=usernameStr, font=("Arial 10"), width=40)
            mailEntry.place(relx=0.3205, rely=0.35, anchor=CENTER)

            mailImage = customtkinter.CTkImage(light_image=Image.open('assets/user.png'),
                                              size=(18, 18))
            mailLabel = customtkinter.CTkLabel(frame, text="", image=mailImage)
            mailLabel.place(relx=0.2, rely=0.35, anchor=CENTER)

            mailLabel = customtkinter.CTkLabel(frame, text="Şifre", font=("Arial", 16,"bold"),bg_color=bg)
            mailLabel.place(relx=0.223, rely=0.472, anchor=CENTER)

            passwordEntry = ttk.Entry(frame, textvariable=passwordStr, font=("Arial 10"), width=40, show="*")
            passwordEntry.place(relx=0.3205, rely=0.51, anchor=CENTER)

            passwordImage = customtkinter.CTkImage(light_image=Image.open('assets/password.png'),
                                                  size=(18, 18))
            passwordLabel = customtkinter.CTkLabel(frame, text="", image=passwordImage)
            passwordLabel.place(relx=0.2, rely=0.51, anchor=CENTER)

            def Show():
                hideButton = Button(frame, image=hideImage, command=Hide, relief=FLAT
                                    , borderwidth=0, bg=bg)
                hideButton.place(relx=0.44, rely=0.51, anchor=CENTER)
                passwordEntry.config(show='')

            def Hide():
                showButton = Button(frame, image=showImage, command=Show, relief=FLAT
                                    , borderwidth=0, bg=bg)
                showButton.place(relx=0.44, rely=0.51, anchor=CENTER)
                passwordEntry.config(show='*')

            showImage = ImageTk.PhotoImage(Image.open("assets/show.png"),
                                           size=(256, 256))
            self.showLabel = Label(frame, image=showImage)

            hideImage = ImageTk.PhotoImage(Image.open("assets/hide.png"))
            self.hideLabel = Label(frame, image=hideImage)

            showButton = Button(frame, image=showImage, command=Show, relief=FLAT, borderwidth=0, background=bg)
            showButton.place(relx=0.44, rely=0.51, anchor=CENTER)

            rememberBox = ttk.Checkbutton(frame, text="Beni Hatırla", variable=self.rememberInt, onvalue=1, offvalue=0)
            rememberBox.place(relx=0.24, rely=0.56, anchor=CENTER)

            loginButton = customtkinter.CTkButton(frame, text="Giriş Yap",command=Login)
            loginButton.place(relx=0.377, rely=0.62, anchor=CENTER)




########################################################################################################################
#                                              M A I N                                                                 #
#                                              M A I N                                                                 #
#                                              M A I N                                                                 #
########################################################################################################################
        def SegmentedButton(value):
            if value == "Giriş Yap":
                SegmentedLogin()
            elif value == "Kaydol":
                SegmentedRegister()
            elif value == "Şifre Değiştirme":
                SegmentedForgotPassword()


        def MainMenu():
            segmentedButton.set("")
            frame = customtkinter.CTkFrame(self,  width=1280, height=540, fg_color=bg)
            frame.place(relx=0.5, rely=0.5,anchor=CENTER)


            deleteUserImage = customtkinter.CTkImage(light_image=Image.open('assets/delete.png'), size=(32, 32))
            deleteUser = customtkinter.CTkButton(self,text="Hesabımı sil",image=deleteUserImage,command=DeleteUsers
                                                 ,bg_color=bg,fg_color=bg, hover_color="#c0cff0",
                                                 text_color="#4aa8fd",font=('Verdana',11),compound="top")
            deleteUser.place(relx=0.57, rely=0.45,anchor=CENTER)

            def Snake():
                import snake
                import pygame #pip install pygame
                try:
                    snake.gameLoop()
                except pygame.error:
                    print("Oyun kapatıldı!")

            snakeGameImage = customtkinter.CTkImage(light_image=Image.open('assets/snake.png'), size=(32, 32))
            snakeGame = customtkinter.CTkButton(self,text="Yılan Oyunu",image=snakeGameImage,command=Snake
                                                 ,bg_color=bg,fg_color=bg, hover_color="#c0cff0",
                                                 text_color="#4aa8fd",font=('Verdana',11),compound="top")
            snakeGame.place(relx=0.43, rely=0.45,anchor=CENTER)

        def DeleteUsers():
            def LoginStateT():
                mailEntry.configure(state=DISABLED)
                passwordEntry.configure(state=DISABLED)
                deleteUserButton.configure(state=DISABLED)

            def LoginStateF():
                mailEntry.configure(state=NORMAL)
                passwordEntry.configure(state=NORMAL)
                deleteUserButton.configure(state=NORMAL)

            def VerifyTwoFA():
                def VerifyCodeFrame():
                    def VerifyCode():
                        verify= verifyEntry.get()

                        if Verify(mail,verify):
                            DeleteUser(mail,verify)
                            wFrame = customtkinter.CTkFrame(verifyFrame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.5, rely=0.7, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame, text="Hesabınız silindi.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                            verifyEntry.configure(state=DISABLED)
                            verifyButton.configure(state=DISABLED)
                        else:
                            LoginStateF()
                            verifyFrame.destroy()
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.65, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame,
                                                             text="Doğrulama kodunuz yanlış. Lütfen \ntekrar giriş yapınız.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                    verifyFrame = customtkinter.CTkFrame(self, width=650, height=500, fg_color=bg)
                    verifyFrame.place(relx=0.75, rely=0.5, anchor=CENTER)

                    verifyImage = customtkinter.CTkImage(light_image=Image.open('assets/protection.png'),
                                                         size=(128, 128))
                    verifyLabel = customtkinter.CTkLabel(verifyFrame, text="", image=verifyImage)
                    verifyLabel.place(relx=0.62, rely=0.46, anchor=CENTER)

                    verifyImage = customtkinter.CTkImage(light_image=Image.open('assets/id.png'),
                                                         size=(28, 28))
                    verifyImageLabel = customtkinter.CTkLabel(verifyFrame, text="", image=verifyImage)
                    verifyImageLabel.place(relx=0.4, rely=0.45, anchor=CENTER)

                    verifyEntry = customtkinter.CTkEntry(verifyFrame, placeholder_text="2FA", width=90, height=28,
                                                         border_width=0, corner_radius=3, font=("Verdana", 20), )
                    verifyEntry.place(relx=0.5, rely=0.45, anchor=CENTER)

                    verifyLabel = customtkinter.CTkLabel(verifyFrame, text="XXX Autheticator Kodunu giriniz.",
                                                         font=("Verdana", 10), text_color="#584d5c")
                    verifyLabel.place(relx=0.5, rely=0.61, anchor=CENTER)

                    verifyButton = customtkinter.CTkButton(verifyFrame, text="Onayla", height=25, width=75,
                                                           command=VerifyCode)
                    verifyButton.place(relx=0.5, rely=0.56, anchor=CENTER)

                mail = mailEntry.get()
                password = passwordEntry.get()

                conn = sql.connect(db)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE eposta=? AND sifre=?", (mail,password))
                result = cursor.fetchone()

                if mail and password :
                        if result:
                            VerifyCodeFrame()
                            LoginStateT()
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.65, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame,
                                                             text="Giriş başarılı. Doğrulama kodunu giriniz.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
                        else:
                            wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                            fg_color="#b2bfdb")
                            wFrame.place(relx=0.32, rely=0.65, anchor=CENTER)
                            wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                            wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                            wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                            wLabel = customtkinter.CTkLabel(wFrame, text=f"E-Mail adresiniz veya şifreniz yanlış.",
                                                             text_color=wColor)
                            wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

                else:
                    wFrame = customtkinter.CTkFrame(frame, width=225, height=40, border_width=1,
                                                    fg_color="#b2bfdb")
                    wFrame.place(relx=0.32, rely=0.65, anchor=CENTER)
                    wFrameTOP = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameTOP.place(relx=0.5, rely=0.15, anchor=CENTER)
                    wFrameBOT = customtkinter.CTkFrame(wFrame, width=100, height=10, fg_color="#9fafd1")
                    wFrameBOT.place(relx=0.5, rely=0.85, anchor=CENTER)
                    wLabel = customtkinter.CTkLabel(wFrame,
                                                     text=f"Lütfen boş bırakmayın.",
                                                     text_color=wColor)
                    wLabel.place(relx=0.5, rely=0.5, anchor=CENTER)


            frame = customtkinter.CTkFrame(self,  width=1280, height=540, fg_color=bg)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            logoImage = customtkinter.CTkImage(light_image=Image.open('assets/delete.png'),
                                               size=(246, 246))
            logoLabel = customtkinter.CTkLabel(frame, text="", image=logoImage)
            logoLabel.place(relx=0.75, rely=0.48, anchor=CENTER)

            mailEntry = customtkinter.CTkEntry(frame, placeholder_text="E-Posta Adresiniz", width=285, height=24,
                                               border_width=0, corner_radius=3)
            mailEntry.place(relx=0.32, rely=0.43, anchor=CENTER)

            mailImage = customtkinter.CTkImage(light_image=Image.open('assets/license.png'),
                                               size=(18, 18))
            mailIcon = customtkinter.CTkLabel(frame, text="", image=mailImage)
            mailIcon.place(relx=0.2, rely=0.43, anchor=CENTER)

            passwordImage = customtkinter.CTkImage(light_image=Image.open('assets/password1.png'),
                                                   size=(18, 18))
            passwordIcon = customtkinter.CTkLabel(frame, text="", image=passwordImage)
            passwordIcon.place(relx=0.2, rely=0.51, anchor=CENTER)

            passwordEntry = customtkinter.CTkEntry(frame, placeholder_text="Şifre", width=135, height=23,
                                                   border_width=0,corner_radius=3)
            passwordEntry.place(relx=0.262, rely=0.51, anchor=CENTER)

            deleteUserButton = customtkinter.CTkButton(frame, text="Hesabımı Sil",command=VerifyTwoFA)
            deleteUserButton.place(relx=0.377, rely=0.51, anchor=CENTER)



        segmentFrame = customtkinter.CTkFrame(self, width=250, height=50, fg_color=bg)
        segmentFrame.place(relx=0.5, rely=0.1, anchor=CENTER)
        segmentedButton = customtkinter.CTkSegmentedButton(segmentFrame,
                                                           values=["Giriş Yap", "Kaydol", "Şifre Değiştirme"],command=SegmentedButton,
                                                           fg_color="#b2bfdb", selected_hover_color="#9fafd1",
                                                           unselected_color="#9fafd1",unselected_hover_color="#c0cff0"
                                                           )
        segmentedButton.place(relx=0.5, rely=0.5, anchor=CENTER)


        mainMenuImage = customtkinter.CTkImage(light_image=Image.open('assets/home.png'), size=(32, 32))
        mainMenuButton = customtkinter.CTkButton(self, text="Ana Menü", image=mainMenuImage, bg_color=bg,
                                                 fg_color=bg, hover_color="#c0cff0", text_color="#4aa8fd",
                                                 font=('Verdana', 10),command=MainMenu)
        mainMenuButton.place(relx=0.1, rely=0.099, anchor=CENTER)


if __name__ == "__main__":
    app = mainPage()
    CreateDB()
    app.mainloop()
