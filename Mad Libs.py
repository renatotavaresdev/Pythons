from tkinter import *

window = Tk()
window.title('Mad Libs')

screen = Canvas(window, width=400, height=300)
screen.pack()

title = Label(window, text='Mad Libs Game', font='sans-serif 15 bold')
screen.create_window(200, 13, window=title)

input1_text = Label(window, text='Enter a color: ')
screen.create_window(60, 50, window=input1_text)

color_input = Entry(window)
screen.create_window(188, 50, window=color_input)


input2_text = Label(window, text='Enter a Plural Noun: ')
screen.create_window(80, 85, window=input2_text)

plural_input = Entry(window)
screen.create_window(230, 85, window=plural_input)

input3_text = Label(window, text='Enter singular Noun: ')
screen.create_window(88, 120, window=input3_text)

singular_input =  Entry(window)
screen.create_window(246, 120, window=singular_input)


def clear():
    color_input.delete(0, END)
    plural_input.delete(0, END)
    singular_input.delete(0, END)
    
    
def get_user_ans():
    user_ans = {'color': color_input.get(),
                'plural_noun': plural_input.get(),
                'singular_noun': singular_input.get()}
    
    if user_ans['color'] == '':
        user_ans['color'] = 'red'

    if user_ans['plural_noun'] == '':
        user_ans['plural_noun'] = 'violets'

    if user_ans['singular_noun'] == '':
        user_ans['singular_noun'] = 'you'

    output = Label(screen, text=f'Roses are {user_ans["color"]}'
                   f' \n {user_ans["plural_noun"]} are blue'
                   f' \n And I love {user_ans["singular_noun"]}.  ',
                   font=('Arial', 15))
    screen.create_window(200, 240, window=output)
    
    
button_show = Button(text='Show Mad Libs', command=get_user_ans)
screen.create_window(150, 170, window=button_show)

button_clear = Button(text='Clear', command=clear)
screen.create_window(250, 170, window=button_clear)

window.mainloop()
