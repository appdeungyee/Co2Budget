# 이 코드를 실행시키려면 ChromeDrive와 Selenium을 다운해야합니다. 이점 참고하시기 바랍니다.
# 이 코드는 MacOS에서 직성이 되었습니다. Window에서는 실행이 불가할 수 도 있으니, 이점 양해해주시기 바랍니다.

from selenium import webdriver
from tkinter import *
from time import *
from webbrowser import *
frame = ()
check = 1
check2 = 1
Link = 'https://www.mcc-berlin.net/fileadmin/data/clock/carbon_clock.htm'


def btngrid1_5():
    global btn1  # 에러이유: 글로벌 선언을 까먹고 안했었다.
    global check
    print(check)
    if check == 1:
        btn1 = Button(frame1, text='.', command=lambda: btngrid1_5())
        btn1.destroy()
        years1_5.grid(row=2, column=0)
        month1_5.grid(row=2, column=1)
        days1_5.grid(row=2, column=2)
        seconds1_5.grid(row=2, column=3)
        milliseconds1_5.grid(row=2, column=4)
        btn1 = Button(frame1, text='숨기기', command=lambda: btngrid1_5())
        label.grid(row=5, column=0, columnspan=5) #time
        btn1.grid(row=3, column=0, columnspan=5)
        Ton1.grid(row=6, column=0, columnspan=5) # How much left
        check = 2

    elif check == 2:
        btn1 = Button(frame1, text='.', command=lambda: btngrid1_5())
        btn1.destroy()
        years1_5.grid_forget()
        month1_5.grid_forget()
        days1_5.grid_forget()
        seconds1_5.grid_forget()
        milliseconds1_5.grid_forget()
        label.grid_forget()
        btn1 = Button(frame1, text='보기', command=lambda: btngrid1_5())
        btn1.grid(row=3, column=0, columnspan=5)
        Ton1.grid_forget() # How much?
        check = 1


def btngrid2_0():
    global btn2
    global check2
    print(check2)
    if check2 == 1:
        btn2 = Button(frame2, text='.', command=lambda: btngrid2_0())
        btn2.destroy()
        years2_0.grid(row=2, column=0)
        month2_0.grid(row=2, column=1)
        days2_0.grid(row=2, column=2)
        seconds2_0.grid(row=2, column=3)
        milliseconds2_0.grid(row=2, column=4)
        btn2 = Button(frame2, text='숨기기', command=lambda: btngrid2_0())

        label2.grid(row=5, column=0, columnspan=5)

        btn2.grid(row=3, column=0, columnspan=5)

        Ton2.grid(row=6, column=0, columnspan=5)
        check2 = 2

    elif check2 == 2:
        btn2 = Button(frame2, text='.', command=lambda: btngrid2_0())
        btn2.destroy()
        years2_0.grid_forget()
        month2_0.grid_forget()
        days2_0.grid_forget()
        seconds2_0.grid_forget()
        milliseconds2_0.grid_forget()
        label2.grid_forget()
        btn2 = Button(frame2, text='보기', command=lambda: btngrid2_0())
        btn2.grid(row=3, column=0, columnspan=5)
        Ton2.grid_forget()
        check2 = 1


def GoLink():
    open(Link)


root = Tk()
root.title("Co2 Budget made by Appdeungyee!!")  # 이름 설정
root.geometry("700x300+100+250")
root.resizable(False, False) # x, y
# image = PhotoImage(file="dlab_logo.png")
# image2 = PhotoImage(file='buykfR0Z_400x400.png')
# Img = PhotoImage(file='Earth.png')


frame2 = LabelFrame(root, relief="solid", bd=1, text='2.0')
frame2.pack(side='left', fill='both', expand=True)
frame1 = LabelFrame(root, relief="solid", bd=1, text='1.5')
frame1.pack(side='right',fill= 'both', expand=True)


browser = webdriver.Chrome('./chromedriver')

browser.implicitly_wait(3) # 웹 로딩까지 기다리기

URL = "https://www.mcc-berlin.net/fileadmin/data/clock/carbon_clock.htm"

browser.get(URL)  # 사이트에 접속

time2_0 = {}
time1_5 = {}

count_down = browser.find_elements_by_css_selector('#timecountdown td')
tonsC2 = browser.find_element_by_css_selector('#carbontonnes').text




