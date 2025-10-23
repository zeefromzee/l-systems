import turtle
import tkinter
import customtkinter as CTk


#This code attempts to create a simple L-System simulator using the turtle graphics library in Python. The L-System is a type of formal grammar used to model the growth processes of plant development. The code defines a set of rules for generating a string of commands, which are then interpreted by the turtle to draw a fractal pattern.
class Lsystems(CTk.CTk):

                        def __init__(self):
                                                super().__init__()
                                                self.title("L-System")
                                                self.geometry("936x550")
                                                self.main_frame = CTk.CTkFrame(
                                                    self,
                                                    fg_color="#FFDDDD",
                                                    border_color="black",
                                                    border_width=1,
                                                    width=936,
                                                    height=550)
                                                self.main_frame.place(x=0, y=0)

                                                self.header()
                                                self.recurrsions_btn()

                        def header(self):
                                                self.btn = CTk.CTkButton(
                                                    self,
                                                    text="L-SYSTEMS SIMULATOR",
                                                    width=936,
                                                    height=95,
                                                    fg_color="#FFDDDD",
                                                    text_color="#1E1E1E",
                                                    hover_color="#FFDDDD",
                                                    corner_radius=0,
                                                    font=("Roboto Mono", 32))
                                                self.btn.pack(pady=0,
                                                              anchor="n")

                        def processString(self, oldStr):
                                                newstr = ""
                                                for ch in oldStr:
                                                                        newstr = newstr + self.applyRules(
                                                                            ch)

                                                return newstr

                        def createLSystem(self, numIters, axiom):
                                                startString = axiom
                                                endString = ""
                                                for i in range(numIters):
                                                                        endString = self.processString(
                                                                            startString
                                                                        )
                                                                        startString = endString

                                                return endString

                        def applyRules(self, ch):
                                                newstr = ""
                                                if ch == 'F':
                                                                        newstr = 'F-F++F-F'  # Rule 1
                                                else:
                                                                        newstr = ch  # no rules apply so keep the character

                                                return newstr

                        def drawLsystem(self, aTurtle, instructions, angle,
                                        distance):
                                                for cmd in instructions:
                                                                        if cmd == 'F':
                                                                                                aTurtle.forward(
                                                                                                    distance
                                                                                                )
                                                                        elif cmd == 'B':
                                                                                                aTurtle.backward(
                                                                                                    distance
                                                                                                )
                                                                        elif cmd == '+':
                                                                                                aTurtle.right(
                                                                                                    angle
                                                                                                )
                                                                        elif cmd == '-':
                                                                                                aTurtle.left(
                                                                                                    angle
                                                                                                )


                        
                        def recurrsions_btn(self):
                                                
                                                self.btn = CTk.CTkButton(
                                                    self,
                                                    text="+",
                                                    width=100,
                                                    height=50,
                                                    fg_color="#FFDDDD",
                                                    text_color="#1E1E1E",
                                                    hover_color="#FFDDDD",
                                                    corner_radius=2,
                                                    font=("Roboto Mono", 25))
                                                self.btn.place(x=100, y=100)
                                                
                                                self.btn1 = CTk.CTkButton(
                                                    self,
                                                    text="-",
                                                    width=100,
                                                    height=50,
                                                    fg_color="#FFDDDD",
                                                    text_color="#1E1E1E",
                                                    hover_color="#FFDDDD",
                                                    corner_radius=2,
                                                    font=("Roboto Mono", 30))
                                                self.btn1.place(x=200, y=100)

                                                self.btn2 = CTk.CTkButton(
                                                    self,
                                                    text="F",
                                                    width=100,
                                                    height=50,
                                                    fg_color="#FFDDDD",
                                                    text_color="#1E1E1E",
                                                    hover_color="#FFDDDD",
                                                    corner_radius=2,
                                                    font=("Roboto Mono", 30))
                                                self.btn2.place(x=300, y=100)

                                                self.btn3 = CTk.CTkButton(
                                                    self,
                                                    text="B",
                                                    width=100,
                                                    height=50,
                                                    fg_color="#FFDDDD",
                                                    text_color="#1E1E1E",
                                                    hover_color="#FFDDDD",
                                                    corner_radius=2,
                                                    font=("Roboto Mono", 30))
                                                self.btn3.place(x=400, y=100)


app = Lsystems()
app.mainloop()
