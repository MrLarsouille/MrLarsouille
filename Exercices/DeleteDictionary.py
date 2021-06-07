contacts = {"Pila": "01217000111", \
            "Piou": "01234000111", \
            "Adrien":"01217000222", "Jackie":"01227000123"}
 
print ("Contacts: ", contacts)
 
print ("\n")
print ("Delete key = 'Pila' ")
 
del contacts["Pila"]
 
 
print ("Contacts (After delete): ", contacts)
 
print ("\n")
print ("Delete key = 'Piou' ")
 
contacts.__delitem__( "Piou")
 
 
print ("Contacts (After delete): ", contacts)
 
 
print ("Clear all element")
 
contacts.clear()
 
print ("Contacts (After clear): ", contacts)
 
del contacts
 
print ("Contacts (After delete): ", contacts)