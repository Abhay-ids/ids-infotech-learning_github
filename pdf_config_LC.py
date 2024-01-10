import re
import json
import fitz  # PyMuPDF

def extract_data_from_pdf(pdf_text, config):
    data_entries = []

    
    for section_config in config["applicableFor"]["sections"]:
        
        if section_config["title"] == "Applications":
            section_data = {"title": section_config["title"], "trademarks": []}

            registration_pattern = re.compile(section_config["trademarks"]["applicationNumber"])
            for match in registration_pattern.finditer(pdf_text):
                applicationNumber = match.group(1).replace('\n', '')

                application_date = re.compile(section_config["trademarks"]["applicationDate"])
                application_date_search = application_date.search(pdf_text[match.end():])
                application_date = application_date_search.group(1).replace('\n', '') if application_date_search else "NULL"

                onwers_name = re.compile(section_config["trademarks"]["owners"]["name"])
                onwers_name_search = onwers_name.search(pdf_text[match.end():])
                onwers_name =  onwers_name_search.group(2).replace('\n', '') if  onwers_name_search else "NULL"
                
                onwers_address = re.compile(section_config["trademarks"]["owners"]["address"])
                onwers_address_search = onwers_address.search(pdf_text[match.end():])
                onwers_address =  onwers_address_search.group(2).replace('\n', '') if  onwers_name_search else "NULL"
                
                onwers_country = re.compile(section_config["trademarks"]["owners"]["country"])
                onwers_country_search = onwers_country.search(pdf_text[match.end():])
                onwers_country =  onwers_country_search.group(1).replace('\n', '') if  onwers_name_search else "NULL"

                verbal_elements = re.compile(section_config["trademarks"]["verbalElements"])
                verbal_elements_search = verbal_elements.search(pdf_text[match.end():])
                verbal_elements =  verbal_elements_search.group(1).replace('\n', '') if  verbal_elements_search else "NULL"

                representatives_name = re.compile(section_config["trademarks"]["representatives"]["name"])
                representatives_name_search = representatives_name.search(pdf_text[match.end():])
                representatives_name =  representatives_name_search.group(1).replace('\n', '') if  representatives_name_search else "NULL"
                
                representatives_address = re.compile(section_config["trademarks"]["representatives"]["address"])
                representatives_address_search = representatives_address.search(pdf_text[match.end():])
                representatives_address =  representatives_address_search.group(2).replace('\n', '') if  representatives_name_search else "NULL"
                
                representatives_country = re.compile(section_config["trademarks"]["representatives"]["country"])
                representatives_country_search = representatives_country.search(pdf_text[match.end():])
                representatives_country =  representatives_country_search.group(1).replace('\n', '') if  representatives_name_search else "NULL"

                goods = re.compile(section_config["trademarks"]["classifications"]["goodServiceDescription"])
                goods_search =  goods.search(pdf_text[match.end():])
                goods =  goods_search.group(2).replace('\n','') if  goods_search else "NULL"
                                
                pattern = re.compile(r"\d+", re.MULTILINE)
                matches = pattern.findall(goods)
                
                priorities_number = re.compile(section_config["trademarks"]["priorities"]["number"])
                priorities_number_search =  priorities_number.search(pdf_text[match.end():])
                priorities_number =  priorities_number_search.group(3).replace('A',"").replace('\n','') if priorities_number_search else "NULL"
                
                priorities_date = re.compile(section_config["trademarks"]["priorities"]["date"])
                priorities_date_search =  priorities_date.search(pdf_text[match.end():])
                priorities_date =  priorities_date_search.group(1).replace('\n',"") if priorities_date_search else "NULL"

                priorities_country = re.compile(section_config["trademarks"]["priorities"]["country"])
                priorities_country_search =  priorities_country.search(pdf_text[match.end():])
                priorities_country =  priorities_country_search.group(2).replace('\n',"") if priorities_country_search else "NULL"

                
            

                section_data["trademarks"].append({
                    "applicationNumber": applicationNumber,
                    "applicationDate": application_date,
                    "owners": {
                        "name": onwers_name,
                        "address": onwers_address,
                        "country": onwers_country
                    },
                    "verbalElements": verbal_elements,
                    "deviceMarks": "",
                    "colors": "",
                    "representatives": {
                        "name": representatives_name,
                        "address": representatives_address,
                        "country": representatives_country
                    },
                    "classifications": {
                        "niceClass": matches[:],
                        "goodServiceDescription": goods
                    },
                    "Disclaimer": "",
                    "priorities": {
                        "number": priorities_number,
                        "date": priorities_date,
                        "country": priorities_country
                    }
                })
                
            data_entries.append(section_data)

    return data_entries


def save_text_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

# Load PDF text (replace 'your_pdf_path.pdf' with the actual path)
with fitz.open(r"LC\LC20231016-42.pdf") as pdf_document:
    pdf_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        pdf_text += page.get_text()

# Load configuration JSON
with open(r"LC-2015-2023.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file,)

# Extract data from PDF
result = extract_data_from_pdf(pdf_text, config)

# Save data to a JSON file
with open("LC\LC20231016-42.json", "w",  encoding="utf-8") as output_file:
    json.dump(result, output_file, indent=4, ensure_ascii=False)

# Save PDF text to a text file
save_text_to_file(pdf_text, "output_LC.txt")

# Display the result
print("Data extracted and saved to extracted_data.json")
