# Driver code
if __name__ == "__main__":
    # create a GUI window
    from tkinter import *

    gui = Tk()

    gui.title("Heart Disease Predictor")

    gui.geometry('300x370')

    enter_lbl = Label(gui, text="Enter the Following:")
    enter_lbl.grid(column=0, row=0)

    age_lbl = Label(gui, text="Age")
    age_lbl.grid(column=0, row=1)

    var_age=StringVar()
    age_txt = Entry(gui,width=10, textvariable=var_age)
    age_txt.grid(column=1, row=1)

    sex_lbl = Label(gui, text="Sex")
    sex_lbl.grid(column=0, row=2)

    selected_sex = IntVar()
    rad1 = Radiobutton(gui,text='Male', value=1, variable=selected_sex)
    rad2 = Radiobutton(gui,text='Female', value=0, variable=selected_sex)
    rad1.grid(column=1, row=2)
    rad2.grid(column=2, row=2)

    cp_lbl = Label(gui, text="CP")
    cp_lbl.grid(column=0, row=3)

    var_cp=StringVar()
    cp_txt = Entry(gui,width=10, textvariable=var_cp)
    cp_txt.grid(column=1, row=3)

    lbl1 = Label(gui, text="(0-3)")
    lbl1.grid(column=2, row=3)

    trestbps_lbl = Label(gui, text="Trestbps")
    trestbps_lbl.grid(column=0, row=4)

    var_trestbps=StringVar()
    trestbps_txt = Entry(gui,width=10, textvariable=var_trestbps)
    trestbps_txt.grid(column=1, row=4)

    chol_lbl = Label(gui, text="Chol")
    chol_lbl.grid(column=0, row=5)

    var_chol=StringVar()
    chol_txt = Entry(gui,width=10, textvariable=var_chol)
    chol_txt.grid(column=1, row=5)

    fbs_lbl = Label(gui, text="Fbs")
    fbs_lbl.grid(column=0, row=6)

    selected_fbs = IntVar()
    rad3 = Radiobutton(gui,text='True', value=1, variable=selected_fbs)
    rad4 = Radiobutton(gui,text='False', value=0, variable=selected_fbs)
    rad3.grid(column=1, row=6)
    rad4.grid(column=2, row=6)

    restecg_lbl = Label(gui, text="Restecg")
    restecg_lbl.grid(column=0, row=7)

    var_restecg=StringVar()
    restecg_txt = Entry(gui,width=10,textvariable=var_restecg)
    restecg_txt.grid(column=1, row=7)

    lbl2 = Label(gui, text="(0-2)")
    lbl2.grid(column=2, row=7)

    thalach_lbl = Label(gui, text="Thalach")
    thalach_lbl.grid(column=0, row=8)

    var_thalach=StringVar()
    thalach_txt = Entry(gui,width=10,textvariable=var_thalach)
    thalach_txt.grid(column=1, row=8)

    exang_lbl = Label(gui, text="Exang")
    exang_lbl.grid(column=0, row=9)

    selected_exang = IntVar()
    rad5 = Radiobutton(gui,text='Yes', value=1, variable=selected_exang)
    rad6 = Radiobutton(gui,text='No', value=0, variable=selected_exang)
    rad5.grid(column=1, row=9)
    rad6.grid(column=2, row=9)

    oldpeak_lbl = Label(gui, text="Oldpeak")
    oldpeak_lbl.grid(column=0, row=10)

    var_oldpeak=StringVar()
    oldpeak_txt = Entry(gui,width=10,textvariable=var_oldpeak)
    oldpeak_txt.grid(column=1, row=10)

    slope_lbl = Label(gui, text="Slope")
    slope_lbl.grid(column=0, row=11)

    var_slope=StringVar()
    slope_txt = Entry(gui,width=10,textvariable=var_slope)
    slope_txt.grid(column=1, row=11)

    lbl3 = Label(gui, text="(0-2)")
    lbl3.grid(column=2, row=11)

    ca_lbl = Label(gui, text="Ca")
    ca_lbl.grid(column=0, row=12)

    var_ca=StringVar()
    ca_txt = Entry(gui,width=10,textvariable=var_ca)
    ca_txt.grid(column=1, row=12)

    lbl4 = Label(gui, text="(0-3)")
    lbl4.grid(column=2, row=12)

    thal_lbl = Label(gui, text="Thal")
    thal_lbl.grid(column=0, row=13)

    var_thal=StringVar()
    thal_txt = Entry(gui,width=10,textvariable=var_thal)
    thal_txt.grid(column=1, row=13)

    lbl5 = Label(gui, text="(1-3)")
    lbl5.grid(column=2, row=13)

    result_lbl = Label(gui, text="Do You Have Heart Disease")
    result_lbl.grid(column=0, row=15)

    result=StringVar()
    result_txt = Entry(gui,width=10,textvariable=result)
    result_txt.grid(column=1, row=15)


    def clicked():
        import numpy as np
        import pickle
        
        model = pickle.load(open('final_model.sav', 'rb'))

        age=int(var_age.get())
        sex=selected_sex.get()
        cp=int(var_cp.get())
        trestbps=int(var_trestbps.get())
        chol=int(var_chol.get())
        fbs=selected_fbs.get()
        restecg=int(var_restecg.get())
        thalach=int(var_thalach.get())
        exang=selected_exang.get()
        oldpeak=float(var_oldpeak.get())
        slope=int(var_slope.get())
        ca=int(var_ca.get())
        thal=int(var_thal.get())

        l=np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        l=l.astype(np.float64)

        y_pred=model.predict([l])

        if y_pred==1:
            result.set("Yes")
        elif y_pred==0:
            result.set("No")

    def clear():
        var_age.set("")
        selected_sex.set(1)
        var_cp.set("")
        var_trestbps.set("")
        var_chol.set("")
        selected_fbs.set(1)
        var_restecg.set("")
        var_thalach.set("")
        selected_exang.set(1)
        var_oldpeak.set("")
        var_slope.set("")
        var_ca.set("")
        var_thal.set("")
        result.set("")

    submit_btn = Button(gui, text="Submit", command=clicked)
    submit_btn.grid(column=1, row=14)

    clear_btn= Button(gui, text="Clear", command=clear)
    clear_btn.grid(column=2, row=14)

    gui.mainloop()
