from datetime import datetime
from pandas_datareader import data as wb
import pandas as pd


class Grafico_unitario_acao_cronologica:

    def __init__(self):
        self


if __name__ == '__main__':
    dadosQTDAcoes = pd.read_csv(r"..\dados\BDACAOSA.csv", sep=';')
    qtd = dadosQTDAcoes
    qtd.loc[qtd['Ação Vendida'] == 0, 'Ação na carteira'] = True
    Qtd_Acao = qtd['Ação na carteira'].count()
    Montante_Atualizado = pd.read_csv(
        r'..\output\Montante_atualizado\Montante_Atualizado.csv', sep=';')
    acoes = Montante_Atualizado
    contador = 0
    data_atual = datetime.now()
    print(Qtd_Acao)

    while contador < Qtd_Acao:
        print(acoes.loc[[contador]]['Ação'])
        dataEntrada = acoes.loc[[contador]]['Data Entrada']
        try:
            prices = \
                wb.DataReader(acoes.loc[[contador]]['Ação'], data_source='yahoo', start=dataEntrada.all(),
                              end=data_atual)[
                    'Adj Close']
            prices['Base'] = 1
        except KeyError:
            pass

        # Data compra
        diaCompraSemFormato = Montante_Atualizado.loc[contador]['Data Entrada']
        diaCompra_Formatado = datetime.strptime(diaCompraSemFormato, '%Y-%m-%d')
        # Data atual
        today = datetime.now()
        dia_Atual_SemFormato = today.strftime("%Y-%m-%d")
        dia_Atual_Formatado = datetime.strptime(dia_Atual_SemFormato, '%Y-%m-%d')
        dia_Atual = dia_Atual_Formatado

        # Calculo da quantidade de dias
        quantidade_dias = abs((dia_Atual - diaCompra_Formatado).days)
        print("Quantidade de Dias: ", quantidade_dias)

        quantidade_mes_aprox = round((quantidade_dias / 30), 2)
        print("Quantidade de Meses: ", quantidade_mes_aprox)

        print("Ação rendeu: ", Montante_Atualizado.loc[contador]['Percentual_Lucro_Ou_Preju'], "%")

        MediaRendimentoMensal = (Montante_Atualizado.loc[contador]['Percentual_Lucro_Ou_Preju'] / quantidade_mes_aprox)
        MediaRendimentoMensal = round(MediaRendimentoMensal, 2)
        print("Média mensal de : ", MediaRendimentoMensal, "%")

        import matplotlib.pyplot as plt

        x = (prices / prices.iloc[0] * 100) - 100

        (x).plot(figsize=(7, 3),
                 grid=True,
                 markerfacecoloralt='red'
                 )

        plt.ylabel('Rendimento Ação desde a entrada')
        plt.xlabel('Data')

        # plt.xlim(40, 160)
        # plt.ylim(0, 0.03)

        type(acoes.loc[[contador]]['Ação'])
        print(acoes.loc[[contador]]['Ação'])
        flag = '%s' % str(Montante_Atualizado['Percentual_Lucro_Ou_Preju'][contador]) + " " + str(
            acoes['Ação'][contador])  # use the first element of list a as the name
        # valor= '%s' % str(Montante_Atualizado['Percentual_Lucro_Ou_Preju'][contador])
        print(flag)
        plt.title(flag)
        plt.savefig(r"..\output\Historico_unitario_acao\%s.png" % flag)
        # plt.savefig(r"..\Codigos\Historico_unitario_acao\%s.png" % flag)

        contador = contador + 1
