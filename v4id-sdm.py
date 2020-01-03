# -----------------------------------------------------------------------------#
# Autore      : 0v3rFlow
# Descrizione : Vvvvid Streaming Downdload Manager. Guarda in streaming e
#               scaricare tutte le serie contenute sul sito Vvvvid.
#               Enjoy :D
# -----------------------------------------------------------------------------#

import os, shutil, requests, youtube_dl, locale, re
from platform import system
from colorama import Fore, init, Style
from terminaltables import AsciiTable
from textwrap import wrap


# Costanti generiche
connid_url = 'https://www.vvvvid.it/user/login'
canale_url = 'https://www.vvvvid.it/vvvvid/ondemand/anime/channels?'
ondemand_url = 'https://www.vvvvid.it/vvvvid/ondemand/'
const01 = 'Windows'
const02 = 'Linux'
const03 = 'clear'
const04 = 'cls'
const05 = Fore.LIGHTYELLOW_EX + 'V4id-SDM>> ' + Fore.RESET
const13 = 'vlc'
const14 = Fore.LIGHTGREEN_EX + '[URL] #Url episodio. [0] #Indietro. '
const20 = Fore.LIGHTGREEN_EX + "[ID] #Info Serie. [0] #Indietro. "
const21 = '/info/?'
const22 = '/seasons/?'
const23 = Fore.LIGHTGREEN_EX + '[IT/JP] #In che lingua vuoi la stagione ? '
const24 = Fore.LIGHTGREEN_EX + '[ID] #Download/Streaming. [0] #Indietro. [00] #Download di tutti gli episodi '
const25 = Fore.LIGHTGREEN_EX + '[D] #Download. [S] #Streaming. [0] #Indietro. '
const26 = Fore.LIGHTGREEN_EX + '[A/a-Z/z] #Inserisci un carattere alfabetico. [0] #Indietro '

# Costanti per schermata principale
const06 = Fore.LIGHTYELLOW_EX + '=========================' + Fore.RESET
const07 = Fore.LIGHTYELLOW_EX + '*       V4ID-SDM        *' + Fore.RESET
const08 = Fore.LIGHTGREEN_EX + 'Benvenuto\n'
const09 = Fore.LIGHTGREEN_EX + 'Comandi:\n'
const10 = '1) Streaming di un episodio'
const11 = '2) Download episodio/serie'
const12 = '0) Esci\n'

# Costanti pagina download
const15 = '1) In Evidenzia'
const16 = '2) Popolari'
const17 = '3) Nuove uscite'
const18 = '4) Filtro A-Z'
const19 = '0) Indietro\n'

# Testi errore
texte01 = Fore.RED + 'ERRORE: ' + Fore.RESET + Fore.LIGHTGREEN_EX + 'VLC non è installato. Impossibile procedere' + Fore.RESET
texte02 = Fore.RED + 'ERRORE: ' + Fore.RESET + Fore.LIGHTGREEN_EX + "Inserire in modo corretto il link. Copia il link dell'episodio che trovi nella barra di ricerca in alto nel sito" + Fore.RESET
texte03 = Fore.RED + 'ERRORE: ' + Fore.RESET + Fore.LIGHTGREEN_EX + 'Nessun risultato trovato' + Fore.RESET

# Header
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}


def carattere_ok(f, pattern):
    len_str = len(f)
    if len_str == 1 and pattern.match(f):
        return True
    else:
        return False


def filtro_az(f=None):
    pattern = re.compile("^([a-z])")
    if not f:
        f = input(const26)
        f.lower()
        if f == '0':
            pagina_download()
        else:
            while not carattere_ok(f, pattern):
                f = input(const26)
                f.lower()
        estrai_serie("A - Z", '4', f)
    else:
        estrai_serie("A - Z", '4', f)


def in_evidenza():
    estrai_serie('In Evidenza', '1')


def popolari():
    estrai_serie('Popolari', '2')


def nuove_uscite():
    estrai_serie('Nuove uscite', '3')


def converti_views(views):
    locale.setlocale(locale.LC_ALL, '')
    views = "{:n}".format(views)
    return views


def estrai_id_serie(json_data, show_id_dict, table, idx):

    for data in json_data:
        # Per ogni record vado a prendermi il numero delle views, il titolo e se l'episodio deve ancora uscire
        # la data di pubblicazione
        idx = idx + 1
        views = data['views']
        views = converti_views(views)
        # table.insert(idx, (idx, titolo, dpubli, views))
        table.insert(idx, (idx, data['title'], data['date_published'], views))
        show_id_dict.update({str(idx): data['show_id']})
    return idx


