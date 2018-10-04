from pprint import pprint

import csv


class process_data():
    def import_tsv(self, filepath):
        pprint('Filepath: ' + filepath)

        line_count = 0

        with open(filepath, 'rb') as csvfile:
            # pprint(csvfile.read(1024))
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)

            reader = csv.DictReader(csvfile, dialect=dialect)

            for row in reader:
                if line_count > 10:
                    break

                pprint(row)

                line_count += 1

        pprint('Processed {} records'.format(line_count))
