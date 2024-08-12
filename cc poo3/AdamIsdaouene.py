from tkinter import *
from tkinter import messagebox
class Contact():
   
    
    T = [ ]
    #---------function pour ajouter les contacts-----------
    def ajouter():
        D = { }
        try:
            name_gui = txt_nom.get()
            D["name"] = name_gui
            
            prenom_gui = txt_Prenom.get()
            D["prenom"] = prenom_gui
            
            adresse_gui = txt_Adresse.get()
            D["adresse"] = adresse_gui
            
            num_gui = txt_numero.get()
            D["numero"] = int(num_gui)
            Contact.T.append(D)
            messagebox.showinfo("Success", "Good !!")
            txt_nom.delete(0 ,END)
            txt_Prenom.delete(0 ,END)
            txt_Adresse.delete(0 ,END)
            txt_numero.delete(0 ,END)
        except Exception as e :
                messagebox.showwarning("Error", f"Il ya un Error in {e}")

        
    #-----function pour afficher les contact-----------    
    def afficher():
        affigher_contact_root = Tk()
        text = Label(affigher_contact_root , text="Les Contact : " , bg="pink")
        text.pack()
        text_1 = Label(affigher_contact_root , text="*"*20)   
        text_1.pack()
        

        for a in Contact.T:
            for k in a.keys():
                kk = (k,"->",a[k])
                text_2 = Label(affigher_contact_root, text=kk)
                text_2.pack()
            text_3 = Label(affigher_contact_root , text = "-"*20)
            text_3.pack()
        text_4 = Label(affigher_contact_root , text="*"*20)
        text_4.pack()       
        
        affigher_contact_root.mainloop()

    #------function pour supprimer----------            
    def suppimer():
        code = inpt_num.get()
        for item in Contact.T:
            if item["name"]==code:
                Contact.T.remove(item)
                N=N-1
        messagebox.showinfo("Success", "Le Contatc supprimer !!")
        inpt_num.delete(0,END)
        
        
    #-------function pour sauvgarder----------    
    def save_as_file():
        with open("Les.txt","w") as fichier:
            for i in range(20):
                fichier.write(str(Contact.T[i]))
                fichier.write("\n")
    
#la creation de page-----         
root = Tk()
root.title("Application de Carnet d'Adresses")


#-----name--input-----
le_name = Label(root, text="  Enter Le Nom : ") 
le_name.grid(row=0 , column=0)
txt_nom = Entry(root)
txt_nom.grid(row=0 , column=1)


#-------Prénom--input------

le_prenom = Label(root ,text="Enter Le Prenom : " )
txt_Prenom = Entry(root )
le_prenom.grid(row=1 , column=0)
txt_Prenom.grid(row=1 , column=1)

#-------Adresse--input-------

le_Adresse = Label(root , text="Enter L'Adresse : ")
txt_Adresse = Entry(root )
le_Adresse.grid(row=2 , column=0)
txt_Adresse.grid(row=2 , column=1)

#----Numéro de téléphone------
le_numero = Label(root , text="Enter le Numéro de téléphone : ")
txt_numero = Entry(root )
le_numero.grid(row= 3, column=0)
txt_numero.grid(row=3 , column=1)

#-----button--------------

btn_ajouter = Button(root , text="Ajouter",bg="green" , command=Contact.ajouter)
btn_ajouter.grid(row=5 , column=0)




btn_afficher__contacts = Button(root , text="afficher des contacts",bg="yellow", command=Contact.afficher)
btn_afficher__contacts.grid(row = 5 , column=2 )


#-----zone d'supprimer--------------
txt_delete_root = Label(root , text="Enter le contact a supprimer: ")
txt_delete_root.grid(row=7 , column=0)
inpt_num = Entry(root)
inpt_num.grid(row=7 , column=1)



btn_supprimer = Button(root , text="supprimer" , bg="skyblue" , command=Contact.suppimer)
btn_supprimer.grid(row = 7 , column=2)                  



#--------Menu-----------
menubar = Menu(root)
root.config(menu=menubar)
menufichier = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Commands", menu=menufichier)

menufichier.add_command(label="Enregistrer" , command=Contact.save_as_file)

menufichier.add_command(label="Quitter" , command=quit)            
root.mainloop()