def show_table(table):
    tabshow = AsciiTable(table)
    print(Fore.LIGHTGREEN_EX + tabshow.table + Fore.RESET)


def stampa_trama_serie(jsoninfo):
    table_data = []
    tablerows = []

    # Prendo il titolo più la descrizione
    title = jsoninfo['title']
    description = jsoninfo['description']

    # Creo la tabella con una riga per poi stampare
    tablerows.append(title)
    tablerows.append(description)
    table_data.append(tablerows)
    table = AsciiTable(table_data)
    max_width = 85
    wrapped_string = '\n'.join(wrap(description, max_width))
    table.table_data[0][1] = wrapped_string
    print(Fore.LIGHTGREEN_EX + table.table + Fore.RESET)

    return title


def scegli_lingua(episodi):

    etichette_ita = ['ITALIANO', 'italiano', 'ita', 'it', 'IT']
    lista_lingua_input = ['IT', 'JP']
    lingua_ita = ''

    json_rows = len(episodi)
    season_new = ''
    if json_rows > 1:
        for idx, ep in enumerate(episodi):
            # Cerco di capire se all'interno del tag name esiste la stringa 'Italiano' ecc..
            for etichette_ita in etichette_ita :
                if ep['name'].find(etichette_ita) != -1:
                    lingua_ita = 'X'
                    episodi_ita = ep
                    idx_it = idx
                    break
            if lingua_ita:
                break
        # Se esiste allora devo chiedere in che lingua si vuole guardare la serie
        if lingua_ita == 'X':
            lingua_input = ''
            while not lingua_input in lista_lingua_input:
                lingua_input = input(const23)

            if lingua_input == 'IT':
                episodi_new = episodi_ita
            else:
                if idx_it == 0:
                    idx_it = idx_it + 1
                    episodi_new = episodi[idx_it]
                else:
                    episodi_new = episodi[0]
    else:
        episodi_new = episodi[0]
        lingua_input = 'JP'

    # Restituisco gli episodi e la lingua
    return episodi_new, lingua_input


def my_hook(d):
    if d['status'] == 'finished':
        print('Download completato!')


def avvio_download(url, jsoninfoseason, showid, title, lingua_ep, parametro, st, idx, code_action=None):
    # bestvideo[height<=?1080]+bestaudio/best
    percorso_file = './' + lingua_ep + '/' + title + '/' + 'Episodio' + str(idx) + '-' + '%(title)s.%(ext)s'
    ydl_opts = {
                'format': "bestvideo+bestaudio/best",
                'outtmpl': percorso_file,
                'continuedl': True,
                'quiet': True,
                'progress_hooks': [my_hook],
                }

    print(title + ':' + ' ' + st + ' ' + '->' + ' ' + 'Download iniziato...')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if parametro:
        return
    else:
        mostra_stagioni(jsoninfoseason, showid, title, code_action, lingua_ep)


def download_stagione(dict_episodi, showid, title, seasonid, jsoninfoseason, lingua_ep, dict_title, code_action):
    idx = 0
    for episodio in dict_episodi:
        idx = idx + 1
        vid = int(dict_episodi[episodio])
        st = dict_title[episodio]
        url = "https://www.vvvvid.it/#!show/%s/%s/%s/%s/%s" % (showid, title, seasonid, vid, st)
        avvio_download(url, jsoninfoseason, showid, title, lingua_ep, 'X', st, idx)

    mostra_stagioni(jsoninfoseason, showid, title, code_action, lingua_ep)


