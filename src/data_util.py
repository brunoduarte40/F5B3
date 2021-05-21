from datetime import datetime, timedelta

data_atual_semFormato = datetime.now()
data_atual = data_atual_semFormato.strftime("%d/%m/%Y")
data_atual_ano_mes_dia = data_atual_semFormato.strftime("%Y-%m-%d")
data_atual

import re
import datetime

class Data_util:

    def __init__(self):
        self


if __name__ == '__main__':
    data_util = Data_util()


try:
    import httplib  # Python 2.7
except ImportError:
    import http.client as httplib  # Python 3.x


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


if __name__ == '__main__':
    datas_teste = [data_atual]

    print("\n\n*** São Paulo ***")
    feriados = obter_feriados('sao-paulo', 'sao-paulo')
    for feriado in feriados:
        print(feriado.strftime("%d/%m/%Y"))

    for data in datas_teste:
        util = "é" if dia_util(data, feriados) else "não é"
        print("{} {} dia útil nesta cidade!".format(data, util))

        anterior = proximo_dia_util(data, feriados, sabado_util=False,
                                    anterior=True)
        print("\--> O dia útil anteior é {}".format(anterior.strftime("%d/%m/%Y")))
        print(anterior)
