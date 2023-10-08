import pandas as pd

cols = ['OFFENCE_FINYEAR','OFFENCE_MONTH','OFFENCE_CODE','OFFENCE_DESC','LEGISLATION',
        'FACE_VALUE', 'LOCATION_DETAILS', 'SPEED_BAND', 'SPEED_IND', 'SPEED_CAMERA_IND',
        'SEATBELT_IND', 'MOBILE_PHONE_IND', 'PARKING_IND', 'TOTAL_NUMBER', 'TOTAL_VALUE']

filename = r".\penalty_data_set_2.csv"

pd.read_csv(filename, usecols=cols).to_csv(r".\penalty_data_set.csv", index=False)