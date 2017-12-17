# Import's tkinter library to create GUI 
from tkinter import *
from tkinter import font 
# Import random library
import random
#Set up a GUI called window
window = Tk()     
# Create's the wharehouse window
canvas = Canvas(window, width=1350, height=720, bg='white')
#Creates controls frame
canvasframe = Canvas(window,width=1136, height=200, bg='red')
####################################################################################
### Control of the sreen state(fullsreen/windowed) #################################
# Current screen state
now=True
# Launches initial screen state
window.overrideredirect(now)
# Screen state toggle function
def Escape(event):
    global now # Imports 'now' value
    if now==False:
        now=True # Changes sreen state info
    else:
        now=False # Changes sreen state info
    window.overrideredirect(now) # Lauches new screen state
# Defines window geometry
canvas.grid(columnspan=200,rowspan=12,padx=285,pady=10)
# Defines controls frames geometry
canvasframe.grid(padx=385)
# Binds Escape key to Escapes function
canvas.bind('<Escape>',Escape)
# Retrieves information from keyboard
canvas.focus_set()
####################################################################################
####################################################################################
### Time Clock #####################################################################
hour = 0 # Hours since program launch
second = 0 # Seconds since program launch
minut = 0 # Minutes since program launch
font0 = font.Font(size=25, weight='bold') # Creates font0
label0 = Label(window, fg="green") # Creates label0
# label0 configuration
label0.config(text='Time Working: '+ str(second)+' seconds',font=font0)
label0.grid(row=9,rowspan=3) # label0 placement on window
# Time function
def time():
    def timecount():
        global second # Imports second value into the function
        global minut # Imports minut value into the function
        global hour # Imports hour value into the function
        second += 1  #Increases second value by 1
        if second >= 60:
            second = 0
            minut += 1 #Increases minut value by 1
            label0.config(text='Time Working: '+ str(minut)+'m '+str(second)
                          +'s',font=font0)
        else:
            if minut>0:
                label0.config(text='Time Working: '+ str(minut)+'m '+str(second)
                              +'s',font=font0)
            else:
                label0.config(text='Time Working: '+ str(second)+'s',font=font0)
        if minut>=60:
            minut=0
            hour += 1 #Increases hour value by 1
        if hour>0:
            label0.config(text='Time Working: '+ str(hour)+'h '+str(minut)+'m '
                          +str(second)+'s',font=font0)  
        label0.after(1000, timecount) # Delay before continuing function
    timecount()

time() # Runs time() function 
####################################################################################
####################################################################################
### Task Counter ###################################################################
counter=[0] # Saves number of times a objective was reached
label1 = Label(window, fg="green") # Creates label1
# label1 configuration
label1.config(text='Operations Performed: '+ str(counter[0]),font=font0)
label1.grid(row=8,rowspan=3) # label placement
# Funtion definition
def count():
    global counter # Import counter list
    counter[0]=counter[0]+1 # Incrases counter value by 1
    label1.config(text='Operations Performed: '+ str(counter[0]),font=font0)    
####################################################################################
####################################################################################
####################################################################################
### Resets Counter #################################################################
def reset():
    global counter # Import counter list
    counter[0] = 0 # Sets counter list value to 0
    label1.config(text='Operations Performed: '+ str(counter[0]),font=font0)
####################################################################################
####################################################################################
####################################################################################
### Defines New Objective ##########################################################
def questcall():
    for id in canvas.find_overlapping(1280, 595, 1290, 605):
        robotcolor = canvas.itemcget(id, 'fill')
        if robotcolor == 'yellow':
            randcolor = random()
            canvas.itemconfig(light, fill=randcolor)
####################################################################################
####################################################################################
####################################################################################
### Piking Random Color from Color List ############################################    
def random():
    import random
    random.choice(color) # Returns a random color from color list
    return random.choice(color)                                                         
