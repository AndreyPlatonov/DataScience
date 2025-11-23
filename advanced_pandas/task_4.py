import pandas as pd

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1', 
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

client_base_no_address = client_base[['client_id']]

clients_revenue_no_address = client_base_no_address.merge(rzd, on = 'client_id', how = 'left').merge(auto, on = 'client_id', how = 'left').merge(air, on = 'client_id', how = 'left')
clients_revenue = client_base.merge(rzd, on = 'client_id', how = 'left').merge(auto, on = 'client_id', how = 'left').merge(air, on = 'client_id', how = 'left')

print(f'таблица с тремя типами выручки для каждого client_id без указания адреса клиента: \n{clients_revenue_no_address.head(10)}\n')
print(f' таблица по типам выручки с указанием адреса клиента: \n{clients_revenue.head(10)}')
