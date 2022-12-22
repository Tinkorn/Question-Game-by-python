from tkinter import *
import csv


answers=[]
exams=[]
filepath_1="answers.txt"
filepath_2="exams.txt"



filepath="SCORE.txt"
Name_score=["Name","Score"]

with open(filepath,"w",encoding="utf-8")as outfile:
            writer = csv.writer(outfile,lineterminator="\n")   #lineterminator="\n" = list ที่ 1 เสร็จขึ้นบรรทัดใหม่
            writer.writerow(Name_score)

def cal_score(your_input,answers):
    real_score=0
    for i in range(5):          #ตรวจสอบว่าตรงกับเฉลยหรือไม่
        if your_input[i]==answers[i]:              
            real_score+=1
    return real_score
    
   
def re():
    mywin3.destroy()
    win1()

def win2():
    
    def win3():
        #PAGE 3++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        mywin2.destroy()#ปิดหน้าต่าง2

        x1=your_input1.get().strip() #รับ inputจาก GUI เเล้วตักเว้นวรรค เเละเก็บไว้ในตัวแปร x
        x2=your_input2.get().strip()
        x3=your_input3.get().strip()
        x4=your_input4.get().strip()
        x5=your_input5.get().strip()
        
        your_input=[]
        your_input.append(x1.lower()) #เปลี่ยนข้อมูลเป็นตัวพิมเล็กเเล้วเก็บข้อมูล ไว้ใน list your_input
        your_input.append(x2.lower())
        your_input.append(x3.lower())
        your_input.append(x4.lower())
        your_input.append(x5.lower())
        
        ###########################
        Name=name.get()
        global mywin3,score
        mywin3=Tk()
        mywin3.config(bg="#252b35")
        mywin3.minsize(500,100)
        ###########################
        
        real_score=cal_score(your_input,answers)
        score=Label(mywin3,text="{} your score is {}".format(Name,real_score),font="Tahoma 30 bold",bg="#252b35",fg="#eaeaea").grid(row=0,padx=100,pady=10)
        bt_try=Button(mywin3,text="Try again",command=re,width=10,bg="#08d9d6").grid(row=1,pady=10)
        bt_close1=Button(mywin3,text="CLOSE",command=mywin3.destroy,width=10,bg="#ff2e62").grid(row=2,pady=10)
        

    
        
        score_list=[Name,real_score]
        
        with open(filepath,"a",encoding="utf-8")as outfile:   # a คือเพิ่มต่อท้าย ranหลายรอบก็เพิ่มตามจำนวนรอบที่run
            writer = csv.writer(outfile,lineterminator="\n")   #lineterminator="\n" = list ที่ 1 เสร็จขึ้นบรรทัดใหม่
            writer.writerow(score_list)
          
        mywin3.mainloop()
        
    #PAGE 2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
    ###########################
    mywin1.destroy() #ปิดหน้าต่าง1
    mywin2=Tk()
    mywin2.config(bg="#252b35")
    mywin2.minsize(600,250)
    
    your_input1=StringVar()
    your_input2=StringVar()
    your_input3=StringVar()
    your_input4=StringVar()
    your_input5=StringVar()
    ##########################
    
    HEAD=Label(mywin2,text="จงเติมคำภาษาอังกฤษ",font="Tahoma 20 bold",fg="#eaeaea",bg="#252b35").grid(row=0,column=1)

    for i in range(5):                
        exam=Label(mywin2,text=("{}".format(exams[i])),font="Tahoma 10 bold",fg="#eaeaea",bg="#252b35").grid(row=[i+3],column=0,padx=50) #แสดงโจทย์
        i+=1
        
    
    enter=Entry(mywin2,textvariable=your_input1).grid(row=3,column=1,pady=10)
    enter=Entry(mywin2,textvariable=your_input2).grid(row=4,column=1,pady=10)
    enter=Entry(mywin2,textvariable=your_input3).grid(row=5,column=1,pady=10)
    enter=Entry(mywin2,textvariable=your_input4).grid(row=6,column=1,pady=10)
    enter=Entry(mywin2,textvariable=your_input5).grid(row=7,column=1,pady=10)
    
    bt_ok=Button(mywin2,text="Let's Check",command=win3,width=10,bg="#08d9d6").grid(row=6,column=3)
    bt_close=Button(mywin2,text="CLOSE",command=mywin2.destroy,width=10,bg="#ff2e62").grid(row=7,column=3)
    
    mywin2.mainloop()
    
#PAGE 1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
#############################
def win1():
    
    
    global mywin1,name
    mywin1=Tk()
    
    
    name=StringVar()
    mywin1.config(bg="#252b35")
    mywin1.minsize(450,200)


    head=Label(mywin1,text="Input name",font="Tahoma 30 bold",bg="#252b35",fg="#eaeaea").grid(row=1,padx=110,column=0)
    namebox=Entry(mywin1,textvariable=name,width=40,bg="#eaeaea")
    namebox.grid(row=2,column=0,padx=110,pady=10)
    namebox.focus()

    bt_next=Button(mywin1,text="NEXT",command=win2,width=10,bg="#08d9d6").grid(row=3,column=0,pady=10)
    bt_close=Button(mywin1,text="CLOSE",command=mywin1.destroy,width=10,bg="#ff2e62").grid(row=4,column=0)

    try:
        with open(filepath_1,"r",encoding="utf-8")as f1:   #อ่าน ANESWES จากfile(เอาข้อมูลมาจากfile)
            while True:
                line=f1.readline()
                if len(line):
                    line=line.rstrip()
                    answers.append(line)
                else :
                    break
    
        with open(filepath_2,"r",encoding="utf-8")as f2:   #อ่าน EXAMS จากfile(เอาข้อมูลมาจากfile)
             while True:
                line=f2.readline()
                if len(line):
                    line=line.rstrip()
                    exams.append(line)
                else :
                    break
    except Exception as error:
        mywin1.destroy()
        print("Error")
        print(error)
    
    mywin1.mainloop()
    return mywin1

win1()

