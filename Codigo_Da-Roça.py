clientes_distancia = {  
    "cliente01": 10,
    "cliente02": 22,
    "cliente03": 15
}
#os clientes e as distâncias de cada um!
                    
clientes=["cliente#79", "cliente#27", "cliente#13"]
motoristas=["motorista01", "motorista02", "motorista03"]

clientes_nao_atentidos=["cliente#13"]
motoristas_disponiveis=["motorista03"]

horas_trabalhadas=0
rota=[]

while clientes_nao_atentidos or motorista:
    motorista_atual=motoristas_disponiveis

cliente_mais_longe_nao_visitado=clientes_distancia
cliente_cadandidato=clientes_nao_atentidos
cliente_mais_proximo_do_outro_visitado=clientes_distancia

hora=[cliente_mais_longe_nao_visitado]
while horas_trabalhadas<=8:
    cliente_cadandidato=[cliente_mais_proximo_do_outro_visitado]

velocidademédia=50 
distancia= cliente_cadandidato
tempoDeslocamento=clientes_distancia/velocidademédia
tempoRetorno=clientes_distancia[cliente_candidato] / velocidade_media


if horas_trabalhadas+tempoDeslocamento+tempoAbastecimento+tempoEntrega>8:
    rota=[clientes_nao_atentidos]

if horas_trabalhadas==horas_trabalhadas+tempoDeslocamento+tempoAbastecimento:
    break

if 3> horas_trabalhadas<5:
    horas_trabalhadas=horas_trabalhadas ++ 