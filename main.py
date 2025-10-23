from pyscript import display, document

def create_order(e):
    document.getElementById('output').innerHTML = ""

    total = 0

    if document.getElementById("Coffee_Cake").checked:
        total += int(document.getElementById("Coffee_Cake").value)

    if document.getElementById("Proformative_Matcha").checked:
        total += int(document.getElementById("Proformative_Matcha").value)

    if document.getElementById("Choclate_Goodness").checked:
        total += int(document.getElementById("Choclate_Goodness").value)

    if document.getElementById("bigBack_special").checked:
        total += int(document.getElementById("bigBack_special").value)

    if document.getElementById("Water_Type").checked:
        total += int(document.getElementById("Water_Type").value)

    if document.getElementById("Pasta_Yum").checked:
        total += int(document.getElementById("Pasta_Yum").value)

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    display(f"Order for: {name}", target="output")
    display(f"Address: {address}", target="output")
    display(f"Contact number: {contact}", target="output")
    display(f"Total: ₱{total:.2f}", target="output")
