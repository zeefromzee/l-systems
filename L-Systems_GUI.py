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
                                                    border_width=0,
                                                    font=("Roboto Mono", 32))
                                                self.btn.pack(pady=0,
                                                              anchor="n")

                        def processString(self,oldStr):
                                                newstr = ""
                                                for ch in oldStr:
                                                                        newstr = newstr + applyRules(ch)

                                                return newstr

                        def createLSystem(self, numIters,axiom):
                                                startString = axiom
                                                endString = ""
                                                for i in range(numIters):
                                                                        endString = processString(startString)
                                                                        startString = endString

                                                return endString

                        
                        def applyRules(ch):
                                                newstr = ""
                                                if ch == 'F':
                                                                        newstr = 'F-F++F-F'   # Rule 1
                                                else:
                                                                        newstr = ch    # no rules apply so keep the character

                                                return newstr

                        def drawLsystem(self, aTurtle, instructions, angle, distance):
                                                for cmd in instructions:
                                                                        if cmd == 'F':
                                                                                                aTurtle.forward(distance)
                                                                        elif cmd == 'B':
                                                                                                aTurtle.backward(distance)
                                                                        elif cmd == '+':
                                                                                                aTurtle.right(angle)
                                                                        elif cmd == '-':
                                                                                                aTurtle.left(angle)


app = Lsystems()
app.mainloop()
