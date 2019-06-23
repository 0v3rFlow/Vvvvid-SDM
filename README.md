# Introduzione
Questo è il mio primo script in Python3. Ho voluto fare questo programma per mettermi alla prova e poter iniziare a conoscere questo linguaggio di programmazione. A questo, ho aggiunto anche la mia passione nel guardare gli anime giapponesi ed è cosi che è nato questo programma. Spero sia utile e che possa piacere come piace a me.

# V4id-SDM

V4id-SDM è script in Python3 che ti permette di guardare, comodamente e senza varie interruzioni, tutte le serie contenute all'interno del famoso sito italiano vvvvid.it con anche la possibilità di poterle scaricare.

 ## Requisiti e compatibiltà
 Lo script è stato scritto utilizzando Python3 e deve essere lanciato con questo. 
 L'ho testato sia con Windows (10) e su Linux.
 
 I moduli che ho utilizzato per creare lo script sono i seguenti :
 
 * requests
 * youtube_dl
 * colorama
 * terminaltables
 
Installare **FFMPEG** su entrambi i sistemi operativi. L'installazione è molto semplice, o cercate su internet oppure andate a questo link dove troverete tutto https://www.thepostspot.com/installare-ffmpeg/

Installare **VLC** su entrambi i sistemi operativi.

**NB: Non funziona fuori dall'Italia a meno che si utilizzi una VPN**

# Installazione su Windows 

**Se hai già installato python3 puoi pure saltare questo pezzo**

* Scaricare ed installare Python da qui (https://www.python.org/downloads/). L'ultima versione che vi propone va benissimo;
  **NB: durante l'installazione selezionare la casella *Add Python to PATH***;
* Riavviare il computer;

**FFMPEG**

* Segui le istruzioni che trovi sul link ( non preoccuparti sono veramente molto semplici ). 
  https://www.thepostspot.com/installare-ffmpeg/
**NB: Se il link non funzionasse su google/youtube trovi molte guide su come installarlo.**

**VLC**
* Scaricate ed installate VLC da qui https://www.videolan.org/vlc/
* Ora dobbiamo aggiungere vlc lanciabile dal prompt dei comandi di windows. Puoi seguire questa semplice guida da 1 minuto (https://www.vlchelp.com/add-vlc-command-prompt-windows/).

Ora che avete sia Python FFMPEG e VLC installati potete scariccare questo repository.
* Scaricare questo repository in formato zip cliccando sul bottone verde 'Clone or Download';
* Estrarre il file zip in una cartella;
* Eseguire il file `v4id-sdm-win-setup` per installare automaticamente i moduli di Python richiesti.

* Ora potete lanciare `v4id-sdm-win.bat`

Enjoy :)



# Installazione su Linux  

**Se hai già installato python3 puoi pure saltare questo pezzo**

```bash
sudo apt-get update
sudo apt-get install python3.*
```

**FFMPEG**
* Segui le istruzioni che trovi sul link ( non preoccuparti sono veramente molto semplici ). 
  https://www.thepostspot.com/installare-ffmpeg/
**NB: Se il link non funzionasse su google/youtube trovi molte guide su come installarlo.**

**VLC**
* Scaricate ed installate VLC da qui https://www.videolan.org/vlc/


Ora che avete sia Python FFMPEG e VLC installati potete scaricare questo repository.

```bash
git clone https://github.com/0v3rFlow/Vvvvid-SDM.git
cd Vvvvvid-SDM
pip install -r requirements.txt
chmod +x ./v4id-sdm.py
```

Enjoy :)

## Utilizzo
Una volta avviato lo script avrai a disposizione 2 opzioni:
* Streaming di un episodio(VLC Obbligatorio)
* Download episodio/serie

### Streaming di un episodio(VLC Obbligatorio) ###
* Basta che inseriate il link dell'episodio per far partire lo streaming. Il link è lo stesso che viene lanciato quando schiacci sul sito il pulsante play.

