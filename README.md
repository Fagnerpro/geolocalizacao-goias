# Geolocalização de Endereços - Goiás

Este projeto é um protótipo desenvolvido em **Python com Streamlit** para geocodificação de endereços urbanos no estado de Goiás, considerando elementos regionais como **quadra** e **lote**, pouco compatíveis com serviços globais de mapas.

## 🚀 Funcionalidades

- Upload de arquivos `.csv` com endereços personalizados
- Formatação inteligente do endereço para geocodificação
- Geolocalização via OpenStreetMap (Nominatim)
- Visualização interativa no mapa com Folium
- Exportação dos resultados com latitude e longitude

## 📁 Estrutura esperada do CSV

Seu arquivo deve conter colunas com os seguintes nomes:

| Campo         | Obrigatório | Exemplo                  |
|---------------|-------------|---------------------------|
| logradouro    | Não         | Rua 7                    |
| numero        | Não         | 123                      |
| bairro        | Sim         | Setor Bueno              |
| quadra        | Não         | 15                       |
| lote          | Não         | 12                       |
| cidade        | Sim         | Goiânia                  |
| estado        | Sim         | GO                       |
| cep           | Não         | 74000-000                |

---

## ▶️ Como executar localmente

```bash
# Clone o repositório
git clone https://github.com/Fagnerpro/geolocalizacao-goias.git
cd geolocalizacao-goias

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
streamlit run app/geolocalizacao_streamlit.py
```

---

## 📌 Tecnologias utilizadas

- [Streamlit](https://streamlit.io)
- [Pandas](https://pandas.pydata.org)
- [Geopy (Nominatim)](https://geopy.readthedocs.io/)
- [Folium](https://python-visualization.github.io/folium/)
- [streamlit-folium](https://github.com/randyzwitch/streamlit-folium)

---

## 🗺️ Visualização

Após o processamento, os endereços com coordenadas válidas serão exibidos em um **mapa interativo**. Você também poderá fazer o **download do resultado em CSV**.

---

## 📥 Exemplo de CSV

Veja o arquivo `data/exemplo_enderecos.csv` incluído no repositório como modelo.

---

## 📄 Licença

Este projeto é de uso acadêmico e institucional. Adaptável para outras regiões e aplicações.