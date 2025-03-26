# geolocalizacao_streamlit.py

# geolocalizacao_streamlit.py

import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("Geolocalização de Endereços com Quadra e Lote - Goiás")

st.markdown("""
Este aplicativo permite importar um arquivo `.csv` com dados de endereços urbanos do estado de Goiás (com campos como quadra, lote, bairro e cidade), e realiza a geocodificação automática com base na formatação regional para visualização no mapa.

**Campos obrigatórios no CSV:** `logradouro`, `numero`, `bairro`, `quadra`, `lote`, `cidade`, `estado`, `cep`
""")

uploaded_file = st.file_uploader("Faça upload do arquivo CSV com os endereços:", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    def formatar_endereco(row):
        if pd.notnull(row['logradouro']) and pd.notnull(row['numero']):
            return f"{row['logradouro']}, {row['numero']}, {row['bairro']}, {row['cidade']} - {row['estado']}, Brasil"
        elif pd.notnull(row['quadra']) and pd.notnull(row['lote']):
            return f"Quadra {row['quadra']} Lote {row['lote']}, {row['bairro']}, {row['cidade']} - {row['estado']}, Brasil"
        else:
            return f"{row['bairro']}, {row['cidade']} - {row['estado']}, Brasil"

    df['endereco_formatado'] = df.apply(formatar_endereco, axis=1)

    st.subheader("Pré-visualização dos dados formatados")
    st.dataframe(df[['logradouro', 'quadra', 'lote', 'bairro', 'cidade', 'endereco_formatado']])

    geolocator = Nominatim(user_agent="geo_app")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    with st.spinner("Geocodificando endereços..."):
        df['localizacao'] = df['endereco_formatado'].apply(geocode)
        df['latitude'] = df['localizacao'].apply(lambda loc: loc.latitude if loc else None)
        df['longitude'] = df['localizacao'].apply(lambda loc: loc.longitude if loc else None)

    st.success("Geocodificação concluída.")

    st.subheader("Visualização no mapa")
    mapa = folium.Map(location=[-16.67, -49.25], zoom_start=7)

    for _, row in df.dropna(subset=['latitude', 'longitude']).iterrows():
        popup_text = f"{row['endereco_formatado']}"
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=popup_text,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(mapa)

    st_folium(mapa, width=1200, height=600, key="mapa")

    st.subheader("Download do arquivo geocodificado")
    df.to_csv("enderecos_geocodificados.csv", index=False)
    st.download_button("📥 Baixar CSV com coordenadas", "enderecos_geocodificados.csv")
