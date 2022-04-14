import tkinter as tk
import globalClasses
import useHelperFunctions
import pageStructs.shipListPage as shipListPage

useHelperFunctions.loadShipData()

root = tk.Tk()
root.resizable(False, False)
root.title('Ostranouts Ship Manager')
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root)
frame_main.grid(sticky='news')

# header
header = tk.Label(frame_main,
                  text="Ostranouts Ship Manager",
                  fg="white",
                  bg="black",
                  width=25,
                  height=2
                  )
header.grid(row=1, column=0, pady=(0, 10), sticky='ew')

navigation_buttons_frame = tk.Frame(frame_main)
navigation_buttons_frame.grid(row=2, column=0, pady=(0, 10), sticky='ew')

# pages

page_wrapper = tk.Frame(frame_main)
page_wrapper.grid(row=3, column=0, pady=(0, 10), sticky='ew')

main_page = globalClasses.Page(page_wrapper)
ship_derelict_page = shipListPage.ShipListPage(
    page_wrapper, useHelperFunctions.loadShipData())
ship_derelict_page.show()
ship_police_page = shipListPage.ShipListPage(page_wrapper, [])
ship_scav_page = shipListPage.ShipListPage(page_wrapper, [])
ship_random_page = shipListPage.ShipListPage(page_wrapper, [])
ship_derelict_page.hide()
ship_police_page.hide()
ship_scav_page.hide()
ship_random_page.hide()

# navigation buttons

def togglePage(page):
    main_page.hide()
    ship_derelict_page.hide()
    ship_police_page.hide()
    ship_scav_page.hide()
    ship_random_page.hide()

    match page:
        case 'derelict':
            ship_derelict_page.show()
        case 'police':
            ship_police_page.show()
        case _:
            main_page.show()

mainPageBtn = tk.Button(navigation_buttons_frame,
                        text="Main Page", command=lambda: togglePage('main'))
derelictPageBtn = tk.Button(
    navigation_buttons_frame, text="Derelict Ships", command=lambda: togglePage('derelict'))
policePageBtn = tk.Button(navigation_buttons_frame,
                          text="Police Ships", command=lambda: togglePage('police'))
mainPageBtn.grid(row=0, column=0, sticky='ew')
derelictPageBtn.grid(row=0, column=1, sticky='ew')
policePageBtn.grid(row=0, column=2, sticky='ew')

# execute
root.mainloop()
