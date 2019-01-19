from tkinter import *

import requests

import tkinter as tk
import tkinter as tkF

from tkinter import font
from tkinter import Text, Tk







root=Tk()

root.configure(background='#13366d')

root.geometry('1366x768')

root.title('Weather App')





customFont = font.Font(family="Calibri", size=23)

customFontRe = font.Font(family="Calibri", size=23)

customFont1 = font.Font(family="Calibri", size=9)

customFont2 = font.Font(family="Calibri", size=10)

customFont3 = font.Font(family="Calibri", size=13)

customFontD = font.Font(family="Calibri", size=15)

customFontR = font.Font(family="Calibri", size=11)

customFonttopL = font.Font(family="Calibri", size=15)

customFont4 = font.Font(family="Calibri", size=14)

customFont5 = font.Font(family="Calibri", size=27)



welcomeLabel=Label(root,text="Welcome To Our Weather App",font=customFont,bg="#13366d",fg="white")

welcomeLabel.place(relx=0.99, rely=0.14, anchor='se')









EnterNameL=Label(root,text="Enter City Name :  ",font=customFont3,bg="#13366d",fg="#f9e2ca")

EnterNameL.pack(side=LEFT)

EnterNameL.place(relx=0.4, rely=0.44, anchor='se')



citynameE=Entry(root,bd=3,width=24,bg="#fca549",fg="#161613",font=customFont1)

citynameE.place(relx=0.87, rely=0.44, anchor='se')









def getWeather():

    url = "http://api.openweathermap.org/data/2.5/weather?q=" + citynameE.get() + "&appid=c16b30e1ad84ce3366830e9689d38e82"



    data = requests.get(url)

    read = data.json()




    country=(format(read['sys']['country']))

    cityname=StringVar()

    cityname.set(format(read['name'])+","+country)

    wdescrip=StringVar()

    wdescrip.set(format(read['weather'][0]['description']).title())



    humidity=StringVar()

    humidity.set(format(read['main']['humidity'])+ " F")

    pressure=StringVar()

    pressure.set(format(read['main']['pressure'])+" atm")



    temp = float(format(read['main']['temp']))

    tempInC = float(temp - 273.14)

    temperature=StringVar()

    temperature.set(str(tempInC)+" C")

    windSpeed=StringVar()

    windSpeed.set(format(read['wind']['speed'])+" mph")

    clouds=StringVar()

    clouds.set(format(read['clouds']['all'])+ " %")



    top = Toplevel(root)

    top.geometry('430x430')

    top.configure(background='#13366d')





    tiltL=Label(top,text="--Weather Reports--",fg="White",font=customFontRe,bg="#13366d")

    tiltL.place(relx=0.84, rely=0.16, anchor='se')



    citynameL = Label(top,  textvariable=cityname,bg="#13366d", fg="#ce1a1a",font=customFont5)

    citynameL.place(relx=0.65, rely=0.3, anchor='se')



    Labeldescrip= Label(top, text="Weather Type : ", bg="#13366d",fg="#E4FEFF",font=customFonttopL)

    Labeldescrip.place(relx=0.38, rely=0.4, anchor='se')



    Labelhumidity = Label(top, text="Humidity : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)

    Labelhumidity.place(relx=0.38, rely=0.48, anchor='se')



    Labelpressure = Label(top, text="Pressure : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)

    Labelpressure.place(relx=0.38, rely=0.56, anchor='se')



    LabelWind = Label(top, text="Wind Speed : ", bg="#13366d",fg="#E4FEFF",font=customFonttopL)

    LabelWind.place(relx=0.38, rely=0.64, anchor='se')



    LabelClouds = Label(top, text="Clouds : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)

    LabelClouds.place(relx=0.38, rely=0.72, anchor='se')



    LabelTemp = Label(top, text="Temp : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)

    LabelTemp.place(relx=0.38, rely=0.8, anchor='se')



    wdescripL = Label(top, textvariable=wdescrip, bg="#13366d", fg="white",font=customFont4)

    wdescripL.place(relx=0.73, rely=0.398, anchor='se')



    humidityL = Label(top,  textvariable=humidity, bg="#13366d", fg="white")

    humidityL.place(relx=0.60, rely=0.47, anchor='se')

    

    pressureL = Label(top,textvariable=pressure, bg="#13366d", fg="white")

    pressureL.place(relx=0.62, rely=0.54, anchor='se')





    windSpeedL = Label(top,textvariable=windSpeed, bg="#13366d", fg="white")

    

    windSpeedL.place(relx=0.62, rely=0.62, anchor='se')

    cloudsL = Label(top, textvariable=clouds, bg="#13366d",fg="white")

    cloudsL.place(relx=0.59, rely=0.70, anchor='se')

    

    TempL = Label(top, textvariable=temperature, bg="#13366d", fg="white")

    TempL.place(relx=0.60, rely=0.79, anchor='se')












b = Button(root, text="Get Weather !", command=getWeather,font=customFontR,bg="#ce1a1a",width=33,height=3,fg="white")

b.place(relx=0.83, rely=0.68, anchor='se')



deveL=Label(root,text="-Developed By Shreekant Gosavi",bg="#13366d",fg="white",font=customFontD)

deveL.place(relx=0.77, rely=0.77, anchor='se')



root.mainloop()

