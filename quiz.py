from tkinter import *

NAN = float("NaN") # Not A Number: a value which can be used to
                   # express undefined float numbers in the program.

class GUI:
  def __init__(self):
    self.__float_result = NAN

    self.__main_window = Tk()

    # Creating the components of the GUI
    self.__entryA          = Entry(self.__main_window)


    self.__labelA          = Label(self.__main_window, text="A:")


    self.__result_title    = Label(self.__main_window, text="Result:")
    self.__result_label = Label(self.__main_window, text=NAN)
    self.__result_button    = Button(self.__main_window, text='press', command=self.get_valus)  # ✯✯✯


    # Positioning the components with grid geometry manager
    self.__labelA.grid(row=0, column=0, sticky=E)
    self.__entryA.grid(row=0, column=1, columnspan=2)

    self.__result_title.grid(row=1, column=3, sticky=E)
    self.__result_label.grid(row=1, column=4)
    self.__result_button.grid(row=1, column=5)

    self.__main_window.mainloop()

  def get_valus(self):
      try:
          a= float(self.__entryA.get())
          self.__float_result=a
          if self.__float_result < 0:

              self.__result_label.configure(text='Error number negative')
          elif self.__float_result > 0:
              self.__result_label.configure(text=f'{self.__float_result}')


      except:
          self.__float_result=0.0
          self.__result_label.configure(text='Error not number')







def main():

    gui=GUI()


if __name__ == "__main__":
    main()