dinner_guests = ["socrates", "plato", "aristotle"]
print "This is an invitation to", dinner_guests[0].capitalize(), "- enjoy yourself"
print "Sending this to", dinner_guests[1].capitalize(), "- you are welcome too"
print "LAST MSG TO THE PARTY ANIMAL", dinner_guests[2].upper(), "- WOOOO"

print "Sadly", dinner_guests[2].capitalize(), "cannot make it"
dinner_guests[2] = "Yung Plebian"

print "New guest welcome:", dinner_guests[2]

dinner_guests.insert(0, "randomer")
dinner_guests.insert(2, "Bill Cosby")
dinner_guests.append("me")

print "First new guest:", dinner_guests[0]
print "Second new guest:", dinner_guests[2]
print "Last new guest:", dinner_guests[-1]

