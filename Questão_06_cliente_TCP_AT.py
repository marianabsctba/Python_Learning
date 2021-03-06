#Questão 06)
#Escreva um programa cliente e servidor sobre TCP em Python em que:
#O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
#O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

import socket, pickle

def lin():
    # linhas apenas para separação
    print('==' * 20)

def client():    
    #socket cliente

    HOST = socket.gethostname()
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    lin()
    diret = input('Qual o nome do diretório? ')
    s.send(diret.encode('ascii'))

    request = b''
    
    while True:       
        data = s.recv(1024);
        print('Dados recebidos do servidor...')
        if not data: break
        request = request + data                
    
    data = pickle.loads(request)
    s.close()
   
    if data == list(data):
        lin()
        print(f'Arquivos do diretório {diret}:')
        lin()
        for i in data:
            print(i)
        lin()
        
    else:
        lin()
        print(data)
        lin()
    
        

if __name__ == '__main__':
    client()
