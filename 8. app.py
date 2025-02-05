from jinja2 import Template

TEMPLATE = """
Hello {name}
This is {p:+} and this is {n:+}
This is in decimal={value:d} and this is in hexadecimal={value:x}"""

temp = """ Hello {{name}}"""

def main():
    print("hello world")
    print(TEMPLATE.format(name="KAS", p=5, n=-7, value = 32))

    template = Template(temp)
    print(template.render(name = "Arpit"))


if __name__ == "__main__":
    main()
