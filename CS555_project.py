
# coding: utf-8

tags = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE','CHIL',
'DIV','DATE','HEAD','TRLR','NOTE']

def is_valid(line):
    tag = line.split(' ')[1].strip()
    if tag in tags:
        return tag
    elif line.split(' ')[2].strip() == 'INDI':
        return line.split(' ')[2].strip()
    else:
        return "Invalid tag"

with open('P01-My-Family-24-Jan-2016.ged','r') as data_ged:
    for row in data_ged:
        print row,"Level:",row[0],"\nTag:",is_valid(row)



