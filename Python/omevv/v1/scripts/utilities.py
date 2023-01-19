import csv

class Utilities:
    def __init__(self):
        pass

    def write_to_csv(self, data, file):
        fh = open(file, 'w', newline='')
        csv_writer = csv.writer(fh)
        count = 0
        for row in data:
            if count == 0:
                header = row.keys()
                csv_writer.writerow(header)
                count += 1

            csv_writer.writerow(row.values())
        fh.close()
