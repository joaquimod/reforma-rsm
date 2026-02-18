import pandas as pd

data = {
    'Codi': ['1.1', '1.2', '2.1', '3.1'],
    'Descripció': [
        'SATE aïllament exterior poliestirè 8cm gruix',
        'Finestra fusta amb vidre doble 4/12/4',
        'Paviment ceràmic en habitació de 5.2m2',
        'Aïllament de coberta amb llana de roca 10cm'
    ],
    'Amidament': [120, 15, 1, 85],
    'Unitat': ['m2', 'u', 'u', 'm2']
}

df = pd.DataFrame(data)
df.to_excel('docs/PB/SIMULACIO_ERRORS/Amidaments_SIM.xlsx', index=False)
