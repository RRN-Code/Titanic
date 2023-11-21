import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title='Titanic', page_icon="🚢", layout='wide')


def load_lottieurl(url: str):
    r = requests.get(url)
    # if r.status_code != 200:
    #     return none
    return r.json()


# Load Animation
with st.container():
    # JSON url
    lottie_hello = load_lottieurl("https://lottie.host/f6d3da52-01de-4d68-8530-6fb2e20e059c/rXY2oOUuo7.json")
    st_lottie(lottie_hello, key='hello', speed=1, width=450, height=450)

st.title('Titanic Dataset Analysis')

st.markdown('---')

# Load Data
with st.container():
    # Load data
    @st.cache_data
    def carregar_dados():
        tit = pd.read_csv('titanic_data.csv', sep=',')
        return tit

    tit = carregar_dados()

with st.container():
    st.subheader('1 - Efetuar a leitura do dataset através do Pandas, gerando um DataFrame de nome tit, levando-se em consideração que o arquivo encontra-se na mesma pasta do notebook.')
    st.code("tit = pd.read_csv(titanic_data.csv)")
    st.write(tit.head(3))
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Conhecendo o Dataset")
    with col2:
        # JSON url
        lottie_start = load_lottieurl("https://lottie.host/62af8624-441a-4f12-9d47-1cc595d93619/quGbKnxaJW.json")
        st_lottie(lottie_start, key='start', speed=1, width=350, height=350)

with st.container():
    st.subheader('2 - Quantas linhas e colunas tem o dataset? Quais os tipos das colunas?')
    st.code("tit.shape")
    st.write(f"Linhas: {tit.shape[0]}")
    st.write(f"Colunas: {tit.shape[1]}")
    st.write(tit.dtypes)
    st.markdown("")
    st.subheader('3 - Mostre os dados dos dez primeiros e 8 últimos registros do dataset.')
    st.code("tit.head(10)")
    st.code("tit.tail(8)")
    st.write(tit.head(10))
    st.write(tit.tail(8))
    st.markdown("")
    st.subheader('4 - Cálculos envolvendo colunas numéricas com dados faltantes podem sofrer impacto. É possível afirmar se há dados faltantes no dataset? Caso positivo, quais e quantos seriam esses dados? Preencha os dados faltantes de forma que não influenciem em operações futuras.')
    st.code("tit.isnull().sum()")
    st.write(tit.isnull().sum())
    mean_age = tit['Age'].mean()
    st.write(f'Idade média: {mean_age:.2f}')
    mode_cabin = tit['Cabin'].mode()
    st.write(f'Cabine comum: {mode_cabin[0][0:3]}')
    mode_embark = tit['Embarked'].mode()
    st.write(f'Porto de Embarque mais comum: {mode_embark[0]}')
    st.code("tit['Age'] = tit['Age'].fillna(30)")
    st.code("tit['Cabin'] = tit['Cabin'].fillna(method='ffill')")
    st.code("tit['Cabin'] = tit['Cabin'].fillna('B96')")
    st.code("tit['Embarked'] = tit['Embarked'].fillna('S')")
    tit['Age'] = tit['Age'].fillna(30)
    tit['Cabin'] = tit['Cabin'].fillna(method='ffill')
    tit['Cabin'] = tit['Cabin'].fillna('B96')
    tit['Embarked'] = tit['Embarked'].fillna('S')
    st.write(tit.isnull().sum())
    st.markdown("")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Adequando o Dataset")
    with col4:
        # JSON url
        lottie_fix = load_lottieurl("https://lottie.host/e02985e5-ad7e-4076-9a80-750c03aca8bf/nTFsSqz96K.json")
        st_lottie(lottie_fix, key='fix', speed=1, width=350, height=350)

