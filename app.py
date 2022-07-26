import func
# add a record to the customers table in customer db
# func.add_one('khalid', 'yakub', 'adetola@outlook.com')

# add many record to the customers table in customer db
stuff = [
    ('harry', 'porter', 'harryporter@yahoo.com'), 
    ('jon', 'snow', 'jonsnow@gmail.com')
]

func.add_many(stuff)

# delete record use rowid as string
# func.delete_one('8')

# show all the records
func.show_all()
