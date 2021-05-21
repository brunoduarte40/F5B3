# usado para rodar versão exe windows
from datetime import datetime, timedelta

data_atual_semFormato = datetime.now()
data_atual = data_atual_semFormato.strftime("%d/%m/%Y")
data_atual_ano_mes_dia = data_atual_semFormato.strftime("%Y-%m-%d")
data_atual
import shutil
import re
import datetime
import pandas as pd


class Montante_atualizado:

    def __init__(self):
        self


if __name__ == '__main__':
    montante_atualizado = Montante_atualizado()

# usado para rodar versão exe windows
# from Codigos.Grafico_Montante_Aplicado import acao_vendidaOrdemCronologica, Montante_carteira_arrend

Valor_Atualizado = pd.read_csv(
    r'..\output\Valor_atualizado_Acoes\Valor_Atualizado.csv', sep=';')
# Valor_Atualizado = pd.read_csv(r'..\Codigos\Valor_atualizado_Acoes\Valor_Atualizado.csv', sep=';')
Valor_Atualizado = pd.DataFrame(Valor_Atualizado)

# usado para rodar versão exe windows
try:
    import httplib  # Python 2.7
except ImportError:
    import http.client as httplib  # Python 3.x
end_date = datetime.datetime.now()
dadosQTDAcoes = pd.read_csv(r'..\dados\BDACAOSA.csv', sep=';')
acao_dataEntrada = pd.DataFrame(dadosQTDAcoes, columns=['Ação', 'Data Entrada', 'Investimento Total', 'Valor Entrada'])
acao_dataEntrada = acao_dataEntrada.sort_values(by='Data Entrada', ascending=True)


##################
def obter_feriados(cidade, uf, ano=None):
    '''Obter lista de feriados por cidade e uf
       de www.feriadosmunicipais.com.br para determinado ano.'''

    # Conectar com o servidor www.feriadosmunicipais.com.br
    conexao = httplib.HTTPConnection('www.feriadosmunicipais.com.br')

    # Obter página dos feriados para a cidade e uf fornecidos
    conexao.request('GET', '/{}/{}/'.format(uf, cidade))
    resposta = conexao.getresponse()

    # Se teve algum erro, mostra o erro e retorna uma lista vazia
    if resposta.status != 200:
        conexao.close()
        print("{} - {}".format(resposta.status, resposta.reason))
        return []

    # Ler o HTML
    html = resposta.read()
    conexao.close()

    # Decodificar o HTML
    charset = re.compile(b'.*charset="([^"]*)".*', re.DOTALL)
    charset = re.sub(charset, r'\1', html)
    html = html.decode(charset.decode())

    # Encontrar os feriados e carnaval onde o padrão é numa linha ter
    # a data no formato dd/mm/aaaa e uma das palavras Feriado ou Carnaval
    feriados = re.findall(r'([0-9]{2}/[0-9]{2}/[0-9]{4}).*'
                          r'(?:Feriado|Carnaval)', html)

    # Converter para o tipo `datetime´ segundo padrão dd/mm/aaaa => %d/%m/%Y
    feriados = [datetime.datetime.strptime(f, '%d/%m/%Y') for f in feriados]

    # Filtrar as datas do ano desejado, se fornecido
    if ano:
        feriados = filter(lambda f: f.year == ano, feriados)

    # Alterar o tipo de `datetime´ para `date´
    feriados = map(lambda f: datetime.date(f.year, f.month, f.day), feriados)

    # Retornar os feriados ordenados

    return sorted(feriados)


def converter_para_data(data):
    '''Converte `data´ no padrão dd/mm/yyyy para o tipo datetime.date.'''
    if not isinstance(data, (datetime.datetime, datetime.date)):
        data = datetime.datetime.strptime(str(data), '%d/%m/%Y')
    if isinstance(data, datetime.datetime):
        data = datetime.date(data.year, data.month, data.day)
    return data


