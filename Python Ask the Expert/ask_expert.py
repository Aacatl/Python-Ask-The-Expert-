from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital_data.txt', 'a') as file:
        for line in file:
            file.write('\n' + country_name + '/' + city_name)
            line = line.rstrip(\n)
            country, city = line.split('/')
            the_world[country] = city

print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()

the_world = {}

read_from_file()
while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer',
                            'The Capital city of' + query_country + 'is' + result + '!')

    else:
        new_city = simple.dialog('Teach me',
                                 'I don\'t know' +
                                 'what is the capital city of' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()
