import pandas as pd

data = pd.read_excel('./Popular_Spotify_Songs.xlsx')

# Definimos condiciones
num_artistas = 2
anyo = 2019

# Creamos subsets
canciones_varios_artistas = data[data['artist_count'] >= num_artistas]
canciones_recientes = data[data['released_year'] >= anyo]

# Calculamos tamaños
num_canciones_varios_artistas = len(canciones_varios_artistas)
num_canciones_recientes = len(canciones_recientes)

# Calculamos intersección
interseccion = len(pd.merge(canciones_varios_artistas, canciones_recientes, how='inner', on=['track_name']))


print(f'Canciones con múltiples artistas: {num_canciones_varios_artistas}')
print(f'Canciones desde 2019: {num_canciones_recientes}')
print(f'Intersección: {interseccion}')