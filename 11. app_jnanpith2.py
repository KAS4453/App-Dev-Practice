from jinja2 import Template

jnanpith_data = [
    {"year": 1965, "awardees" : "G. Sankara Kurup", "language" : "Malayalam"},
    {"year": 1966, "awardees" : "Tarashankar Bandopadhyaya", "language" : "Bengali"},
    {"year": 1967, "awardees" : "Kuppali Venkatappagowda Puttappa", "language" : "Kannada"},
]
def main():
    # Read the template file content into a variable
    template_file = open("12. jnanpith_template.html.jinja2")
    TEMPLATE = template_file.read()
    template_file.close()

    # Render the template using Jinja2
    template = Template(TEMPLATE)
    content = template.render(janapith_data=jnanpith_data)

    # Save the rendered html document
    my_html_document_file = open('13. jnanpith_template_generated.html', "w")
    my_html_document_file.write(content)
    my_html_document_file.close()

if __name__ == "__main__":
    main()