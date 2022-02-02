from implementation import *
import pandas as pd

def reader_fun(self):
    a = []

    with open('accounts.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                self.insertVertices("bank", a)
    with open('homes.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                a.append(row[4])
                self.insertVertices("home", a)
    with open('cars.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                self.insertVertices("car", a)
    with open('phones.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                self.insertVertices("phone", a)
    with open('people.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                a.append(row[4])
                a.append(row[5])

                self.insertVertices("person", a)
    with open('calls.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                a.append(row[4])
                self.insertEdge("call", a)
    with open('ownerships.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                a.append(row[4])
                self.insertEdge("ownership", a)
    with open('relationships.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                self.insertEdge("relation", a)
    with open('transactions.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a.clear()
            if line_count == 0:
                line_count += 1
                continue
            else:
                a.append(row[0])
                a.append(row[1])
                a.append(row[2])
                a.append(row[3])
                a.append(row[4])
                self.insertEdge("transaction", a)


def get_ssuspect(self):

    li=[]
    x={}

    for i in self.suspects:
        x[i]=self.this_Vertex.verteces[i]
        li.append([x[i].personal_code,x[i].name,x[i].last_name,x[i].Job])

    df = pd.DataFrame(li)

    return df
def df_faz1(self):
    return pd.read_csv("people.csv")