def scegli_episodi(jsoninfoseason, dict_episodi, showid, title, seasonid, dict_title, lingua_ep, filtro, code_action):
    comandi_dict = ['S', 'D', '0']

    id = ''
    while not (id in dict_episodi or id == '0' or id == '00'):
        id = input(const24)

    if id in dict_episodi:
        
        comando = ''
        while not comando in comandi_dict:
            comando = input(const25)

        if comando == 'D':
            vid = int(dict_episodi[id])
            st = dict_title[id]
            url = "https://www.vvvvid.it/#!show/%s/%s/%s/%s/%s" % (showid, title, seasonid, vid, st)
            avvio_download(url, jsoninfoseason, showid, title, lingua_ep, None, st, id, code_action)
        elif comando == 'S':
            vid = int(dict_episodi[id])
            st = dict_title[id]
            url = "https://www.vvvvid.it/#!show/%s/%s/%s/%s/%s" % (showid, title, seasonid, vid, st)
            avvio_streaming(url, None, code_action, jsoninfoseason, showid, title, lingua_ep, filtro)
        elif comando == '0':
            scegli_episodi(jsoninfoseason, dict_episodi, showid, title, seasonid, dict_title, lingua_ep, filtro, code_action)
    elif id == '0':
        pass
        if filtro:
            filtro_az(filtro)
        else:
            chiama_pagina(code_action, download_menu_actions)
    elif id == '00':
        pass
        download_stagione(dict_episodi, showid, title, seasonid, jsoninfoseason, lingua_ep, dict_title, code_action)
        scegli_episodi(jsoninfoseason, dict_episodi, showid, title, seasonid, dict_title, lingua_ep)
    else:
        pass


def mostra_stagioni(jsoninfoseason, showid, title, code_action, lingua_ep=None, filtro=None):

    # Dizionari per salvare i codici di ogni episodio ed il suo titolo
    dict_episodi = {}
    dict_title = {}

    # Lista righe per la tabella
    table = []

    # Header tabella
    tableheader = ['ID','Titolo', 'Numero episodio', 'Disponibile', 'Data Uscita']
    table.append(tableheader)


    if not lingua_ep:
        jsoninfoseason, lingua_ep = scegli_lingua(jsoninfoseason)
    seasonid = jsoninfoseason['season_id']

    idx = 0
    # Per ogni episodio vado a prendermi i codici che identificano l'episodio e se è disponibile. Quando ho fatto
    # mostro a video il risultato.
    for data in jsoninfoseason['episodes']:
        idx = idx + 1

        if  data['playable'] == False:
            datauscita = data['availability_date']
            disponibile = 'No'
        else:
            datauscita = ' '
            disponibile = 'Si'
            dict_episodi.update({str(idx): str(data['video_id'])})

        dict_title.update({str(idx): str(data['title'])})
        table.insert(idx, (idx, data['title'], data['number'], disponibile, datauscita))

    show_table(table)

    scegli_episodi(jsoninfoseason, dict_episodi, showid, title, seasonid, dict_title, lingua_ep, filtro, code_action)


def getinfo(showid, session, params, code_action, filtro=None):

    # Recupero il json con i dettagli della serie che ho selezionato
    url_info = ondemand_url + str(showid) + const21
    jsoninfo = session.get(url_info, params=params, headers=headers, cookies=session.cookies).json()['data']

    # Costruisco e stampo la tabella con la titolo e trama serie
    title = stampa_trama_serie(jsoninfo)

    # Recupero tutti gli episodi della serie
    url_season = ondemand_url+ str(showid) + const22
    jsoninfoseason = session.get(url_season, params=params, headers=headers, cookies=session.cookies).json()['data']

    # Mostro tutti gli episodi della serie
    mostra_stagioni(jsoninfoseason, showid, title, code_action, None, filtro)


