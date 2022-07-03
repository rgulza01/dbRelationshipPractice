from app import db, Owner, Gadget

db.drop_all()
db.create_all()
owner1 = Owner(name = "Putuputu", address = "Via badia di cava")
owner2 = Owner(name = "Gulugulu", address = "Frank land")


gadget1 = Gadget(model = "Note 10 +", type = "phone", owner=owner1)
gadget2 = Gadget(model = "Galaxy z flip", type = "phone", owner=owner2)
gadget3 = Gadget(model = "Note pad", type = "tablet", owner=owner2)
db.session.add_all([owner1, owner2, gadget1, gadget2])
db.session.commit()
print("z3 flip owner: ", gadget2.owner)
print("Gulugulu gatgets: ")
for g in owner2.gadgets:
    print(g)