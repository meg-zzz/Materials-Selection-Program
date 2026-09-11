from setup import field_optns

print ('Available properties are:')

for field in field_optns:
    print(field)

while True:
    user_properties = input('Please specify the desired properties separated by commas (eg. density, band_gap): ').split(',')
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
        break
    else:
        print('Invalid properties entered, please try again. Remember to separate with commas and include underscores.')
    

#Use user input to sort through available materials
import pandas as pd
from setup import df

#With a for loop
for prop in properties:
    if (prop == 'density'):
        df['full_density']= df['density'].notna()
        user_d = ((d_max >= df['full_density']) & (df['full_density'] >= d_min))
    elif (prop == 'bulk_modulus'):
        df['full_voigtbm']= df['voight_bulk'].notna()
        df['full_reussbm']= df['reuss_bulk'].notna()
        df['full_vrhbm']= df['vrh_bulk'].notna()
        user_bm = df[(df['full_voigtbm'] <= bm_max) & (df['full_reuss'] >= bm_min)]
    elif (prop == 'shear_modulus'):
        df['full_shear'] = df['shear_modulus'].notna()
        user_sm = ((sm_max >= df['full_shear']) & (df['full_shear'] >= sm_min))
    elif (prop == 'homogeneous_poisson'):
          df['full_hp'] = df['homogeneous_poisson'].notna()
          user_hp = ((hp_max >= df['full_hp']) & (df['full_hp'] >= hp_min))
    elif (prop == 'band_gap'):
         df['full_bg'] = df['band_gap'].notna()
         user_bg = ((bg_max >= df['full_bg']) & (df['full_bg'] >= bg_min))
    elif (prop == 'is_magnetic'):
        if (mag == 'yes' | 'Yes'):
            user_mag = (df['is_magnetic' == 'True'])
        else:
            user_mag = (df['is_magnetic'] == 'False')

print(df)