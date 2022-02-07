import pandas as pd
from datetime import date

column_names = ['First Name', 'Last Name', 'Office MLS ID', 'Office_Compare', 'Office E-mail']

excel_file_name = '' + '.xlsx'

df = pd.read_excel(excel_file_name, names = column_names)

unique_offices = set(df['Office MLS ID'])
office_list = list(df['Office MLS ID'])

date = date.today()
date = date.strftime("%B_%d_%Y")

office_admins_full = []

for unique_office in unique_offices:
    office_admins = []
    list_index = 0
    current_office = ''  
    for office in office_list:
        if office == unique_office:
            current_office = office
            first_name = df['First Name'][list_index]
            last_name = df['Last Name'][list_index]
            admin_full_name = first_name + ' ' + last_name
            office_admins.append(admin_full_name)           
            office_email = df['Office E-mail'][list_index]
        list_index = list_index + 1
    office_admins = str(office_admins).replace('[', '').replace(']', '').replace("'", '')
    office_admins_full.append([current_office, office_email, office_admins])
    
df = pd.DataFrame(office_admins_full, columns = ['Office MLS ID', 'Office E-mail','Office Admins'])            
df.to_excel('Office_Admins' + '_' + date + '.xlsx', index = False)

