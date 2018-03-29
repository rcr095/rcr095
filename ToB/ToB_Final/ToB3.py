import tkinter as tk
import sqlite3 as sql
import ctypes as ct
import time
import unittest

        
    
class MemberDB:

    def __init__(self, db):
        self.connect(db)

    def commit(self): #commits changes made to the database
        return self.connection.commit()

    def connClose(self): #terminates database connection
        return self.connection.commit()
        return self.cursor.close()
        return self.connection.close()

    def connect(self, db):
        self.connection = sql.connect(db)
        self.cursor = self.connection.cursor()

    def printdb(self): #prints the full database to the commandline
        sql_command = "SELECT * FROM memberships"
        self.cursor.execute(sql_command)
        print('Memberships:')
        for i in self.cursor.fetchall():
            print(i)
        sql_command = "SELECT * FROM members"
        self.cursor.execute(sql_command)
        print('Memebers:')
        for i in self.cursor.fetchall():
            print(i)
    
    def membershipDisplay(self): #return all memberships type available
        sql_command = """SELECT * FROM memberships"""
        self.cursor.execute(sql_command)
        memberships = self.cursor.fetchall()
        return memberships
    
class Member(MemberDB):

    def memberSearch(self, name, memID): #finds a member with thr provided details
        if name != None and memID != None:
            format_str = """SELECT * FROM members WHERE id={memID} AND name='{name}'"""
            sql_command = format_str.format(memID=str(memID), name=name)
            self.cursor.execute(sql_command)
            members = self.cursor.fetchall()
        elif name != None:
            format_str = """SELECT * FROM members WHERE name='{name}'"""
            sql_command = format_str.format(name=name)
            self.cursor.execute(sql_command)
            members = self.cursor.fetchall()
        elif memID != None:
            format_str = """SELECT * FROM members WHERE id={memID}"""
            sql_command = format_str.format(memID=str(memID))
            self.cursor.execute(sql_command)
            members = self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM members")
            members = self.cursor.fetchall()
        return members

    def renewMembership(self, membership, memID): #updates the members membership information
            join_date = time.strftime("%d/%m/%Y")
            format_str = """UPDATE members SET membership='{membership}', join_date='{join_date}' WHERE id={memID};"""
            sql_command = format_str.format(membership=membership, join_date=join_date, memID=memID)
            self.cursor.execute(sql_command)
            self.connection.commit()
            return
    
class OperatorController(Member):

    def addMember(self, name, phone, email, birth_date, membership): #add a new member to the database
        if phone != None and ((str(phone).isdigit()==False) or len(str(phone)) > 14 or len(str(phone)) < 5):
            return 1,0
        if email != None and (('@' not in email) or ('.' not in email)):
            return 2,0
        join_date = time.strftime("%d/%m/%Y")
        memid = self.memberTot()
        format_str = """INSERT INTO members(id, name, phone, email, birth_date, join_date, membership)
                                VALUES ("{memid}", "{name}", "{phone}", "{email}", "{birth_date}", "{join_date}", "{membership}");"""

        sql_command = format_str.format(memid=memid, name=name, phone=phone, email=email, birth_date=birth_date, join_date=join_date, membership=membership)
        self.cursor.execute(sql_command)
        self.connection.commit()
        return 0, memid
    
    def memberTot(self): #finds the last used id and returns the next available id
        self.cursor.execute("SELECT * FROM members")
        members = self.cursor.fetchall()
        if len(members)>0:
            memberID = members[-1][0] + 1
        else:
            memberID = 0
        return memberID
    
    def delMember(self, idReq, nameReq): #deletes a member from the database
        format_str = "DELETE FROM members WHERE id={idReq} AND name='{nameReq}'"
        sql_command=format_str.format(idReq=idReq, nameReq=nameReq)
        self.cursor.execute(sql_command)
        self.connection.commit()
        return 

    def updMember(self, name, phone, email, birth_date): #updates information
            memID = self.memberID
            updated = []
            #each if statement will verify if there's new data to be implemented/updated
            if name != None:
                format_str = """UPDATE members SET name='{name}' WHERE id={memID};"""
                sql_command = format_str.format(name=name, memID=memID)
                self.cursor.execute(sql_command)
                self.connection.commit()
                updated.append(name)
            if email != None:
                format_str = """UPDATE members SET email='{email}' WHERE id={memID};"""
                sql_command = format_str.format(email=email, memID=memID)
                self.cursor.execute(sql_command)
                self.connection.commit()
                updated.append(email)
            if phone != None:
                format_str = """UPDATE members SET phone='{phone}' WHERE id={memID};"""
                sql_command = format_str.format(phone=phone, memID=memID)
                self.cursor.execute(sql_command)
                self.connection.commit()
                updated.append(phone)
            if birth_date != None:
                format_str = """UPDATE members SET birth_date='{birth_date}' WHERE id={memID};"""
                sql_command = format_str.format(birth_date=birth_date, memID=memID)
                self.cursor.execute(sql_command)
                self.connection.commit()
                updated.append(birth_date)
            return updated
        