def dia_util(data, feriados=[], sabado_util=False):
    '''Retonar se o dia é útil (True) ou não (False) de acordo
       com uma lista de feriados e se sábado será considerado útil.'''
    data = converter_para_data(data)
    semana = data.weekday()
    return ((semana not in (5, 6) or (semana == 5 and sabado_util))
            and data not in feriados)


def proximo_dia_util(data, feriados=[], sabado_util=False,
                     anterior=False, d_mais=0):
    '''Retonar o dia útil de acordo com uma lista de feriados e se
       sábado será considerado útil, sendo a data fornecida
       acrescida (anterior=False) ou decrescida (anterior=True)
       de um dia útil mais `d_mais´ dias úteis.
       Se `d_mais´ for negativo, retorna a data fornecida se esta for útil.'''
    data = converter_para_data(data)
    um_dia = datetime.timedelta(-1 if anterior else 1)
    if d_mais > -1:
        data += um_dia
    while True:
        while not dia_util(data, feriados, sabado_util):
            data += um_dia
        d_mais -= 1
        if d_mais < 0:
            break
        data = data + um_dia
    return data


# usado para rodar versão exe windows

if __name__ == '__main__':
    datas_teste = [data_atual]

    # print("\n\n*** São Paulo ***")
    feriados = obter_feriados('sao-paulo', 'sao-paulo')
    # for feriado in feriados:
    # print(feriado.strftime("%d/%m/%Y"))

    for data in datas_teste:
        util = "é" if dia_util(data, feriados) else "não é"
        # print("{} {} dia útil nesta cidade!".format(data, util))

        anterior = proximo_dia_util(data, feriados, sabado_util=False,
                                    anterior=True)
        # print("\--> O dia útil anteior é {}".format(anterior.strftime("%d/%m/%Y")))
        # print(anterior)

if dia_util(data, feriados):
    print("é util")
    data_pesquisa = data_atual_ano_mes_dia
else:
    print("Não é util")
    data_pesquisa = anterior.strftime("%Y-%m-%d")

print(data_atual_ano_mes_dia)
print(data_atual)
print(data_pesquisa)

from datetime import datetime

hora_atuais = datetime.now()
hora_em_texto = hora_atuais.strftime("%H:%M")
hora_abertura_pregao_em_texto = ("10:30")
hora = datetime.strptime(hora_em_texto, "%H:%M")
hora_abertura_pregao = datetime.strptime(hora_abertura_pregao_em_texto, "%H:%M")
if (hora_abertura_pregao >= hora):
    print("antes de 10:30")
    data_pesquisa = anterior.strftime("%Y-%m-%d")
    print("antes das 10:30 o dia util é", data_pesquisa)
else:
    print("Depois das 10:30")

print(data_pesquisa)
# df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
Novo_Valor_Atualizado = Valor_Atualizado.rename(columns={"Unnamed: 0": "Ação", data_pesquisa: 'Valor_Atualizado'})
# Novo_Valor_Atualizado = Novo_Valor_Atualizado.columns.str.replace(data_pesquisa, 'log(gdp)')
##Novo_Valor_Atualizado = Valor_Atualizado.rename(columns={'Unnamed: 0:': "Ação"})
##Novo_Valor_Atualizado = Valor_Atualizado.rename(columns={data_pesquisa: 'Valor_Atualizado'})
print(Novo_Valor_Atualizado)
print(data_pesquisa)
##############################################################################################

import os.path

isExist = os.path.exists("..\\output\\Historico_unitario_acao")
if isExist == True:
    # shutil.rmtree(r"..\Codigos\Historico_unitario_acao")
    shutil.rmtree("..\\output\\Historico_unitario_acao");
    # os.mkdir(r"..\Codigos\Historico_unitario_acao")
    os.mkdir(r"..\output\Historico_unitario_acao");
else:
    # os.mkdir(r"..\Codigos\Historico_unitario_acao")
    os.mkdir("..\\output\\Historico_unitario_acao")

#


# dadosQTDAcoes = pd.read_csv(r"..\Dados\BDACAOSA.csv", sep = ';')
nomeAcoesEDataEntradaInvestimentoTotal = pd.DataFrame(dadosQTDAcoes,
                                                      columns=['Ação', 'Data Entrada', 'Investimento Total',
                                                               'Ação Vendida'])

