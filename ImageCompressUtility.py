import cv2
import customtkinter
import os 
from customtkinter import filedialog
import threading
from PIL import Image

#Global variables
nooffilescompressed = 0
quality = 90
themestate = "Dark"
initpath=''
savepath=''

#Set theme to the GUI
customtkinter.set_appearance_mode(themestate)

#Function that changes the theme upon button toggle
def change_theme():
    global themestate
    if themestate == "Light":
        themestate = "Dark"
    elif themestate == "Dark":
        themestate = "Light"      
    customtkinter.set_appearance_mode(themestate)
    theme_switch.configure(text = themestate)  

#Function to open up the file manager and choose the folder containing the images
def select_files():
    global initpath,total_no_of_files
    initpath = filedialog.askdirectory().replace('/','\\\\') 
    total_no_of_files = len(os.listdir(initpath))

#Function to choose destination folder
def select_dest():
    global savepath
    savepath = filedialog.askdirectory().replace('/','\\\\')
    compress_button.configure(state = "normal")

#Updates the quality parameter shown in the label 
def update_label(pos):
    global quality
    quality = int(pos)
    qualitylabel.configure(text = "Quality: "+str(int(pos))+"%")

#Function that starts the compression thread in the background
def initcompress():
    bgcomp = threading.Thread(target= compress)
    bgcomp.start()

def compress() :
        nooffilescompressed = 0
        #Deactivating buttons/widgets while compression is in progress
        select_src_button.configure(command = None)  
        select_dest_button.configure(command = None)   
        compress_button.configure(state = "disabled")  
        slider.configure(state = "disabled")

        for filename in os.listdir(initpath):
            nooffilescompressed+=1
            try:
                image_preview = customtkinter.CTkImage(light_image=Image.open(initpath+r"/"+filename),dark_image=Image.open(initpath+r"/"+filename),size=(200,200))

                image_preview_label.configure(image =image_preview )
                image = cv2.imread(initpath+r"\\"+filename)
                status = cv2.imwrite(savepath+r"\\"+filename, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
                if status == True:
                    percent_reduce = ((os.path.getsize(initpath+r"\\"+filename)-os.path.getsize(savepath+r"\\"+filename))/os.path.getsize(initpath+r"\\"+filename))*100
                    statusmsg = "Done compressing: "+ filename+"  No of files compressed: "+str(nooffilescompressed)+"/"+str(total_no_of_files)+" Percentage reduction: "+str(abs(round(percent_reduce,2)))+"%"
                    progress_label.configure(text = statusmsg)    
            except:
                pass
               
        #Activating buttons/widgets after completion of compression
        select_src_button.configure(command = select_files)  
        select_dest_button.configure(command = select_dest) 
        slider.configure(state = "normal")
       
      
app= customtkinter.CTk()

#Initiating app geometry
app.geometry("1000x600")

#Source selection button
select_src_button = customtkinter.CTkButton(master=app, text="Select Files",command=select_files ,corner_radius=20,height=40,font=("Helvetica",15))
select_src_button.place(relx=0.4, rely=0.2, anchor=customtkinter.CENTER)

#Destination selection button
select_dest_button = customtkinter.CTkButton(master=app, text="Select Save Location",command=select_dest,corner_radius=20,height=40,font=("Helvetica",15))
select_dest_button.place(relx=0.6, rely=0.2, anchor=customtkinter.CENTER)

#Compress button
compress_button = customtkinter.CTkButton(master=app, text="Compress",command=initcompress,corner_radius=20,height=40,state="disabled",font=("Helvetica",15))
compress_button.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

#Slider to choose level of quality
slider = customtkinter.CTkSlider(master=app, from_=0, to=100,command=update_label)
slider.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER,)
slider.set(90) #Setting default quality to 95

#Label to display the quality parameter
qualitylabel = customtkinter.CTkLabel(master=app, text= "Quality: "+str(int(slider.get()))+"%",font=("Helvetica",15))
qualitylabel.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

#Indicates progress
progress_label = customtkinter.CTkLabel(master=app, text= "",font=("Helvetica",15))#
progress_label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

#Toggle button to trigger theme change
theme_switch=  customtkinter.CTkSwitch(master=app, text="Dark", command=change_theme,)
theme_switch.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

image_preview = customtkinter.CTkImage(light_image=Image.open('placeholderimg_black.png'),dark_image=Image.open('placeholderimg_white.png'),size=(200,200))
image_preview_label = customtkinter.CTkLabel(app, text="", image=image_preview)
image_preview_label.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)


#Toggles switch to 'ON' postion
theme_switch.select()

app.mainloop()






