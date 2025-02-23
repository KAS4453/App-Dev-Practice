from jinja2 import Template

jnanpith_data = [
    {"year": 1965, "awardees" : "G. Sankara Kurup", "language" : "Malayalam"},
    {"year": 1966, "awardees" : "Tarashankar Bandopadhyaya", "language" : "Bengali"},
    {"year": 1967, "awardees" : "Kuppali Venkatappagowda Puttappa", "language" : "Kannada"},
]

TEMPALATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="description" content="This page lists Jnanpith Awardees"/>
    <title>Jnanpith</title>
</head>
<body>
    <div id = "intro">
        <h1> Jnanpith </h1>
        Bharatiya Jnanpith is a literary organization based in Delhi. It also presents highest literary awards in India.
    </div>
    <div id = "main">
        <h1> Awardees </h1>
        <table>
            <thead>
                <tr>
                    <th> Year </th>
                    <th> Awardees </th>
                    <th> Language </th>
                </tr>
            </thead>
            <tbody>
                {% for janapith in janapith_data %}
                    <tr>
                        <td>{{ janapith["year"] }} </td>
                        <td>{{ janapith["awardees"] }} </td>
                        <td>{{ janapith["language"] }} </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

def main():
    template = Template(TEMPALATE)
    print(template.render(janapith_data=jnanpith_data))

    content = template.render(janapith_data=jnanpith_data)
    my_html_document_file = open('10. jnanpith_generated.html', "w")
    my_html_document_file.write(content)
    my_html_document_file.close()


if __name__ == "__main__":
    main()
