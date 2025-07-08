import csv
with open('day.csv' , mode = 'r') as rf:
    csv_read = csv.DictReader(rf)
    #next(csv_read , None)
    with open('new2_csv' , mode = 'w') as wf:
        fieldnames = ['Numeric-2','Numeric-Suffix']
        csv_write = csv.DictWriter(wf , fieldnames=fieldnames, delimiter='\t')
        for rows in csv_read:
            print(rows)
            del rows ['Numeric']
            csv_write.writerow(rows)

# with open ('new_csv', mode = 'w' ) as wf :
#     csv_write = csv.writer(wf , delimiter='\t')
#     for rows in csv_read:
#         print(rows)
#         csv_write.writerow(rows)