from setup import field_optns

print ('Available properties are:')

for field in field_optns:
    print(field)

while True:
    user_properties = input('Please specify the desired properties ' \
    'separated by commas (eg. density, band_gap): ').split(',')
    properties = [prop.strip() for prop in user_properties]

    if all(prop in field_optns for prop in properties):
        for prop in properties:
            if (prop == 'density'):
                d_min = float(input('Minimum density (g/cm^-3):' ))
                d_max = float(input('Maximum density (g/cm^-3):' ))
            elif (prop == 'bulk_modulus'):
                bm_min = float(input('Minimum bulk modulus (GPa): '))
                bm_max = float(input('Maximum bulk modulus (GPa): '))
            elif (prop == 'shear_modulus'):
                sm_min = float(input('Minimum shear modulus (GPa): '))
                sm_max = float(input('Maximum shear modulus (GPa): '))
            elif (prop == 'homogeneous_poisson'):
                hp_min = float(input('Minimum poisson: '))
                hp_max = float(input('Maximum poisson: '))
            elif (prop == 'band_gap'):
                bg_min = float(input('Minimum band gap (eV): '))
                bg_max = float(input('Maximum band gap (eV): '))
            elif (prop == 'is_magnetic'):
                mag = input('Does material need to be magnetic (Yes, No): ')
            elif (prop == 'is_stable'):
                stb = input('Does material need to be stable (Yes, No): ')
        break
    else:
        print('Invalid properties entered, please try again. ' \
        'Remember to separate with commas and include underscores.')
    

#Use user input to sort through available materials
import pandas as pd
from setup import df

#With a for loop
for prop in properties:
    if (prop == 'density'):
        user_d = ((d_max >= df['density']) & (df['density'] >= d_min))
        df = df[user_d]
    elif (prop == 'bulk_modulus'):
        user_bm = df[(df['voigt_bulk'] <= bm_max) & (df['reuss_bulk'] >= bm_min)]
        df = df[user_bm]
    elif (prop == 'shear_modulus'):
        user_sm = ((sm_max >= df['shear_modulus']) & (df['shear_modulus'] >= sm_min))
        df = df[user_sm]
    elif (prop == 'homogeneous_poisson'):
          user_hp = ((hp_max >= df['homogeneous_poisson']) & 
                     (df['homogeneous_poisson'] >= hp_min))
          df = df[user_hp]
    elif (prop == 'band_gap'):
         user_bg = ((bg_max >= df['band_gap']) & (df['band_gap'] >= bg_min))
         df = df[user_bg]
    elif (prop == 'is_magnetic'):
        if (mag.lower() == 'yes'):
            user_mag = (df['is_magnetic'] == True)
        else:
            user_mag = (df['is_magnetic'] == False)
    elif (prop == 'is_stable'):
        if (stb.lower() == 'yes'):
            user_stb = (df['is_stable'] == True)
        else:
            user_stb = (df['is_stable'] == False)
        df = df[user_stb]

print(f'{len(df)} materials found.')

#Ask user which property to sort results by
while True:
    user_sort = input ('Sort results by (One property only): ')
    user_order = input('In ascending order? (Yes/No): ')
    if user_sort in properties:
        df = df.sort_values(by= user_sort,
                            ascending = (user_order.lower() == 'yes'))
        break
    else:
        print('Invalid property entered, please try again.')


#Print results

pd.set_option('display.max_columns', None)

while True:
    display_rows = int(input('How many rows of the results would you like to see? '))
    if (display_rows <= len(df)) & (display_rows > 0):
        print(df.head(display_rows))
        break
    else:
        print ('Too many/few rows requested, please try again.')

