import xml.etree.ElementTree as ET

def read_products(filename: str):
    """
    Read products from XML file and print their names with quantities
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    print("Products list:")
    for product in root.findall("product"):
        name = product.find("name").text
        quantity = product.find("quantity").text
        print(f"{name} — {quantity}")


def update_quantity(filename: str, product_name: str, new_quantity: int):
    """
    Update the quantity of a specific product
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    for product in root.findall("product"):
        name = product.find("name").text
        if name == product_name:
            product.find("quantity").text = str(new_quantity)
            break

    tree.write(filename, encoding="utf-8", xml_declaration=True)


xml_file = "products.xml"

read_products(xml_file)

update_quantity(xml_file, "Молоко", 75)

print("\nAfter update:")
read_products(xml_file)
