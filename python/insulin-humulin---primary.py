# Matthew J Carr, Alison K Wright, Lalantha Leelarantha, Hood Thabit, Nicola Milne, Naresh Kanumilli, Darren M Ashcroft, Martin K Rutter, 2024.

import sys, csv, re

codes = [{"code":"1616440000000000.0","system":"gprdproduct"},{"code":"725241000000000.0","system":"gprdproduct"},{"code":"719941000000000.0","system":"gprdproduct"},{"code":"720441000000000.0","system":"gprdproduct"},{"code":"724241000000000.0","system":"gprdproduct"},{"code":"1616140000000000.0","system":"gprdproduct"},{"code":"720141000000000.0","system":"gprdproduct"},{"code":"721141000000000.0","system":"gprdproduct"},{"code":"724141000000000.0","system":"gprdproduct"},{"code":"720041000000000.0","system":"gprdproduct"},{"code":"720241000000000.0","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-humulin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-humulin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-humulin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