for c in count_down:
    time2_0[c.get_attribute('id')] = c.text # 2.0도 정보 찾기


browser.find_element_by_id('1.5').click()
sleep(0.1)


for c in count_down:
    time1_5[c.get_attribute('id')] = c.text  # 1.5도 정보 찾기

tonsC = browser.find_element_by_css_selector('#carbontonnes').text



print(time2_0)
print(time1_5)


text1 = 'About {}years {}months {}days {}.{}seconds left until the temperature reaches 1.5℃'.format(time1_5['years'], time1_5['months'], time1_5['days'], time1_5['seconds'], time1_5['milliseconds'])
text2 = 'About {}years {}months {}days {}.{}seconds left until the temperature reaches 2℃'.format(time2_0['years'], time2_0['months'], time2_0['days'], time2_0['seconds'], time2_0['milliseconds'])



browser.quit()

btn1 = Button(frame1, text='보기', command=lambda: btngrid1_5())
btn2 = Button(frame2, text='보기', command=lambda: btngrid2_0())
btnL = Button(frame2, text='상세정보(링크들어가기)', command=lambda: GoLink())
btnL2 = Button(frame1, text='상세정보(링크들어가기)', command=lambda: GoLink())
label = Label(frame1, text=text1) # 시간알려줌
label2 = Label(frame2, text=text2)
Lyears = Label(frame1, text='Years', width=5, bg='cyan', fg='white')
Lmonths = Label(frame1, text='Months', width=5, bg='purple', fg='white')
Ldays = Label(frame1, text='Days', width=5, bg='black', fg='white')
Lseconds = Label(frame1, text='Seconds', width=8, bg='red', fg='white')
Lmls = Label(frame1, text='Milliseconds', width=10, bg='green', fg='white')

Ton1 = Label(frame1, text='{}{}'.format(tonsC, 'tons left'))
Ton2 = Label(frame2, text='{}{}'.format(tonsC2, 'tons left'))
# Me = Label(frame2, text='made by 박전한결 from Dlab Suseong Campus')
# MeDos = Label(frame2, text='made by 박전한결 from Dlab Suseong Campus')



Lyears2 = Label(frame2, text='Years', width=5, bg='cyan', fg='white')
Lmonths2 = Label(frame2, text='Month', width=5, bg='purple', fg='white')
Ldays2 = Label(frame2, text='Days', width=5, bg='black', fg='white')
Lseconds2 = Label(frame2, text='Seconds', width=8, bg='red', fg='white')
Lmls2 = Label(frame2, text='Milliseconds', width=10, bg='green', fg='white')


years1_5 = Label(frame1, text=time1_5['years'])
month1_5 = Label(frame1, text=time1_5['months'])
days1_5 =  Label(frame1, text=time1_5['days'])
seconds1_5 = Label(frame1, text=time1_5['seconds'])
milliseconds1_5 = Label(frame1, text=time1_5['milliseconds'])


#  --------------------


years2_0 = Label(frame2, text=time2_0['years'])
month2_0 = Label(frame2, text=time2_0['months'])
days2_0 = Label(frame2, text=time2_0['days'])
seconds2_0 = Label(frame2, text=time2_0['seconds'])
milliseconds2_0 = Label(frame2, text=time2_0['milliseconds'])
# wall_label = Label(frame1, image = image)
# image_label= Label(frame2, image = image2)
# Earth = Label(frame1, image=Img)


Lyears.grid(row=1, column=0)
Lyears2.grid(row=1, column=0)
Lmonths.grid(row=1, column=1)
Lmonths2.grid(row=1, column=1)
Ldays.grid(row=1, column=2)
Ldays2.grid(row=1, column=2)
Lseconds.grid(row=1, column=3)
Lseconds2.grid(row=1, column=3)
Lmls.grid(row=1, column=4)
Lmls2.grid(row=1, column=4)
btn1.grid(row=3, column=0, columnspan=5)
btn2.grid(row=3, column=0, columnspan=5)
btnL.grid(row=4, column=0, columnspan=5)
btnL2.grid(row=4, column=0, columnspan=5)
# wall_label.place(x=180, y=150)
# Me.grid(row=6, column=0)
# image_label.place(x=180, y=80)
# Earth.grid(row=7,column=0, columnspan=5)


root.mainloop()
