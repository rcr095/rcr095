import tkinter as tk
import sqlite3 as sql

class GUI():

    def __init__(self):
        self.startWindow()
        self.startMain()
        self.connection = sql.connect("tob.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA table_info(members)")
        self.cursor.execute("SELECT * FROM members")
        self.memberTot()

    def memberTot(self):
        self.cursor.execute("SELECT * FROM members")
        members = self.cursor.fetchall()
        return len(members)
        
    def startMain(self):
        self.buildFrame()
        self.packBtt()
        self.header('Membership\nManagement')
        self.backgrd()
        self.btMHome = tk.Button(self.frame, text = 'Close', command=self.close)
        self.btMHome.place(x=550, y=540, width=200, height=60)

    def close(self):
        return
    
    def startWindow(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title('Tour of Britain')

    def buildFrame(self):
        self.frame = tk.Canvas(self.window, width = 800, height = 650, bg = 'lightblue')
        self.frame.pack()

    def packBtt(self):
        self.bt1 = tk.Button(self.frame, text = 'Add New Member', command=self.newM)
        self.bt1.place(x=50, y=200, width=200, height=100)
        self.bt2 = tk.Button(self.frame, text = 'Remove Member', command=self.remM)
        self.bt2.place(x=50, y=350, width=200, height=100)
        self.bt3 = tk.Button(self.frame, text = 'Manage Membership Fees', command=self.manMF)
        self.bt3.place(x=50, y=500, width=200, height=100)

    def header(self, text):
        self.frame.create_text(150,95, fill='black', font='Times 20 bold', text=text)

    def restart(self, header):
        self.frame.destroy()
        self.buildFrame()
        self.backgrd()
        self.header(header)

    def backgrd(self):
        self.frame.create_text(525,275, fill='black', font='Times 60 italic bold', text='  Tour\n    of\nBritain')

    def home(self):
        self.frame.destroy()
        self.startMain()
        

    def homeBt(self):
        self.btMHome = tk.Button(self.frame, text = 'Home', command=self.home)
        self.btMHome.place(x=550, y=540, width=200, height=60)
        
    def newM(self):
        self.restart('Add New\nMember')
        self.entryName = tk.Entry(self.frame)
        self.frame.create_text(85,220, fill='black', font='Times 16 bold', text='Name:  ')
        self.frame.create_window(50, 250, height=30, width =200, window=self.entryName, anchor=tk.W)
        self.entryMail = tk.Entry(self.frame)
        self.frame.create_text(85,300, fill='black', font='Times 16 bold', text='Email:  ')
        self.frame.create_window(50, 330, height=30, width =200, window=self.entryMail, anchor=tk.W)
        self.entryPhone = tk.Entry(self.frame)
        self.frame.create_text(85,380, fill='black', font='Times 16 bold', text='Phone: ')
        self.frame.create_window(50, 410, height=30, width =200, window=self.entryPhone, anchor=tk.W)
        self.entryDate = tk.Entry(self.frame)
        self.frame.create_text(85,460, fill='black', font='Times 16 bold', text='           Date of Birth:')
        self.frame.create_window(50, 490, height=30, width =200, window=self.entryDate, anchor=tk.W)
        self.bt = tk.Button(self.frame, text = 'Add Member', command=self.add)
        self.bt.place(x=50, y=540, width=200, height=60)
        self.homeBt()
        
    def add(self):
        if (self.entryName.get() and self.entryDate.get() and (self.entryPhone.get() or self.entryMail.get())): 
            format_str = """INSERT INTO members(id, name, phone, email, birth_date)
                        VALUES ("{memid}", "{name}", "{phone}", "{email}", "{birth_date}");"""
            memid = self.memberTot()+1
            name = self.entryName.get()
            phone = self.entryPhone.get()
            email = self.entryMail.get()
            birth_date = self.entryDate.get()
            sql_command = format_str.format(memid=memid, name=name, phone=phone, email=email, birth_date=birth_date)
            self.cursor.execute(sql_command)
            self.connection.commit()
            self.restart(' Added\nMember')
            format_str = "SELECT * FROM members WHERE id={memid}"
            sql_command = format_str.format(memid=memid)
            self.cursor.execute(sql_command)
            member = self.cursor.fetchall()[0]
            zeroL = '0'*(6-len(str(member[0])))
            idReq = zeroL+str(member[0])
            nameReq = str(member[1])
            emailReq = str(member[2])
            phoneReq = str(member[3])
            birth_date = str(member[4])
            textA='Member ID: '+idReq+'\nName: '+nameReq+'\nEmail: '+emailReq+'\nPhone: '+phoneReq+'\nBirth Date: '+birth_date
            self.frame.create_text(150,200, fill='black', font='Times 16 bold', text=textA)
            self.homeBt()

    def remM(self):
        self.restart('Remove\nMember')
        self.entryName = tk.Entry(self.frame)
        self.frame.create_text(85,220, fill='black', font='Times 16 bold', text='Name:  ')
        self.frame.create_window(50, 250, height=30, width =200, window=self.entryName, anchor=tk.W)
        self.entryNumber = tk.Entry(self.frame)
        self.frame.create_text(103,300, fill='black', font='Times 16 bold', text='Member ID:')
        self.frame.create_window(50, 330, height=30, width =200, window=self.entryNumber, anchor=tk.W)
        self.bt = tk.Button(self.frame, text = 'Remove Member', command=self.rem)
        self.bt.place(x=50, y=370, width=200, height=60)
        self.homeBt()

    def rem(self):
        idReq = self.entryNumber.get()
        ename = self.entryName.get()
        if self.entryNumber.get():
            try:
                self.restart('Member\nRemoved')
                nameReq = 'Ricardo'
                format_str = "DELETE FROM members WHERE id={mId} AND name={ename}"
                sql_command=format_str.format(mId=idReq, ename=ename)
                self.cursor.execute(sql_command)
                textA='Deleted:\nName:'+nameReq+'\nMember ID: '+idReq
                self.frame.create_text(150,200, fill='black', font='Times 16 bold', text=textA)
                self.connection.commit()
            except :
                self.restart('Member\nNot Removed')
                textA='Member Does Not Exist\n       Verify Details'
                self.frame.create_text(150,200, fill='black', font='Times 16 bold', text=textA)
                self.bt = tk.Button(self.frame, text = 'Try Again', command=self.remM)
                self.bt.place(x=50, y=250, width=200, height=60)
            self.homeBt()

    def manMF(self):
        self.restart('Manage Fees')
        sql_command = "SELECT * FROM fees WHERE fee='non_member'"
        self.cursor.execute(sql_command)
        nonMem = str(self.cursor.fetchall()[0][2])
        sql_command = "SELECT * FROM fees WHERE fee='membership'"
        self.cursor.execute(sql_command)
        memFee = str(self.cursor.fetchall()[0][2])
        textA = 'Current Fees:\n\nMembership Fee: £'+memFee+'\nNon-Member Fee: £'+nonMem
        self.frame.create_text(150,200, fill='black', font='Times 16 bold', text=textA)
        self.frame.create_text(128,300, fill='black', font='Times 22 bold', text='Update Fees:')
        self.entryMF = tk.Entry(self.frame)
        self.frame.create_text(150,350, fill='black', font='Times 16 bold', text='New Membership Fee:')
        self.frame.create_window(50, 380, height=30, width =200, window=self.entryMF, anchor=tk.W)
        self.entryNM = tk.Entry(self.frame)
        self.frame.create_text(155,410, fill='black', font='Times 16 bold', text='New Non-Member Fee:')
        self.frame.create_window(50, 440, height=30, width =200, window=self.entryNM, anchor=tk.W)
        self.bt = tk.Button(self.frame, text = 'Update', command=self.updt)
        self.bt.place(x=50, y=470, width=200, height=60)
        self.homeBt()

    def updt(self):
        if self.entryMF.get():
            memFee = int(self.entryMF.get())
            format_str = "UPDATE fees SET value={value} WHERE fee='membership'"
            sql_command=format_str.format(value=memFee)
            self.cursor.execute(sql_command)
        if self.entryNM.get():
            nonMem = int(self.entryNM.get())
            format_str = "UPDATE fees SET value={value} WHERE fee='non_member'"
            sql_command=format_str.format(value=nonMem)
            self.cursor.execute(sql_command) 
        self.connection.commit()
        self.manMF()

    def printdb(self):
        sql_command = "SELECT * FROM fees"
        self.cursor.execute(sql_command)
        print('Fees:')
        for i in self.cursor.fetchall():
            print(i)
        sql_command = "SELECT * FROM members"
        self.cursor.execute(sql_command)
        print('Memebers:')
        for i in self.cursor.fetchall():
            print(i)
        
 
    
if __name__ == '__main__':
    tob = GUI()  
