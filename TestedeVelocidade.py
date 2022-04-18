import speedtest
import time


while True:
    print('='*60)
    print('Verificando sua velocidade de internet...')
    print('='*60)


    threads = 16
    servers=[22997]
    s = speedtest.Speedtest()

    try:
        s.get_servers(servers)
    except:
        s.get_closest_servers()
        s.get_best_server()

    s.download(threads=threads)
    s.upload(threads=threads)
    s.results
    resultado = s.results.dict()
    download = float(resultado['download']/10**6)
    upload = float(resultado['upload']/10**6)
    ping = float(resultado['ping'])
    servidor = resultado['server']["sponsor"]
    ip = resultado['client']["ip"]
    empresa = resultado['client']["isp"]

    print(f'Download: {download:.2f}\nUpload: {upload:.2f}\nPing: {ping:.2f}\nServidor: {servidor}'
          f'\nIp: {ip}\nEmpresa: {empresa}')
    print('='*60)
    time.sleep(300)

