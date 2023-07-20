from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import wolframalpha

def find_answer(question):
    app_id = 'JGTY7P-7Y3WP69XRV'
    the_client = wolframalpha.Client(app_id)  
    try:
        response = the_client.query(question)  
        answer = next(response.results).text
    except:  
        answer = ""

    return answer

def compute_result():
    answer_field.delete(0, END)  
    query = question_field.get()
    if query != "":  
        answer = find_answer(query)
    if answer != "":  
        answer_field.insert(0, answer)
    else:  
        answer_field.insert(0, "No Results Found!")  
        mb.showerror("No Results Found", "Oops! Unable to find the answer of the Query.")
    else:  
        mb.showerror("Empty Field", "Entry Field Cannot be Empty.")

def reset_entries():
    question_field.delete(0, END)  
    answer_field.delete(0, END)  
    mb.showinfo("Fields Reset", "All Fields are reset.")

def exit_application():
    main_win.destroy()

    if __name__ == '__main__':
        main_win = Tk()
        main_win.title("My Assistant - PAVAN")
        main_win.geometry("700x300+600+300")
        main_win.resizable(0, 0)  
        main_win.config(bg = "#F0FFFF")
        main_win.iconbitmap("./icons/assistant.ico")
        assist_img = ImageTk.PhotoImage(Image.open("./images/bot.png").resize((50, 50), Image.Resampling.LANCZOS))
        title_frame = Frame(main_win, bg = "#F0FFFF")     
        input_frame = Frame(main_win, bg = "#F0FFFF")     
        button_frame = Frame(main_win, bg = "#F0FFFF")

        title_frame.pack()  
        input_frame.pack(fill = "both", padx = 30)  
        button_frame.pack()
    heading = Label(  
        title_frame,  
        text = "My Assistant",  
        font = ("times new roman", "20", "bold"),  
        bg = "#F0FFFF",  
        fg = "#4169E1"  
        )
        image.grid(row = 0, column = 0, padx = 10, pady = 10)  
        heading.grid(row = 0, column = 1, padx = 10, pady = 10)
    question_label = Label(  
        input_frame,  
        text = "Enter the Query :",  
        font = ("times new roman", "12", "bold"),  
        bg = "#F0FFFF",  
        fg = "#191970"  
        )
     question_field = Entry(  
        input_frame,  
        width = 60,  
        font = ("times new roman", "12"),  
        bg = "#FFFFFF",  
        fg = "#000000",  
        relief = GROOVE  
        )
     answer_label = Label(  
        input_frame,  
        text = "Answer :",  
        font = ("times new roman", "12", "bold"),  
        bg = "#F0FFFF",  
        fg = "#191970"  
        )  
    answer_field = Entry(  
        input_frame,  
        width = 60,  
        font = ("times new roman", "12"),  
        bg = "#FFFFFF",  
        fg = "#000000",  
        relief = GROOVE  
        )  
    question_label.grid(row = 0, column = 0, padx = 10, pady = 0, sticky = W)  
    question_field.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)  
    answer_label.grid(row = 2, column = 0, padx = 10, pady = 0, sticky = W)  
    answer_field.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

      compute_button = Button(  
        button_frame,  
        text = "Go",  
        font = ("times new roman", "12"),  
        bg = "#00FF7F",  
        fg = "#000000",  
        activebackground = "#3CB371",  
        activeforeground = "#FFFFFF",   
        relief = GROOVE,  
        width = 12,  
        command = compute_result  
    )  
    
    reset_button = Button(  
        button_frame,  
        text = "Clear",  
        font = ("times new roman", "12"),  
        bg = "#DCDCDC",  
        fg = "#000000",  
        activebackground = "#696969",  
        activeforeground = "#FFFFFF",   
        relief = GROOVE,  
        width = 12,  
        command = reset_entries  
    )  
   
    close_button = Button(  
        button_frame,  
        text = "Cancel",  
        font = ("times new roman", "12"),  
        bg = "#FF0000",  
        fg = "#FFFFFF",  
        activebackground = "#8B0000",  
        activeforeground = "#FFFFFF",   
        relief = GROOVE,  
        width = 12,  
        command = exit_application  
    )  
   
    compute_button.grid(row = 0, column = 0, padx = 10, pady = 20)  
    reset_button.grid(row = 0, column = 1, padx = 10, pady = 20)  
    close_button.grid(row = 0, column = 2, padx = 10, pady = 20)
    
  main_win.mainloop()  
