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

def get_micro_1_dice():
    data_micro_1_dict = dict()
    title = "page"
    for i in range(6):
        temp_massive = []
        for j in range(6):
            record = dict()
            record["foo"] = fake.text(max_nb_chars=5)
            record["first"] = fake.text(max_nb_chars=5)
            record["name"] = fake.name()
            record["age"] = randint(1, 100)
            temp_massive.append(record)
        data_micro_1_dict[title + str(i)] = temp_massive
    return data_micro_1_dict

def get_micro_2_dice():
    data_micro_2_dict = dict()
    title = "page"
    for i in range(6):
        temp_massive = []
        for j in range(6):
            record = dict()
            record["bar"] = fake.text(max_nb_chars=5)
            record["second"] = fake.text(max_nb_chars=5)
            record["profession"] = fake.job()
            record["company"] = fake.company()
            temp_massive.append(record)
        data_micro_2_dict[title + str(i)] = temp_massive
    return data_micro_2_dict


def write_documents_to_file(name, dict_file):
    with open(name, 'w') as f:
        json.dump(dict_file, f, ensure_ascii=False, indent=4)


def print_dict_in_json_format(data):
    pprint.pprint(data)

if __name__ == '__main__':
    data_doc = get_documents_dict(10)
    data_printer = get_printers_dict(10)
    data_micro_1 = get_micro_1_dice()
    data_micro_2 = get_micro_2_dice()
    #print_dict_in_json_format(data)
    write_documents_to_file("./document_api/documents.json", data_doc)
    write_documents_to_file("./printer_api/printers.json", data_printer)
    write_documents_to_file("./micro_1_api/micro1.json", data_micro_1)
    write_documents_to_file("./micro_2_api/micro2.json", data_micro_2)

""""
from random import randint
d = {
    "page0": [
        {
            "foo": "What.",
            "first": "Put.",
            "name": "Aaron Tran",
            "age": 38
        },
        {
            "foo": "For.",
            "first": "Week.",
            "name": "Shari Reynolds",
            "age": 26
        },
        {
            "foo": "Idea.",
            "first": "Know.",
            "name": "Andrea Robertson",
            "age": 53
        },
        {
            "foo": "May.",
            "first": "West.",
            "name": "Corey Gilbert",
            "age": 48
        },
        {
            "foo": "Life.",
            "first": "TV.",
            "name": "William Blackburn",
            "age": 42
        }
    ],
    "page1": [
        {
            "foo": "Nor.",
            "first": "Add.",
            "name": "Deborah Reilly",
            "age": 23
        },
        {
            "foo": "We.",
            "first": "Hard.",
            "name": "Kimberly Lawrence",
            "age": 94
        },
        {
            "foo": "Here.",
            "first": "Car.",
            "name": "Barbara Parker",
            "age": 28
        },
        {
            "foo": "Deep.",
            "first": "Guy.",
            "name": "Kevin Ochoa",
            "age": 55
        },
        {
            "foo": "Page.",
            "first": "Sign.",
            "name": "Jonathan Adams",
            "age": 25
        }
    ],
    "page2": [
        {
            "foo": "Oil.",
            "first": "Nor.",
            "name": "Jason Clark",
            "age": 96
        },
        {
            "foo": "Easy.",
            "first": "Box.",
            "name": "Carl Cox",
            "age": 53
        },
        {
            "foo": "Lay.",
            "first": "Save.",
            "name": "Lori Mahoney",
            "age": 66
        },
        {
            "foo": "Film.",
            "first": "Loss.",
            "name": "William Compton",
            "age": 49
        },
        {
            "foo": "Next.",
            "first": "Wife.",
            "name": "Laurie Brown",
            "age": 23
        }
    ],
    "page3": [
        {
            "foo": "Base.",
            "first": "Bank.",
            "name": "Michael Garcia",
            "age": 37
        },
        {
            "foo": "Bit.",
            "first": "Gas.",
            "name": "Bradley Hanson",
            "age": 12
        },
        {
            "foo": "Ever.",
            "first": "Son.",
            "name": "Ryan Cox",
            "age": 2
        },
        {
            "foo": "Edge.",
            "first": "Ever.",
            "name": "Geoffrey Rivers",
            "age": 12
        },
        {
            "foo": "Plan.",
            "first": "Eye.",
            "name": "Bruce Harrington",
            "age": 84
        }
    ],
    "page4": [
        {
            "foo": "Huge.",
            "first": "It.",
            "name": "Clinton Ward",
            "age": 35
        },
        {
            "foo": "Rise.",
            "first": "Blue.",
            "name": "Lindsay Thomas",
            "age": 94
        },
        {
            "foo": "Well.",
            "first": "Fish.",
            "name": "Tyler Reynolds DVM",
            "age": 42
        },
        {
            "foo": "Soon.",
            "first": "Well.",
            "name": "Christopher Gutierrez",
            "age": 31
        },
        {
            "foo": "Seat.",
            "first": "Time.",
            "name": "Dalton Salazar",
            "age": 89
        }
    ]
}
new_key = "page"+str(randint(0, 4))
keys = ['foo', 'first']
new_dict = dict()
for i in keys:
    new_dict[i] = d[new_key][randint(0,4)].get(i)
print(new_dict)
print([d[new_key][randint(0,4)].get(key) for key in keys])
"""