class OperatorUI(OperatorController):

    def __init__(self):
        self.buildFrame()
        self.connect('tob.db')

    def buildFrame(self):#creates main frame
        self.w, self.h = 1000, 720
        self.win = tk.Tk()
        self.state = 'window'
        self.win.resizable(False, False)
        self.win.geometry('%dx%d+0+0' % (self.w, self.h))
        self.win.title('Tour of Britain')
        font = 'Times 14 bold'
        h = 100
        w = 150
        self.frame = tk.Canvas(self.win, width = self.w, height = self.h, bg = 'white')
        self.frame.pack()
        self.frame.create_text((50, 50), text = 'Membership Management', font = 'Times 20 bold', anchor = tk.NW)
        self.btSearch = tk.Button(self.frame, font = font, text = 'Search', command = self.searchTab, bg='royalblue')
        self.btSearch.place(x = 50, y = 150, width = w, height = h)
        self.btAdd = tk.Button(self.frame, font = font, text = 'Add\nMember', command = self.addMemberTab, bg='deepskyblue')
        self.btAdd.place(x = 50+w, y = 150, width = w, height = h)
        self.btDel = tk.Button(self.frame, font = font, text = 'Delete\nMember', command = self.deleteTab, bg='royalblue')
        self.btDel.place(x = 50+(w*2), y = 150, width = w, height = h)
        self.btUpdMember = tk.Button(self.frame, font = font, text = 'Update\nMember', command = self.updateTab, bg='deepskyblue')
        self.btUpdMember.place(x = 50+(w*3), y = 150, width = w, height = h)
        self.btClose = tk.Button(self.frame, font = font, text = 'Exit', command = self.close, bg='sienna')
        self.btClose.place(x = 50+(w*4), y = 150, width = w, height = h)
        self.current = tk.Canvas(self.frame, width = self.w-100, height = self.h-350, bg = 'white', highlightbackground="black")
        self.current.place(x = 50, y = 300)
        self.searchTab()
        return
    
    def searchTab(self):#creates search tab
        self.currentFrame()
        font = 'Times 12 bold'
        self.current.create_text((50, 50), text = 'Search', font = 'Times 20 bold', anchor = tk.NW)
        self.current.create_text((50, 100), text = 'Find current members information or available memberships.', font = 'Times 16 bold', anchor = tk.NW)    
        self.btMemberS = tk.Button(self.current, font = font, text = 'Member Search', command = self.memberSearchTab, bg='royalblue')
        self.btMemberS.place(x = 50, y = 150, width = 200, height = 100)
        self.btMembershipS = tk.Button(self.current, font = font, text = 'Membership Search', command = self.membershipSearch, bg='deepskyblue')
        self.btMembershipS.place(x = 250, y = 150, width = 200, height = 100)
        return

    def memberSearchTab(self):#opens member search tab
        self.currentFrame()
        font = 'Times 12 bold'
        self.current.create_text((50, 50), text = 'Member Search', font = 'Times 20 bold', anchor = tk.NW)
        self.current.create_text((50, 100), text = 'Find current members information from their name or ID.', font = 'Times 16 bold', anchor = tk.NW)   
        self.current.create_text((50, 130), text = 'Member ID', font = font, anchor = tk.NW)
        self.entryID = tk.Entry(self.current)
        self.current.create_window(155, 130, height=25, width =200, window=self.entryID, anchor=tk.NW)
        self.current.create_text((50, 160), text = 'Name', font = font, anchor = tk.NW)
        self.entryName = tk.Entry(self.current)
        self.current.create_window(155, 160, height=25, width =200, window=self.entryName, anchor=tk.NW)    
        self.btMemberS = tk.Button(self.current, font = font, text = 'Search', command = self.memberSearchBt, bg='royalblue')
        self.btMemberS.place(x = 50, y = 190, width = 305, height = 30)
        return

    def memberSearchBt(self):#opens the member search tab
        if self.entryName.get() and self.entryID.get():
            memID = self.entryID.get()
            name = self.entryName.get()
            members = self.memberSearch(name, memID)
        elif self.entryName.get():
            name = self.entryName.get()
            members = self.memberSearch(name, None)
        elif self.entryID.get():
            memID = self.entryID.get()
            members = self.memberSearch(None, memID)
        if len(members) > 0:
            textOut = ''
            for i in members: 
                textOut=textOut+'\nID: '+str(i[0])+' | Name: '+i[1]+' | Phone: '+str(i[2])+' | Email: '+i[3]+' | Birth Date: '+i[4]+' | Mem. Since: '+i[5]+' | Membership: '+i[6]
            self.currentFrame()
            font = 'Times 12'
            self.current.create_text((50, 50), text = 'Search Results:', font = 'Times 20 bold', anchor = tk.NW)
            self.current.create_text((30, 80), text = textOut, font = font, anchor = tk.NW)
        else:
            self.memberSearchTab()
            self.current.create_text((10, 10), text = 'No member found.', font = 'Times 16 ', anchor = tk.NW)   
        return

    def membershipSearch(self):#opens and displayed memberships available
        memberships = self.membershipDisplay()
        textOut = ''
        for i in memberships:
            textOut = textOut+'\n'+i[0]+' | Price: £'+str(i[1])+' | Duration: '+str(i[2])+' days.'
        self.currentFrame()
        font = 'Times 12'
        self.current.create_text((50, 50), text = 'Memberships:', font = 'Times 20 bold', anchor = tk.NW)
        self.current.create_text((50, 80), text = textOut, font = 'Times 12', anchor = tk.NW)
        return

    def addMemberTab(self):#creates new menber tab
        self.currentFrame()
        font = 'Times 14 bold'
        self.current.create_text((50, 50), text = 'Add New Member', font = 'Times 20 bold', anchor = tk.NW)
        self.current.create_text((50, 100), text = 'Name', font = font, anchor = tk.NW)
        self.entryName = tk.Entry(self.current)
        self.current.create_window(155, 100, height=25, width =200, window=self.entryName, anchor=tk.NW)
        self.current.create_text((50, 130), text = 'Phone', font = font, anchor = tk.NW)
        self.entryPhone = tk.Entry(self.current)
        self.current.create_window(155, 130, height=25, width =200, window=self.entryPhone, anchor=tk.NW)
        self.current.create_text((50, 160), text = 'Email', font = font, anchor = tk.NW)
        self.entryMail = tk.Entry(self.current)
        self.current.create_window(155, 160, height=25, width =200, window=self.entryMail, anchor=tk.NW)
        self.current.create_text((50, 190), text = 'Birth Date', font = font, anchor = tk.NW)
        self.entryDate = tk.Entry(self.current)
        self.current.create_window(155, 190, height=25, width =200, window=self.entryDate, anchor=tk.NW)
        self.current.create_text((50, 220), text = 'Membership', font = font, anchor = tk.NW)
        self.entryMembership = tk.Entry(self.current)
        self.current.create_window(155, 220, height=25, width =200, window=self.entryMembership, anchor=tk.NW)
        self.confirm = tk.Button(self.current, font = font, text = 'Confirm', command = self.addMemberBt, bg='white')
        self.confirm.place(x = 50, y = 270, width = 305, height = 30)
        memberships = self.membershipDisplay()
        textOut = 'Memberships available:'
        for i in memberships:
            textOut = textOut+'\n'+i[0]+' | Price: £'+str(i[1])+' | Duration: '+str(i[2])+' days.'
        self.current.create_text((405, 50), text = textOut, font = 'Times 12', anchor = tk.NW)
        self.current.create_text((50, 320), text = 'Member name, birth date and either phone or email required.', font = 'Times 16', anchor = tk.NW)
        return

    def addMemberBt(self):#check input validity and runs funtion to add new member
        memberships =self.membershipDisplay()
        membershipNames = []
        for i in memberships:
            membershipNames.append(i[0])     
        if self.entryMembership.get() in membershipNames:
            if self.entryName.get() and self.entryDate.get() and (self.entryPhone.get() or self.entryMail.get()):
                name = str(self.entryName.get())
                phone = self.entryPhone.get()
                email = str(self.entryMail.get())
                birth_date = self.entryDate.get()
                membership = self.entryMembership.get()
                added, memid = self.addMember(name, phone, email, birth_date, membership)
                if added == 1:
                    self.addMemberTab()
                    self.current.create_text((10, 10), text = 'Invalid phone number.', font = 'Times 16 ', anchor = tk.NW)
                    return
                elif added == 2:
                    self.addMemberTab()
                    self.current.create_text((10, 10), text = 'Invalid email.', font = 'Times 16 ', anchor = tk.NW)
                    return
                elif added == 0:
                    self.added(memid)  
            else:
                self.current.create_text((10, 10), text = 'Information Missing!', font = 'Times 16 ', anchor = tk.NW)
        else:
            self.current.create_text((10, 10), text = 'Membership does not exist!', font = 'Times 16 ', anchor = tk.NW)

    def added(self, memid):#shows information of the added member including the ID which is shown here for the first time
        self.currentFrame()
        self.current.create_text((50, 50), text = 'Added New Member', font = 'Times 20 bold', anchor = tk.NW)
        member = self.memberSearch(None, memid)[0]
        zeroL = '0'*(6-len(str(member[0])))
        idReq = zeroL+str(member[0])
        nameReq, emailReq, phoneReq, birthDate, joinDate, membership = member[1], member[3], str(member[2]), str(member[4]), member[5], member[6]
        textReq = ('Member ID: '+idReq+'\nName: '+nameReq+'\nEmail: '+emailReq+'\nPhone: '+
                    phoneReq+'\nBirth Date: '+birthDate+'\nMember Since: '+joinDate+'\nMembership Type: '+membership)
        self.current.create_text((50,100), text = textReq, anchor = tk.NW)
        self.btCancel = tk.Button(self.current, text = 'Back', command=self.addBack, bg='white')
        self.btCancel.place(x=50, y=270, width=200, height=50)

    def addBack(self):#goes back to the main new member tab
        self.addMemberTab()
        
    def deleteTab(self):  #creates delete tab      
        self.currentFrame()
        font = 'Times 14 bold'
        self.current.create_text((50, 50), text = 'Delete Existing Member', font = 'Times 20 bold', anchor = tk.NW)
        self.current.create_text((50, 100), text = 'M. ID', font = font, anchor = tk.NW)
        self.entryID = tk.Entry(self.current)
        self.current.create_window(110, 100, height=25, width =200, window=self.entryID, anchor=tk.NW)
        self.current.create_text((50, 130), text = 'Name', font = font, anchor = tk.NW)
        self.entryName = tk.Entry(self.current)
        self.current.create_window(110, 130, height=25, width =200, window=self.entryName, anchor=tk.NW)
        self.confirm = tk.Button(self.current, font = font, text = 'Confirm', command = self.delBt, bg='white')
        self.confirm.place(x = 50, y = 180, width = 260, height = 30)
        self.current.create_text((50, 230), text = 'Member name and ID must match.', font = 'Times 16', anchor = tk.NW)
        return

    def delBt(self):#check the validity of the input and confirm deletetion or adk for the verification of details.
        if self.entryID.get() and self.entryName.get():
            idReq = int(self.entryID.get())
            nameReq = self.entryName.get()
            existence = False
            members = self.memberSearch(None, None)
            for i in members:
                if idReq == i[0] and nameReq == i[1]:
                    existence = True        
            if existence == True:
                self.delMember(idReq, nameReq)
                self.currentFrame()
                self.current.create_text((50, 50), text = 'Deleted Member', font = 'Times 20 bold', anchor = tk.NW)
                textReq='Member ID: '+str(idReq)+'\nName: '+nameReq
                self.current.create_text((50,100), text = textReq, anchor = tk.NW)
                self.btDel = tk.Button(self.current, text = 'Back', command=self.deleteTab, bg='white')
                self.btDel.place(x=50, y=150, width=200, height=50)
            else:
                self.deleteTab()
                textReq = 'Member Does not exist. Verify Details.'
                self.current.create_text((10,10), text = textReq, font = 'Times 16 ', anchor = tk.NW)

    def updateTab(self):#creates update tabe
        self.currentFrame()
        font = 'Times 14 bold'
        self.current.create_text((50, 50), text = 'Update Member Information', font = 'Times 20 bold', anchor = tk.NW)
        self.current.create_text((50, 100), text = 'M. ID', font = font, anchor = tk.NW)
        self.entryID = tk.Entry(self.current)
        self.current.create_window(110, 100, height=25, width =200, window=self.entryID, anchor=tk.NW)
        self.current.create_text((50, 130), text = 'Name', font = font, anchor = tk.NW)
        self.entryName = tk.Entry(self.current)
        self.current.create_window(110, 130, height=25, width =200, window=self.entryName, anchor=tk.NW)
        self.confirm = tk.Button(self.current, font = font, text = 'Confirm', command = self.updConf, bg='white')
        self.confirm.place(x = 50, y = 180, width = 260, height = 30)
        self.current.create_text((50, 230), text = 'Member name and ID must match.', font = 'Times 16', anchor = tk.NW)
        return

    def updConf(self):#shows information and created the boxes for the user input of the update tab
        if self.entryID.get() and self.entryName.get():
            idReq = int(self.entryID.get())
            nameReq = self.entryName.get()
            existence = False
            members = self.memberSearch(None, None)
            for i in members:
                if idReq == i[0] and nameReq == i[1]:
                    existence = True
                    member = i       
            if existence == True:
                font = 'Times 14 bold'
                self.currentFrame()
                self.current.create_text((50, 50), text = 'Member Information', font = 'Times 20 bold', anchor = tk.NW)
                self.current.create_text((160, 100), text = 'Current Information', font = font, anchor = tk.NW)
                self.current.create_text((360, 100), text = 'New Information', font = font, anchor = tk.NW)
                self.current.create_text((50, 130), text = 'Member ID', font = font, anchor = tk.NW)
                self.current.create_text((160, 130), text = str(member[0]), font = font, anchor = tk.NW)
                self.memberID = member[0]
                self.current.create_text((50, 160), text = 'Name', font = font, anchor = tk.NW)
                self.current.create_text((160, 160), text = str(member[1]), font = font, anchor = tk.NW)
                self.entryName = tk.Entry(self.current)
                self.current.create_window(360, 160, height=25, width =200, window=self.entryName, anchor=tk.NW)
                self.current.create_text((50, 190), text = 'Phone', font = font, anchor = tk.NW)
                self.current.create_text((160, 190), text = str(member[2]), font = font, anchor = tk.NW)
                self.entryPhone = tk.Entry(self.current)
                self.current.create_window(360, 190, height=25, width =200, window=self.entryPhone, anchor=tk.NW)
                self.current.create_text((50, 220), text = 'Email', font = font, anchor = tk.NW)
                self.current.create_text((160, 220), text = str(member[3]), font = font, anchor = tk.NW)
                self.entryMail = tk.Entry(self.current)
                self.current.create_window(360, 220, height=25, width =200, window=self.entryMail, anchor=tk.NW)
                self.current.create_text((50, 250), text = 'Birth Date', font = font, anchor = tk.NW)
                self.current.create_text((160, 250), text = str(member[4]), font = font, anchor = tk.NW)
                self.entryDate = tk.Entry(self.current)
                self.current.create_window(360, 250, height=25, width =200, window=self.entryDate, anchor=tk.NW)
                self.current.create_text((50, 280), text = 'Mem. Since', font = font, anchor = tk.NW)
                self.current.create_text((160, 280), text = str(member[5]), font = font, anchor = tk.NW)
                self.current.create_text((50, 310), text = 'Membership', font = font, anchor = tk.NW)
                self.current.create_text((160, 310), text = str(member[6]), font = font, anchor = tk.NW)
                self.entryMembership = tk.Entry(self.current)
                self.current.create_window(360, 310, height=25, width =200, window=self.entryMembership, anchor=tk.NW)
                self.btDel = tk.Button(self.current, text = 'Update Information', command=self.updMemberBt, bg='white')
                self.btDel.place(x=610, y=100, width=200, height=50)
                self.btDel = tk.Button(self.current, text = 'Renew Membership', command=self.renewMembershipBt, bg='white')
                self.btDel.place(x=610, y=160, width=200, height=50)
                self.btDel = tk.Button(self.current, text = 'Cancel', command=self.updateTab, bg='white')
                self.btDel.place(x=610, y=220, width=200, height=50)
                self.current.create_text((50, 340), text = 'Information update and membership renewal must be done separately.', font = 'Times 12', anchor = tk.NW)
            else:
                self.updateTab()
                textReq = 'Member Does not exist. Verify Details.'
                self.current.create_text((10,10), text = textReq, font = 'Times 16 ', anchor = tk.NW)

    def updMemberBt(self):# verifies the validity of the input and shows error or run the update member function
        if self.entryMail.get()  or self.entryPhone.get()  or self.entryName.get() or self.entryDate.get():
            memID = self.memberID
            name = None
            email = None
            phone = None
            birth_date = None
            if self.entryName.get():
                name = self.entryName.get()
            if self.entryMail.get():
                email = self.entryMail.get()
                if self.entryMail.get() and (('@' not in email) or ('.' not in email)):
                    self.updateTab()
                    self.current.create_text((10, 10), text = 'Invalid email.', font = 'Times 16 ', anchor = tk.NW)
                    return
            if self.entryPhone.get():
                phone = self.entryPhone.get()
                if (phone.isdigit()==False) or len(str(phone)) > 14 or len(str(phone)) < 5:
                    self.updateTab()
                    self.current.create_text((10, 10), text = 'Invalid phone number.', font = 'Times 16 ', anchor = tk.NW)
                    return
            if self.entryDate.get():
                birth_date = self.entryDate.get()
            self.updMember(name, phone, email, birth_date)             
            self.updateTab()
            textReq = 'Information Updated.'
            self.current.create_text((10,10), text = textReq, font = 'Times 16 ', anchor = tk.NW)
        else:
            self.updateTab()
            textReq = 'Nothing to Update.'
            self.current.create_text((10,10), text = textReq, font = 'Times 16 ', anchor = tk.NW)

    def renewMembershipBt(self):#confirms the renewal of the membership
        if self.entryMembership.get():
            membership = self.entryMembership.get()
            memID = self.memberID
            self.renewMembership(membership, memID)
            self.updateTab()
            textReq = 'Membership Renewed.'
            self.current.create_text((10,10), text = textReq, font = 'Times 16 ', anchor = tk.NW)
    
    def currentFrame(self):#creates a new frame inside the main frame where the current focus is at
        self.current.destroy()
        self.current = tk.Canvas(self.frame, width = self.w-100, height = self.h-350, bg = 'paleturquoise', highlightbackground="black")
        self.current.place(x = 50, y = 300)

    def close(self):#closes the window
        self.connClose()
        return self.win.destroy()