with st.container():
    st.subheader("5 - Uma vez que algumas colunas não serão utilizadas, eventualmente é melhor excluí-las para que não interfiram na análise. Assim, exclua do dataset as colunas Sibsp, Parch e Ticket.")
    st.code("tit = tit.drop(['SibSp', 'Parch', 'Ticket'], axis=1)")
    tit = tit.drop(['SibSp', 'Parch', 'Ticket'], axis=1)
    st.write(tit.head())
    st.subheader("6 - Renomear as colunas restantes para a lingua portuguesa, utilizando os seguintes nomes de colunas: IdPassageiro, Sobreviveu, Classe, Nome, Sexo, Idade, Tarifa, Cabine e Embarque.")
    st.code("old_names = tit.columns.tolist()")
    old_names = tit.columns.tolist()
    st.write(old_names)
    new_names = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'Tarifa', 'Cabine', 'Embarque']
    st.code("new_names = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'Tarifa', 'Cabine', 'Embarque']")
    st.write(new_names)
    tit_dict = dict(zip(old_names, new_names))
    st.code("tit_dict = dict(zip(old_names, new_names))")
    st.write(tit_dict)
    tit = tit.rename(columns=tit_dict)
    st.code("tit = tit.rename(columns = tit_dict)")
    st.write(tit.head())
    st.markdown("")
    st.subheader("7 - Alterar o conteudo da coluna Sobreviveu para: 0 => Não 1 => Sim")
    tit['Sobreviveu'] = tit['Sobreviveu'].replace(0, 'Não')
    tit['Sobreviveu'] = tit['Sobreviveu'].replace(1, 'Sim')
    st.code("tit['Sobreviveu'] = tit['Sobreviveu'].replace(0, 'Não')")
    st.code("tit['Sobreviveu'] = tit['Sobreviveu'].replace(1, 'Sim')")
    st.write(tit.head())
    st.markdown("")
    st.subheader("8 - Alterar o conteudo da coluna Sexo para: female => Mulher male => Homem")
    tit['Sexo'] = tit['Sexo'].replace('female', 'Mulher')
    tit['Sexo'] = tit['Sexo'].replace('male', 'Homem')
    st.code("tit['Sexo'] = tit['Sexo'].replace('female', 'Mulher')")
    st.code("tit['Sexo'] = tit['Sexo'].replace('male', 'Homem')")
    selected_sexo = st.selectbox("Qual sexo você gostaria de selecionar?",
                 pd.Series(tit['Sexo'].unique()).sort_values(ascending=True).tolist())
    st.write(tit[tit['Sexo'] == selected_sexo].head())
    st.markdown("")


col5, col6 = st.columns(2)
with col5:
    st.subheader("Alguns números")
with col6:
    # JSON url
    lottie_number = load_lottieurl("https://lottie.host/a3e888ee-29b9-4d56-af56-c0d11e4de5f3/5ufDkO1GkY.json")
    st_lottie(lottie_number, key='number', speed=0.1, width=350, height=350)

