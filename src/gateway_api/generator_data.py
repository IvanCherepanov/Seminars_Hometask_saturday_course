from faker import Faker
from random import randint
import json
import pprint

fake = Faker('en_US')


def get_documents_dict(n):
    data_documents = dict()
    title = "page"
    for i in range(n):
        page_massive = []
        for j in range(randint(10, 20)):
            record = dict()
            record["document_uuid"] = fake.aba()
            record["document_name"] = fake.text(max_nb_chars=20)
            record["document_created"] = fake.iso8601()
            record["document_edited"] = fake.iso8601()
            page_massive.append(record)
        data_documents[title + str(i)] = page_massive
    return data_documents

def get_printers_dict(n):
    data_documents = dict()
    title = "page"
    for i in range(n):
        page_massive = []
        for j in range(randint(10, 20)):
            record = dict()
            record["printer_uuid"] = fake.aba()
            record["printer_name"] = fake.text(max_nb_chars=20)
            record["printer_type"] = fake.text(max_nb_chars=5)
            record["printer_address"] = fake.address()
            page_massive.append(record)
        data_documents[title + str(i)] = page_massive
    return data_documents

def write_documents_to_file(name, dict_file):
    with open(name, 'w') as f:
        json.dump(dict_file, f, ensure_ascii=False, indent=4)


def print_dict_in_json_format(data):
    pprint.pprint(data)

if __name__ == '__main__':
    data_doc = get_documents_dict(10)
    data_printer = get_printers_dict(10)
    #print_dict_in_json_format(data)
    write_documents_to_file("./document_api/documents.json", data_doc)
    write_documents_to_file("./printer_api/printers.json", data_printer)