class TestToBGui(unittest.TestCase):

    def test_update(self): #uses a for loop to change the name of a member given an ID
        tob = OperatorController('tob.db')
        names = ['Ricardo', 'Jon', 'Alex']
        tob.memberID = 0
        for name in names:
            updated = tob.updMember(name, None, None, None)
            self.assertEqual(tob.memberSearch(None, 0)[0][1], updated[0])
        tob.connClose()

    def test_new(self): #uses a for loop to add 3 new members
        tob = OperatorController('tob.db')
        members = [['Ricardo', 91310283, 'ricardo@gmail.com', '11/10/1995', 'Silver'], ['Jon',
                None, 'jon@gmail.com', '02/05/1980', 'Bronze'], ['Alex', 12318181, None, '11/10/1985', 'Gold']]
        tob.memberID = 0
        for member in members:
            updated = tob.addMember(member[0], member[1], member[2], member[3], member[4])
            self.assertEqual(tob.memberSearch(None, updated[1])[0][1], member[0])
            self.assertEqual(str(tob.memberSearch(None, updated[1])[0][2]), str(member[1]))
            self.assertEqual(tob.memberSearch(None, updated[1])[0][3], str(member[2]))
            self.assertEqual(tob.memberSearch(None, updated[1])[0][4], member[3])
            self.assertEqual(tob.memberSearch(None, updated[1])[0][6], member[4])
        tob.connClose()
        
    def test_del(self): #uses a for loop to delete the previously added members
        tob = OperatorController('tob.db')
        members = [[80, 'Ricardo'], [81, 'Jon'], [82, 'Alex']]
        tob.memberID = 0
        for member in members:
            self.assertEqual(tob.memberSearch(member[1], member[0])[0][1], member[1])
            updated = tob.delMember(member[0], member[1])
            self.assertEqual(tob.memberSearch(member[1], member[0]), [])
        tob.connClose()
        

if __name__ == '__main__':
    tob = OperatorUI()