with st.container():
    st.subheader("9 - Quantas mulheres e quantos homems estavam à bordo, de acordo com o dataset?")
    st.code("tit['Sexo'].value_counts()")
    st.write(tit['Sexo'].value_counts())
    st.markdown("")
    st.subheader("10 - Quantos passageiros sobreviveram e quantos não sobreviveram?")
    st.code("tit['Sobreviveu'].value_counts()")
    st.write(tit['Sobreviveu'].value_counts())
    st.markdown("")
    st.subheader("11 - Quantas mulheres não sobreviveram?")
    st.code("tit.groupby('Sexo')['Sobreviveu'].value_counts()")
    st.write(tit.groupby('Sexo')['Sobreviveu'].value_counts())
    st.markdown("")
    st.subheader("12 - Proporcionalmente, sobreviveram mais homens ou mais mulheres? Cite as proporções.")
    st.code("tit.groupby('Sexo')['Sobreviveu'].value_counts(normalize= True, ascending= False)")
    st.write(tit.groupby('Sexo')['Sobreviveu'].value_counts(normalize= True, ascending= False))
    st.markdown("")
    st.subheader("13 - Levando-se em consideração a idade dos passageiros, qual a idade e quantidade de pessoas com o maior número de mortos?")
    st.code("age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]")
    st.code("age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']")
    st.code("tit['Faixa_Etária'] = pd.cut(tit['Idade'], bins=age_bins, labels=age_labels, right=False)")
    st.code("tit_filter = tit[tit['Sobreviveu'] == 'Não']")
    st.code("tit_filter.groupby('Faixa_Etária').size().reset_index(name='Count')")
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']
    tit['Faixa_Etária'] = pd.cut(tit['Idade'], bins=age_bins, labels=age_labels, right=False)
    tit_filter = tit[tit['Sobreviveu'] == 'Não']
    tit_filter.groupby('Faixa_Etária').size().reset_index(name='Count')
    st.write(tit_filter.groupby('Faixa_Etária').size().reset_index(name='Count'))
    st.markdown("")
    st.subheader("14 - Qual a média de idade dos homens sobreviventes?")
    st.code("homens_sobreviventes = tit[(tit['Sexo'] == 'Homem') & (tit['Sobreviveu'] == 'Sim')]")
    st.code("homens_sobreviventes['Idade'].mean()")
    homens_sobreviventes = tit[(tit['Sexo'] == 'Homem') & (tit['Sobreviveu'] == 'Sim')]
    idade_y = homens_sobreviventes['Idade'].mean()
    st.write(f"Idade média é {idade_y:.2f}")
    st.markdown("")
    st.subheader("15 - Levando-se em consideração passageiros prioritários (mulheres e crianças de até 15 anos independente do sexo) qual a proporção de sobreviventes por sexo?")
    st.code("prioritarios = tit[(tit['Sexo'] == 'Mulher') | (tit['Idade'] <= 15)]")
    st.code("prioritarios.groupby('Sexo')['Sobreviveu'].value_counts(normalize=True, ascending=False)")
    prioritarios = tit[(tit['Sexo'] == 'Mulher') | (tit['Idade'] <= 15)]
    prioritarios.groupby('Sexo')['Sobreviveu'].value_counts(normalize=True, ascending=False)
    st.write(prioritarios.groupby('Sexo')['Sobreviveu'].value_counts(normalize=True, ascending=False))
    st.markdown("")
    st.subheader("16 - Qual a quantidade de passageiros por classe?")
    st.code("tit['Classe'].value_counts(ascending=False)")
    tit['Classe'].value_counts(ascending=False)
    st.write(tit['Classe'].value_counts(ascending=False))
    st.markdown("")
    st.subheader("17 - Qual o percentual de sobreviventes por classe?")
    st.code("tit.groupby('Classe')['Sobreviveu'].value_counts(normalize=True, ascending=False)")
    tit.groupby('Classe')['Sobreviveu'].value_counts(normalize=True, ascending=False)
    st.write(tit.groupby('Classe')['Sobreviveu'].value_counts(normalize=True, ascending=False))
    st.markdown("")
    st.subheader("18 - Crie um dataframe que demonstre a quantidade de sobreviventes e não sobreviventes, agrupados por sexo e classe.")
    st.code("sexo_classe = tit.groupby(['Sexo', 'Classe'])['Sobreviveu'].value_counts(ascending=False).reset_index(name='Count')")
    sexo_classe = tit.groupby(['Sexo', 'Classe'])['Sobreviveu'].value_counts(ascending=False).reset_index(name='Count')
    st.write(sexo_classe = tit.groupby(['Sexo', 'Classe'])['Sobreviveu'].value_counts(ascending=False).reset_index(name='Count'))
    st.markdown("")
    st.subheader("19 - Dos homens com idade entre 24 e 30 anos quantos da classe 3 sobreviveram? Quantos da classe 2 não sobreviveram?")
    st.code("novo_df = tit[(tit['Sexo'] == 'Homem') & (tit['Idade'] <= 30) & (tit['Idade'] >= 24)]")
    st.code("novo_df.groupby('Classe')['Sobreviveu'].value_counts(ascending=False)")
    novo_df = tit[(tit['Sexo'] == 'Homem') & (tit['Idade'] <= 30) & (tit['Idade'] >= 24)]
    novo_df.groupby('Classe')['Sobreviveu'].value_counts(ascending=False)
    st.write(novo_df.groupby('Classe')['Sobreviveu'].value_counts(ascending=False))
    st.markdown("")

# Load Animation
with st.container():
    # JSON url
    lottie_bye = load_lottieurl("https://lottie.host/7381af27-2fa5-46d6-bcb7-1551561923b7/pstRlCQAJN.json")
    st_lottie(lottie_bye, key='bye', speed=1, width=350, height=350)