####################################################################################
####################################################################################
####################################################################################
### Sends Robot to the objective when called #######################################
def beginquest():
    # Identifies Objective Color
    for id in canvas.find_overlapping(1230, 700, 1330, 620):
        callcolor = canvas.itemcget(id, 'fill')
    # Detection of the Robot presence at the starting position
    for id in canvas.find_overlapping(1280, 595, 1290, 605):
        robotcolor = canvas.itemcget(id, 'fill')
        # Allows fucntion call if the robot is at the starting position
        if robotcolor == 'yellow':
            if callcolor=='blue': # Moves towards Blue Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(1223):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'darkblue': # Moves towards Dark Blue Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(1223):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'lightblue': # Moves towards Light Blue Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(903):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'grey': # Moves towards Grey Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(903):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'violet': # Moves towards Violet Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(923):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'darkorange': # Moves towards Dark Orange Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(923):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function    
            elif callcolor == 'orange': # Moves towards Orange Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(608):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'salmon': # Moves towards Salmon Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(608):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'pink': # Moves towards Pink Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(623):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'purple': # Moves towards Purple Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(623):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'red': # Moves towards Red Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(303):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'silver': # Moves towards Silver Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(303):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'green': # Moves towards Green Box
                for i in range(543):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(323):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'lightgreen': # Moves towards Light Green Box
                for i in range(163):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(323):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                for i in range(135):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(63):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'darkgreen': # Moves towards Dark Green Box
                for i in range(410):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            elif callcolor == 'brown': # Moves towards Brown Box
                for i in range(273):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                        canvas.update()
                for i in range(53):
                    for x in range(50):
                        x1,y1,x2,y2=canvas.coords(robot)
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                        canvas.update()
                count() # Call count() function
            # Makes call Box white when movent ends
            canvas.itemconfig(light, fill='white')
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
### Makes Robot return to the starting position ####################################   
def returN():
    # Identification of the robot current position
    x1,y1,x2,y2=canvas.coords(robot)
    # Identification of the current objective color
    for id in canvas.find_overlapping(x1-5,y1-5,x2-5,y2-5):
        callcolor = canvas.itemcget(id, 'fill')
    if callcolor=='blue': # Returns from Blue Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()
        for i in range(1223):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'darkblue': # Returns from Dark Blue Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(1223):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'lightblue': # Returns from Light Blue Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()        
        for i in range(903):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()        
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        

    elif callcolor == 'grey': # Returns from Grey Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(903):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        

    elif callcolor == 'violet': # Returns from Violet Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()
        for i in range(923):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'darkorange': # Returns from Dark Orange Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(923):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
                
    elif callcolor == 'orange': # Returns from Orange Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()
        for i in range(608):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'salmon': # Returns from Salmon Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(608):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'pink': # Returns from Pink Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()
        for i in range(623):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'purple': # Returns from Purple Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(623):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'red': # Returns from Red Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()
        for i in range(303):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'silver': # Returns from Silver Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(303):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'green': # Returns from Green Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1-vy,x2,y2-vy)
                canvas.update()
        for i in range(323):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(543):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'lightgreen': # Returns from Light Green Box
        for i in range(63):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1-vx,y1,x2-vx,y2)
                canvas.update()
        for i in range(135):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
        for i in range(323):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(163):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'darkgreen': # Returns from Dark Green Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(410):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()

    elif callcolor == 'brown': # Returns from Brown Box
        for i in range(53):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1+vx,y1,x2+vx,y2)
                canvas.update()
        for i in range(273):
            for x in range(50):
                x1,y1,x2,y2=canvas.coords(robot)
                canvas.coords(robot,x1,y1+vy,x2,y2+vy)
                canvas.update()
####################################################################################
####################################################################################
####################################################################################
# List of possible box colors
color = ('blue','darkblue','lightblue','grey','violet','darkorange','orange',
         'salmon','pink','purple','red','silver','green','lightgreen','darkgreen',
         'brown')
