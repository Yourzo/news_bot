import csv  # !not need to run this ever again


def create_csv_file():
    fields = ['row', 'last message']
    row = [0, 0]
    file_name = 'none'

    with open(file_name, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerow(row)


if __name__ == '__main__':
    create_csv_file()
