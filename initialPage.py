show_frame(page0)

pg0_button = Button(page0, text='USER', font=(
    'Arial', 20, 'bold'), command=lambda: show_frame(user_page_1))
pg0_button.place(x=100, y=90)

pg0_button = Button(page0, text='ADMIN', font=(
    'Arial', 20, 'bold'), command=lambda: show_frame(admin_page_1))
pg0_button.place(x=350, y=90)