# Robot Box
robot=canvas.create_rectangle(1275,590,1295, 610, width=2, fill='yellow')
# Objective Boxes
canvas.create_rectangle(125 , 125,  225, 250, fill=color[0]) # Blue Box
canvas.create_rectangle(125 , 250,  225, 375, fill=color[1]) # Dark Blue Box
canvas.create_rectangle(225 , 125,  325, 250, fill=color[2]) # Ligh Blue Box
canvas.create_rectangle(225 , 250,  325, 375, fill=color[3]) # Grey Box
canvas.create_rectangle(425 , 125,  525, 250, fill=color[4]) # Violet Box
canvas.create_rectangle(425 , 250,  525, 375, fill=color[5]) # Dark Orange Box
canvas.create_rectangle(525 , 125,  625, 250, fill=color[6]) # Orange Box
canvas.create_rectangle(525 , 250,  625, 375, fill=color[7]) # Salmon Box
canvas.create_rectangle(725 , 125,  825, 250, fill=color[8]) # Pink Box
canvas.create_rectangle(725 , 250,  825, 375, fill=color[9]) # Purple Box
canvas.create_rectangle(825 , 125,  925, 250, fill=color[10])# Red Box
canvas.create_rectangle(825 , 250,  925, 375, fill=color[11])# Silver Box
canvas.create_rectangle(1025, 125, 1125, 250, fill=color[12])# Green Box
canvas.create_rectangle(1025, 250, 1125, 375, fill=color[13])# Light Green Box
canvas.create_rectangle(1125, 125, 1225, 250, fill=color[14])# Dark Green Box
canvas.create_rectangle(1125, 250, 1225, 375, fill=color[15])# Brown Box
# Whareshouse Limit
canvas.create_rectangle(0   , 500, 1225, 510, fill='black') # Robot Bottom Limit
canvas.create_rectangle(1215, 510, 1225, 710, fill='black') # Robot House Left Limit
canvas.create_rectangle(0   , 710, 1350, 720, fill='black') # Bottom Limit 
canvas.create_rectangle(0   , 0  , 10  , 720, fill='black') # Left Limit
canvas.create_rectangle(1340, 0  , 1350, 720, fill='black') # Right Limit
canvas.create_rectangle(0   , 0  , 1350, 10 , fill='black') # Top Limit
### Box Barriers ############################################
canvas.create_rectangle(125 , 365,  325, 375, fill='black')                        
canvas.create_rectangle(425 , 365,  625, 375, fill='black') 
canvas.create_rectangle(725 , 365,  925, 375, fill='black') 
canvas.create_rectangle(1025, 365, 1225, 375, fill='black') 
canvas.create_rectangle(125 , 115,  325, 125, fill='black') 
canvas.create_rectangle(425 , 115,  625, 125, fill='black') 
canvas.create_rectangle(725 , 115,  925, 125, fill='black') 
canvas.create_rectangle(1025, 115, 1225, 125, fill='black') 
canvas.create_rectangle(220 , 115,  230, 365, fill='black') 
canvas.create_rectangle(520 , 115,  530, 365, fill='black') 
canvas.create_rectangle(820 , 115,  830, 365, fill='black') 
canvas.create_rectangle(1120, 115, 1130, 365, fill='black') 
canvas.create_rectangle(  10, 245, 1225, 255, fill='black') 
#############################################################
# Box Call
light=canvas.create_rectangle(1225, 710, 1340, 610, fill='white')
####################################################################################
####################################################################################
####################################################################################
vx = 0.02   # x velocity 
vy = 0.02    # y velocity
          
# Font definition
font1 = font.Font(size=13, weight='bold')

# Quest Call Button
buttonQC=Button(canvasframe,text='Quest\nCall',command=questcall,bg='lightblue',
               height=9, width=17)
buttonQC.place(x=10,y=10) 
buttonQC['font'] = font1

# Begin Quest Button
buttonBQ=Button(canvasframe,text='Begin\nQuest',command=beginquest,bg='lightblue',
               height=9, width=17)
buttonBQ.place(x=198,y=10)
buttonBQ['font'] = font1

# Return Button
buttonR=Button(canvasframe,text='Return', command=returN, bg='lightblue',
               height=9, width=17)
buttonR.place(x=386,y=10)
buttonR['font'] = font1

# Reset Button
buttonRst=Button(canvasframe,text='Reset', command=reset, bg='lightblue',
               height=9, width=17)
buttonRst.place(x=762,y=10)
buttonRst['font'] = font1

# Shutdown Button
buttonRst=Button(canvasframe,text='Shutdown',command=window.destroy,bg='lightblue',
               height=9, width=17)
buttonRst.place(x=950,y=10)
buttonRst['font'] = font1
####################################################################################
### Automatic/Manual Toggle Button #################################################
state=[0] # Toggle button current state list                                              
                                                                                   
def toggle(): # Funtion that defines toggle button                                 
                                       #
    if togbtn.config('text')[-1] == 'Manual':
        for id in canvas.find_overlapping(1280, 595, 1290, 605):                   
            robotcolor = canvas.itemcget(id, 'fill')#
            if robotcolor == 'yellow':                                                 
                togbtn.config(text='Automatic')                                        
                state[0]=1                                                               
    else:                                                                       
        togbtn.config(text='Manual')                                                                
        state[0]=0                                                                 
                                                                                   
    while state[0]==1:                                                             
        questcall()                                                             
        beginquest()                                                                
        returN()                                                                   
                                                                                                                                
togbtn = Button(canvasframe,text="Manual", command=toggle, bg='lightblue',              
               height=9, width=17)                                                                
togbtn.place(x=574,y=10)                                                                
togbtn['font'] = font1                                                             
####################################################################################
### Crete the control box ########################################################## 
canvas.create_rectangle(13,513,1215,707,width=5, outline='blue')
### Complete the GUI ###############################################################
# .state('zoomed') forces the window to be the equal to the screen size
window.state('zoomed') 
