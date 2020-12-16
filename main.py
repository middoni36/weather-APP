import tkinter as tk
import requests
import PIL
class weatherapp(tk.Tk):
     def __init__(self,title):
         super().__init__()
         self.API_KEY="52f7c1f4c29fa672b360b6c0336bd05f"
         self.header="https://pro.openweathermap.org/data/2.5/forecast" ##endpoint
         self.geometry("600x700")
         self.title(f"{title}")
         self.backgroundimage=tk.PhotoImage(file="C:/Users/w111361/Downloads/okbye.png")
         self.packthebuttons_in_canvas()



     def getweather(self,city):
         params={"APPID":"52f7c1f4c29fa672b360b6c0336bd05f",
                  "city":f"{city}",
                 "units":"imperial"

         }

         r=requests.get(self.header,params=params)
         print(r.json())


















     def packthebuttons_in_canvas(self):

         myframe=tk.Frame(self,bg="#7ecdf2",bd=5)
         myframe.place(relwidth=0.98,relheight=0.98,relx=0.01 ,rely=0.01) ## 70 procent from myinital frame gemeotry width and 85 from geometry height

         mylabel = tk.Label(myframe, image=self.backgroundimage)
         mylabel.place(relwidth=1, relheight=1)

         lower_frame = tk.Frame(myframe, bg="#aee8e3", bd=3)
         lower_frame.place(relx=0.02, rely=0.08, relwidth=1, relheight=0.1)



         entry = tk.Entry(lower_frame, bg="white",font=40,bd=5)
         entry.place(relx=0.01,rely=0.08,relwidth=0.68,relheight=0.8)




         buton_text=tk.Button(lower_frame,text="Get Weather",bg="White",font=40,bd=10,command=lambda : self.getweather(entry.get()))
         buton_text.place(relx=0.695,rely=0.08,relwidth=0.28,relheight=0.8)

         labelframe=tk.Frame(myframe,bg="#7ecdf2")
         labelframe.place(rely=0.23,relx="0.02",relheight=0.7,relwidth=0.98)

         label=tk.Label(labelframe,text="this a label",bg="white")
         label.place(relx=0.02,rely=0.01,relwidth=0.97,relheight=0.96)















if __name__ == '__main__':
    myweather=weatherapp("GUI weather")
    myweather.mainloop()