def estrai_serie(nome_azione, code_action, filtro=None):
    clear()

    # Mi collego al sito VVVVID per prendere le serie che sono in evidenza
    s = requests.Session()

    # Recupero il connid che utlizza il sito per poter naviagare tra le pagina
    connid = s.get(connid_url, headers=headers, cookies=s.cookies).json()['data']['conn_id']
    params = {'conn_id': connid}

    # Estraggo il json che contiene i codici 'id' per visualizzare i vari canali
    canale_anime = s.get(canale_url, params=params, headers=headers, cookies=s.cookies ).json()['data']

    # Vado a prendermi il codice id riferito a quelli in evidenza
    for canale in canale_anime:
        if canale['name'] == nome_azione:
            # Prendo il numero che identifica il canale che voglio visualizarre tra: popolari, in evidenza, nuove uscite,
            # filtro a-z
            id_canale = canale['id']
            break

    # Se ho scelto il canale "Filtro A-Z" devo passare nell'url anche il filtro
    if nome_azione == 'A - Z':
        params = {'filter': filtro,
                  'conn_id': connid}

    url_stagioni = 'https://www.vvvvid.it/vvvvid/ondemand/anime/channel/%s/last?' % (id_canale)

    try:
        json_serie = s.get(url_stagioni, params=params, headers=headers, cookies=s.cookies).json()['data']
    except:
        print(texte03)
        filtro_az()

    try:
        url_evidenza = 'https://www.vvvvid.it/vvvvid/ondemand/anime/channel/%s/?' % (id_canale)
        json_serie_new = s.get(url_evidenza, params=params, headers=headers, cookies=s.cookies).json()['data']
    except:
        json_serie_new = ''

    # Dizione che contiene i codice che identifica la serie
    serie_id_dict = {}

    # Lista di testata per la tabella
    tableheader = ['ID','Titolo', 'Data pubblicazione', 'Views']

    # Lista righe per la tabella
    table = []

    # Inserisco la testata
    table.append(tableheader)
    idx = 0
    # serie_id_dict, table = estrai_id_serie(json_serie, json_serie_new)
    idx = estrai_id_serie(json_serie, serie_id_dict , table, idx)
    if json_serie_new:
        estrai_id_serie(json_serie_new, serie_id_dict , table, idx)

    show_table(table)

    idsel = ''
    while not idsel in serie_id_dict:
        idsel = input(const20)
        if idsel == '0':
            pagina_download()
            break
    showid = serie_id_dict[idsel]
    getinfo(showid, s, params, code_action, filtro)


def pagina_download():
    clear()
    stampa_testata()
    print(const09)
    print(const15)
    print(const16)
    print(const17)
    print(const18)
    print(const19)
    comando = input(const05)
    while not comando in download_menu_actions:
        comando = input(const05)
    chiama_pagina(comando, download_menu_actions)


def avvio_streaming(input_url, dict_action=None, code_action=None, season=None, showid=None, title=None, lingua_ep=None, filtro=None):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(input_url, download=False)
        # Prendo l'url che contiene l'm3u8
        m3u8 = meta['url']

    # Costruiamo il comando da lanciare
    avvia = "youtube-dl -q --no-warnings -o - %s | vlc -f -q -" % (m3u8)

    # Avvio lo streaming.
    os.system(avvia)
    
    # Se ho lo showid allora ritorno alla lista degli episodi
    if showid:
        clear()
        mostra_stagioni(season, showid, title, code_action, lingua_ep, filtro)
    else:
        # Quando chiudo lo streaming devo ritornare alla pagina precedente
        chiama_pagina(code_action, dict_action)


def pagina_streaming():
    # Verifico l'esistenza di VLC
    if shutil.which(const13):
        # Inserisci il link dell'episodio
        input_url = input(const14)
        if input_url == '0':
            main_menu()
        else:
            while not controlla_link(input_url):
                input_url = input(const14)

            input_url = input_url.replace('/show/', '/#!show/')
            avvio_streaming(input_url, main_menu_actions, '1')

    else:
        print(texte01)
        exit()


def chiama_pagina(comando, dict_action):
    # Vado a prendere la funzione che è attribuita al comando
    clear()
    if comando in dict_action:
        dict_action[comando]()
    else:
        main_menu()


def clear():
    # Pulisco la schermata
    if system() == const01:
        os.system(const04)
    else:
        os.system(const03)


def stampa_testata():
    # Print della testata
    print(const06)
    print(const07)
    print(const06)


def stampa_menu():
    # Print del menu
    stampa_testata()
    print(const08)
    print(const09)
    print(const10)
    print(const11)
    print(const12)


def main_menu():
    clear()
    stampa_menu()
    comando = input(const05)
    # In base al codice che scelgo scatta la funzione
    chiama_pagina(comando, main_menu_actions)


def controlla_link(input_url):
    # verifico che il mio parametro non sia vuoto
    if not input:
        return False
    else:

        if input_url == '0':
            main_menu()
        else:
            # Faccio una chiamata al sito per verificare che vada bene
            try :
                get_link = requests.get(input_url, headers=headers)
                if get_link.status_code == 200:
                    return True
                else:
                   return False
            except:
                print(texte02)


# Dizionari
main_menu_actions = {
                    'main_menu': main_menu,
                    '1': pagina_streaming,
                    '2': pagina_download,
                    '0': exit,
                    }

# Download action
download_menu_actions = {
                        '1': in_evidenza,
                        '2': popolari,
                        '3': nuove_uscite,
                        '4': filtro_az,
                        '0': main_menu,
                        }

if __name__ == "__main__":
    # Lancio il menu
    main_menu()