acao_E_Invest = pd.DataFrame(dadosQTDAcoes,
                             columns=['Ação', 'Data Entrada', 'Valor Entrada', 'Quantidade', 'Investimento Total',
                                      'Ação Vendida'])

acao_vendidaOrdenada = acao_E_Invest.sort_values(by='Ação Vendida', ascending=True)

Qtd_acao = acao_vendidaOrdenada
Qtd_acao.loc[Qtd_acao['Ação Vendida'] == 0, 'Ação na carteira'] = True
Qtd_AcaoNaCarteira = Qtd_acao['Ação na carteira'].count()

AcaoNaCarteira = acao_vendidaOrdenada.head(Qtd_AcaoNaCarteira)

Montante_carteira = sum(AcaoNaCarteira['Investimento Total'])
Montante_carteira_arrend = round(Montante_carteira, 2)
print(Montante_carteira_arrend)

# import matplotlib.pyplot as plt
# AcaoNaCarteira.savefig('grafico.png')
import matplotlib as mpl, matplotlib.pyplot as plt

# plt.rc('figure', figsize = (250,50))
plt.rc('figure')
# print(mpl.__version__)
# fig, ax = plt.subplots()
# ax.set_facecolor('k')


# AcaoNaCarteira.plot(x='Ação', y='Investimento Total', kind='pie', labels = AcaoNaCarteira['Ação'], fontsize = 30, autopct='%1.1f%%')
Grafico = AcaoNaCarteira.plot(x='Ação', y='Investimento Total', kind='pie', labels=AcaoNaCarteira['Ação'], fontsize=5)
Grafico.legend().set_visible(False)
plt.savefig(r'..\output\Grafico_montante_atualizado.png', format='png')

# botar em ordem cronologica
acao_vendidaOrdemCronologica = AcaoNaCarteira.sort_values(by='Data Entrada', ascending=True)

##############################################
Novo_Valor_Atualizado = Novo_Valor_Atualizado[['Ação', 'Valor_Atualizado']]

MergeCodigoAcaoSA = acao_vendidaOrdemCronologica
SincroniaAcao = MergeCodigoAcaoSA.merge(Novo_Valor_Atualizado, left_on='Ação', right_on='Ação')

Montante_Atualizado = SincroniaAcao.assign(
    Investimento_Atualizado=SincroniaAcao['Valor_Atualizado'] * SincroniaAcao['Quantidade'])

carteiraAtualizada = sum(Montante_Atualizado['Investimento_Atualizado'])
carteiraAtualizada = round(carteiraAtualizada, 2)
print("Foi investido um montante de R$", Montante_carteira_arrend)
print("A carteira Atualizada contem um montante de R$", carteiraAtualizada)

valorizacao_carteira_atual = ((carteiraAtualizada * 100) / Montante_carteira_arrend) - 100
valorizacao_carteira_atual = round(valorizacao_carteira_atual, 2)
print(valorizacao_carteira_atual, "%")

Montante_Atualizado = Montante_Atualizado.assign(
    LucroPreju=Montante_Atualizado['Investimento_Atualizado'] - Montante_Atualizado['Investimento Total'])
Montante_Atualizado = Montante_Atualizado.assign(
    Percentual_Lucro_Ou_Preju=Montante_Atualizado['LucroPreju'] * 100 / Montante_Atualizado['Investimento Total'])
Montante_Atualizado = round(Montante_Atualizado, 2)

# Montante_Atualizado.to_csv('C:\\Users\\Tech\\Google Drive\\Compartilhada\\F5MYBOVESPA\\Codigos\\Montante_atualizado\\Montante_Atualizado.csv', index=False,
# sep=';')
# Montante_Atualizado.to_csv('..\\Codigos\\Montante_atualizado\\Montante_Atualizado.csv', index=False, sep=';')
Montante_Atualizado.to_csv(r'..\output\Montante_atualizado\Montante_Atualizado.csv',
                           index=False, sep=';')
