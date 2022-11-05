import pandas as pd

# path_pre = '/Users/jonahbuckingham-cain/PycharmProjects/pythonProject/venv/static/'
path_pre = 'venv/staic/'
path_nonpilot = path_pre + 'NONPILOT.txt'
path_pilot = path_pre + 'PILOT.txt'
pilot_count = path_pre +'pilot_count.csv'

def parc_txt(path):
    width_record = [8, 2, 30, 30, 33, 33, 17, 2, 10, 18, 2, 1, 6, 6, 922]
    columns_record = ['UNIQUE ID', 'RECORD TYPE', 'FIRST & MIDDLE NAME', 'LAST NAME & SUFFIX', 'STREET 1', 'STREET 2',
                      'CITY',
                      'STATE', 'ZIP CODE', 'COUNTRY-NAME', 'REGION', 'MEDICAL CLASS', 'MEDICAL DATE',
                      'MEDICAL EXPIRE DATE', 'FILLER']
    df = pd.read_fwf(path, names=columns_record, widths=width_record)
    df_pilot_record = df.loc[df['RECORD TYPE'] == 0].reset_index(drop=True)

    width_cert = [8, 2, 1, 1, 8, 110, 990]
    columns_cert = ['UNIQUE ID', 'RECORD TYPE', 'CERTIFICATE TYPE', 'CERTIFICATE LEVEL',
                    'CERTIFICATE EXPIRE DATE', 'RATINGS', 'TYPE RATINGS']

    df = pd.read_fwf(path, names=columns_cert, widths=width_cert)
    df_cert = df.loc[~(df['RECORD TYPE'] == 0)].reset_index(drop=True)
    return (df_pilot_record, df_cert)


df_contact_pilot, df_cert_pilot = parc_txt(path_pilot)
# df_contact_nonpilot, df_cert_nonpilot = parc_txt(path_nonpilot)

df_clean = df_cert_pilot.dropna(subset=['RATINGS'])
df_tr = df_clean.loc[df_clean['RATINGS'].str.contains('UAS')].reset_index(drop=True)
drone_pilots = df_tr['UNIQUE ID'].to_list()
df_drone_pilots = df_contact_pilot.loc[df_contact_pilot['UNIQUE ID'].isin(drone_pilots)].reset_index(drop=True)
df_drone_pilots['zip'] = df_drone_pilots['ZIP CODE'].str.split('-', expand=True)[0]
df_zip = df_drone_pilots.groupby(['zip']).count().reset_index()
df_zip['count'] = df_zip['UNIQUE ID']
df_zip.drop(df_zip.columns.difference(['zip', 'count']), 1, inplace=True)

# ten_miles = [95403, 95439, 95401, 95492, 95402, 95406, 95405, 95404, 95407, 95444, 95473, 95436, 95409, 95472]
# ten_miles_gen = ['94515', '94928', '94931', '94951', '95401', '95402', '95403', '95404', '95405', '95406', '95407', '95409', '95439', '95444', '95448', '95472', '95492']
# ten_miles_gen2 = [95401,95403,95404,95405,95407,95436,95439,95444,95448,95471,95472,95492]
# twenty_miles = [95403, 95439, 95401, 95492, 95402, 95406, 95405, 95404, 95407, 95444, 95473, 95436, 95409, 95472, 95448,
#                 94928, 94515, 95471, 95419, 94926, 94927, 94931, 95452, 95446, 94951, 95462, 94576, 95486, 95442, 94922,
#                 94972, 95465, 95431, 95430, 94508, 94573, 95441, 94923, 94574, 95416, 94955, 94975, 94562, 94953, 94999,
#                 94971, 95433]

df_zip.to_csv(path_or_buf=pilot_count, index=False)

