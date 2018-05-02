def chapter_6_1():
    """
    csv文件
    csv.reader / csv.writer
    csv.DictReader / csv.DictWriter
    """

    import csv
    from collections import namedtuple

    """
    读csv
    """

    def test1():
        with open("stocks.csv") as f:
            f_csv = csv.reader(f)
            header = next(f_csv)
            for row in f_csv:
                print(row)

    def test2():
        with open("stocks.csv") as f:
            f_csv = csv.reader(f)
            headings = next(f_csv)
            Row = namedtuple("Row", headings)
            for r in f_csv:
                row = Row(*r)
                print(row)

    def test3():
        with open("stocks.csv") as f:
            f_csv = csv.DictReader(f)
            for row in f_csv:
                print(row)

    """
    写csv文件
    """

    def test4():
        headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
        rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
                ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
                ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
                ]
        with open("output.csv", "w") as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)

    def test5():
        headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
        rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
                 'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
                {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
                 'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
                {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
                 'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
                ]
        with open("output.csv", "w") as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)


def chapter_6_2():
    """
    json数据
    json.dumps() / json.loads()
    """

    import json

    def test1():
        data = dict(name="ACME", shares=100, price=542.23)
        json_str = json.dumps(data)
        d = json.loads(json_str)

        with open("data.json", "w") as f:
            json.dump(data, f)

        with open("data.json", "r") as f:
            data = json.load(f)
