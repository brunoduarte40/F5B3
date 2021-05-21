import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Grafico_geral_lucroXprejuizo:

    def __init__(self):
        self


if __name__ == '__main__':
    grafico_geral_lucroXprejuizo = Grafico_geral_lucroXprejuizo()

#Montante_Atualizado = pd.read_csv('..\\Codigos\\Montante_atualizado\\Montante_Atualizado.csv', sep=';')
Montante_Atualizado = pd.read_csv(r'..\output\Montante_atualizado\Montante_Atualizado.csv', sep=';')
plt.rc('figure', figsize=(110, 40))

figMedia = Montante_Atualizado.plot.bar(color='blue', x='Ação', y='Percentual_Lucro_Ou_Preju', fontsize=55, grid=True)
figMedia.set_ylabel('%', {'fontsize': 60})
figMedia.set_title('Rendimento % desde a entrada', {'fontsize': 80})

plt.savefig(r'..\output\Grafico_geral_lucro.png', format='png')