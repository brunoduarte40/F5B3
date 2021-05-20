import shutil
import pandas as pd
import matplotlib.pyplot as plt
import os


class Montante_aplicado:

    def __init__(self):
        self


if __name__ == '__main__':
    montante_aplicado = Montante_aplicado()
    dadosQTDAcoes = pd.read_csv(r"J:\Compartilhada\Compartilhada\F5BOVA\Dados\BDACAOSA.csv", sep=';')
    isExist = os.path.exists("J:\\Compartilhada\\Compartilhada\\F5BOVA\\Codigos\\Historico_unitario_acao")

    if isExist == True:
        shutil.rmtree("J:\\Compartilhada\\Compartilhada\\F5BOVA\\Codigos\\Historico_unitario_acao");
        os.mkdir(r"J:\Compartilhada\Compartilhada\F5BOVA\Codigos\Historico_unitario_acao");
    else:
        os.mkdir("J:\\Compartilhada\\Compartilhada\\F5BOVA\\Codigos\\Historico_unitario_acao")
    ##########################################################################################################
    nomeAcoesEDataEntradaInvestimentoTotal = \
        pd.DataFrame(dadosQTDAcoes,
                     columns=['Ação', 'Data Entrada', 'Investimento Total',
                              'Ação Vendida'])

    acao_E_Invest = \
        pd.DataFrame(dadosQTDAcoes,
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
    plt.rc('figure')
    Grafico = AcaoNaCarteira.plot(x='Ação', y='Investimento Total', kind='pie', labels=AcaoNaCarteira['Ação'],
                                  fontsize=5)
    Grafico.legend().set_visible(False)
    plt.savefig(r'J:\Compartilhada\Compartilhada\F5BOVA\Codigos\Grafico.png', format='png')

    # botar em ordem cronologica
    acao_vendidaOrdemCronologica = AcaoNaCarteira.sort_values(by='Data Entrada', ascending=True)

    # inserir grafico de barras
    figMedia = acao_vendidaOrdemCronologica.plot.bar(color='blue', x='Ação', y='Investimento Total', fontsize=5,
                                                     grid=True)
    figMedia.set_ylabel('R$ Aplicado', {'fontsize': 6})
    figMedia.set_title('Valores Aplicados na carteira', {'fontsize': 8})

    plt.savefig(r'J:\Compartilhada\Compartilhada\F5BOVA\Codigos\figMedia.png', format='png')