### Download episodio/serie ###
Come nel sito potrai scegliere le stagioni in base ai seguenti filtri:
* 1)In Evidenza
* 2)Popolari
* 3)Nuove uscite 
* 4)Filtro A-Z ( Inserire l'iniziale della serie che si vuole cercare )

In base alla scelta lo script ci risponderà con le stagioni.
Esempio:

```bash
1) In Evidenzia
2) Popolari
3) Nuove uscite
4) Filtro A-Z
0) Indietro

V4id-SDM>> 1
```

```bash
+----+--------------------------------------------------+--------------------+-----------+
| ID | Titolo                                           | Data pubblicazione | Views     |
+----+--------------------------------------------------+--------------------+-----------+
| 1  | L'Attacco dei Giganti - Terza Stagione           | 2018               | 7.658.411 |
| 2  | One-Punch Man - Seconda stagione                 | 2019               | 3.521.184 |
| 3  | Demon Slayer                                     | 2019               | 1.354.187 |
| 4  | Tokyo Ghoul:re                                   | 2018               | 6.109.987 |
| 5  | Le bizzarre avventure di Jojo - Vento Aureo      | 2018               | 2.663.030 |
| 6  | Star Blazers 2202                                | 2017               | 236.643   |
| 7  | The Promised Neverland                           | 2019               | 1.284.060 |
| 8  | Sword Art Online: Alicization                    | 2018               | 3.324.257 |
| 9  | Goblin Slayer                                    | 2018               | 2.038.531 |
| 10 | Steins;Gate 0                                    | 2018               | 1.102.815 |
| 11 | In questo angolo di mondo                        | 2016               | 16.172    |
| 12 | No Game No Life: Zero                            | 2017               | 75.785    |
| 13 | Infini-T Force Movie                             | 2018               | 8.927     |
| 14 | Gurazeni                                         | 2018               | 280.169   |
| 15 | My Hero Academia – Terza stagione                | 2018               | 5.576.441 |
| 16 | Megalo Box                                       | 2018               | 760.984   |
| 17 | Sword Art Online Alternative: Gun Gale Online    | 2018               | 811.081   |
| 18 | I Miei 23 Schiavi - Dorei-ku The Animation       | 2018               | 325.760   |
| 19 | Full Metal Panic! Invisible Victory              | 2018               | 286.157   |
| 20 | Devils' Line                                     | 2018               | 707.829   |
| 21 | Legend of the Galactic Heroes                    | 2018               | 126.305   |
| 22 | Tokyo Ghoul                                      | 2014               | 6.709.135 |
| 23 | Tokyo Ghoul vA                                   | 2015               | 5.462.814 |
| 24 | Kill la Kill                                     | 2013               | 1.255.173 |
| 25 | Another                                          | 2012               | 714.256   |
| 26 | Code Geass: Akito the Exiled                     | 2012               | 307.107   |
| 27 | La Grande Avventura del Piccolo Principe Valiant | 1968               | 3.299     |
| 28 | Pop Team Epic                                    | 2018               | 162.265   |
| 29 | Dame x Prince Anime Caravan                      | 2018               | 152.372   |
| 30 | No Game No Life                                  | 2014               | 982.554   |
+----+--------------------------------------------------+--------------------+-----------+
[ID] #Info Serie. [0] #Indietro. 
```
Ora inseriamo l'ID che è il numero che corrisponde all'episodio.  
Esempio:  1 e poi invio.

```bash

[ID] #Info Serie. [0] #Indietro. 1
+----------------------------------------+---------------------------------------------------------------------------------------+
| L'Attacco dei Giganti - Terza Stagione | Attack on Titan (Shingeki no kyojin) - In precedenza gli uomini temevano il mondo     |
|                                        | esterno. Vivevano circondati da mura invalicabili, innalzate allo scopo di proteggere |
|                                        | l’umanità dai Giganti: creature a immagine dell’uomo, ma snaturate nel comportamento  |
|                                        | e negli appetiti. Inchiodati a catene invisibili, gli uomini oggi hanno imparato che  |
|                                        | neppure dentro le mura la sicurezza è garantita. Dopo la brutale minaccia del Gigante |
|                                        | Bestia e la fuga dei traditori, Eren e compagni vedono scossi nelle fondamenta i      |
|                                        | valori con cui sono cresciuti. Minacciati nella sopravvivenza continueranno a cercare |
|                                        | un fuoco di verità che illumini il loro cammino.                                      |
+----------------------------------------+---------------------------------------------------------------------------------------+
[IT/JP] #In che lingua vuoi la stagione ? JP
```
Verrà visualizzata la trama della stagione. Se è stato doppiato in italiano possiamo scegliere la lingua tra 'IT' o 'JP'.
Esempio : JP

```bash
+----+-----------------------------------------------+-----------------+-------------+-------------------+
| ID | Titolo                                        | Numero episodio | Disponibile | Data Uscita       |
+----+-----------------------------------------------+-----------------+-------------+-------------------+
| 1  | Segnale di fumo                               | 01              | Si          |                   |
| 2  | Dolore                                        | 02              | Si          |                   |
| 3  | Storie passate                                | 03              | Si          |                   |
| 4  | Fiducia                                       | 04              | Si          |                   |
| 5  | Risposta                                      | 05              | Si          |                   |
| 6  | Peccato                                       | 06              | Si          |                   |
| 7  | Desiderio                                     | 07              | Si          |                   |
| 8  | Le mura del distretto di Orvud                | 08              | Si          |                   |
| 9  | Monarca delle Mura                            | 09              | Si          |                   |
| 10 | Amici                                         | 10              | Si          |                   |
| 11 | Spettatore                                    | 11              | Si          |                   |
| 12 | La notte prima dell'operazione di riconquista | 12              | Si          |                   |
| 13 | La città dove tutto iniziò                    | 13              | Si          |                   |
| 14 | Le lance fulmine                              | 14              | Si          |                   |
| 15 | La venuta                                     | 15              | Si          |                   |
| 16 | Partita perfetta                              | 16              | Si          |                   |
| 17 | Il coraggioso                                 | 17              | Si          |                   |
| 18 | Sole di mezzanotte                            | 18              | Si          |                   |
| 19 | La cantina                                    | 19              | Si          |                   |
| 20 | Quel giorno                                   | 20              | Si          |                   |
| 21 | Episodio 21                                   | 21              | No          | 24 giu 2019 18:00 |
+----+-----------------------------------------------+-----------------+-------------+-------------------+
[ID] #Download/Streaming. [0] #Indietro. [00] #Download di tutti gli episodi

```
Adesso abbiamo 2 possibilità: scegliere un episodio oppure scaricare tutta la serie
**NB: Se gli episodi devono essere ancora pubblicati, vedrà solamente la data di uscita**

**NB2: Se dicidi di scaricare tutta la serie o un solo episodio verrà creata una cartello dentro la cartella dello script con il nome"Vvvvid" e al suo interno troverai divisi per lingua tutte le serire con i lori episodi**

**-> Cartella : VVVVID -> JP -> L'attacco dei giganti -> Episodio 1...**

**->                   -> IT -> L'attacco dei giganti -> Episodio 1...**
          
Esempio: 1

```bash
+----+-----------------------------------------------+-----------------+-------------+-------------------+
| ID | Titolo                                        | Numero episodio | Disponibile | Data Uscita       |
+----+-----------------------------------------------+-----------------+-------------+-------------------+
| 1  | Segnale di fumo                               | 01              | Si          |                   |
| 2  | Dolore                                        | 02              | Si          |                   |
| 3  | Storie passate                                | 03              | Si          |                   |
| 4  | Fiducia                                       | 04              | Si          |                   |
| 5  | Risposta                                      | 05              | Si          |                   |
| 6  | Peccato                                       | 06              | Si          |                   |
| 7  | Desiderio                                     | 07              | Si          |                   |
| 8  | Le mura del distretto di Orvud                | 08              | Si          |                   |
| 9  | Monarca delle Mura                            | 09              | Si          |                   |
| 10 | Amici                                         | 10              | Si          |                   |
| 11 | Spettatore                                    | 11              | Si          |                   |
| 12 | La notte prima dell'operazione di riconquista | 12              | Si          |                   |
| 13 | La città dove tutto iniziò                    | 13              | Si          |                   |
| 14 | Le lance fulmine                              | 14              | Si          |                   |
| 15 | La venuta                                     | 15              | Si          |                   |
| 16 | Partita perfetta                              | 16              | Si          |                   |
| 17 | Il coraggioso                                 | 17              | Si          |                   |
| 18 | Sole di mezzanotte                            | 18              | Si          |                   |
| 19 | La cantina                                    | 19              | Si          |                   |
| 20 | Quel giorno                                   | 20              | Si          |                   |
| 21 | Episodio 21                                   | 21              | No          | 24 giu 2019 18:00 |
+----+-----------------------------------------------+-----------------+-------------+-------------------+
[ID] #Download/Streaming. [0] #Indietro. [00] #Download di tutti gli episodi 1
[D] #Download. [S] #Streaming. [0] #Indietro. 

```
Ora lo script ci chiede se vogliamo scaricare [D] il singolo episodio oppure lo vogliamo semplicemente guardare [S].
Esempio: [Ð] = Download terminato troverai l'episodio nella stessa cartella dello scritp. [S] = Verrà aperto VLC.

## FINE!

Spero che possiate apprezzare il mio programma ed il mio impegno. Sicuramente il codice non è scritto a livello avanzato, ma per me aver raggiuto questo obiettivo è stato molto gratificante. Non mi fermerò qui! Cercherò di fare altri piccoli progetti per migliorarmi ancora di più ;)

Se vi è piaciuto il mio programma lasciate pure una stella e se vi fa piacere, offrirmi anche un caffè :) https://www.paypal.me/VvvvidSDM














 
 
 
 




