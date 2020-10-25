Welcome to the Centro Notifiche wiki! Please feel free to make any changes you want and put it out.

# New Features!
  - Work in progress 3.0.0
  - Added Automatic SSML for Alexa
  - Added support for media content id and type.

# Package Notification HUB

- [What This Is](#what-this-is)
- [What It Does](#what-it-does)
- [How this works](#how-this-works)
- [Requirements](#requirements)
- [How to install](#Installation)
- [File](#file)
  - [Secret (Configuration)](#secret)
  - [HUB Main](#hub-main)
  - [HUB Alexa](#hub-alexa)
  - [HUB Google](#hub-google)
  - [HUB Build Message](#hub-build-message)
  - [Hub Extra (optional)](#hub-extra-optional)
- [Variables Event Hub (script.my_notify)](#variables)
  - [Alexa](#alexa)
    - [Examples](#examples-alexa)
  - [Google](#google)
    - [Examples](#examples-google)
- [Lovelace](#lovelace)
- [Utility](#utility)
  - [Sensor Home Assistant Start](#sensor-home-assistant-start)
- [Automations Examples](#automations-examples)
- [FAQ](#FAQ)


# What This Is

Centro Notifiche è un package per Home Assistant, che funziona insieme all'[App Notifier][Notifier] in [AppDaemon][AppDaemon].<br>

Notification Center is a package for Home Assistant, which works together with the [Notifier][Notifier] App in [AppDaemon][AppDaemon].

# What It Does

Serve per inviare messaggi di testo (Telegram, Push...), 
TTS Google e Alexa, notifiche VoIP a te e/o ai tuoi dispositivi come PC, smartphone, pad, ecc.<br>

It is used to send text messages (Telegram, Push...), 
TTS Google and Alexa, Voip notifications to you and/or your devices such as Pcs, smartphones, pads, etc.

# How this works

In sintesi, si inviano le notifiche con il servizio script (`script.my_notify`) tramite delle variabili.
Lo script crea un evento in Home Assistant, con il nome "`HUB`" e con tutti i dati impostati nelle variabili.
L'applicazione Notifier di AppDaemon, in ascolto sull'evento HUB, al verificarsi di tale evento, 
distribuisce le notifiche di testo, audio e persistenti sui vari dispositivi, in base ai dati ricevuti.
Il package va configurato con il file secret, indispensabile per ottenere le giuste informazioni ed evitare 
continue modifiche in caso di aggiornamenti futuri.

In summary, you send notifications with the script service (`script.my_notify`) via variables. 
The script creates an event in Home Assistant, with the name "`HUB`" and with all the data set in the variables. 
Appdaemon’s Notifier application, which listens to the HUB event, distributes text, audio, 
and persistent notifications on the various devices based on the received data. 
The package must be configured with the secret file, 
essential to get the right information and avoid continuous changes in case of future updates.

# Requirements

Prima dell'installazione di questo package, dovrai installare l'app `Notifier`, 
e configurare le integrazioni di HA, `Time & date` e `Workday`

Before installing this package, you will need to install the `Notifier`app, 
and configure integrations of HA, `Time & date` and `Workday`

  - [AppDaemon][AppDaemon] - [Addon][Addon-AD]
  - [Notifier][Notifier]
  - [Sensor Time & Date][TimeDate]
    <details>
    <summary>Example - Click to expand</summary>

    ```yaml
    sensor:
      - platform: time_date
        display_options:
          - 'time'
          - 'date'
          - 'date_time'
          - 'date_time_utc'
          - 'date_time_iso'
          - 'time_date'
          - 'time_utc'
          - 'beat'
    ```
    </details>
  - [Sensor Workday][Workday]
    <details>
    <summary>Example - Click to expand</summary>

    ```yaml
    binary_sensor:
      - platform: workday
        country: IT
        workdays: [mon,tue,wed,thu,fri]
        excludes: [sat,sun,holiday]
        add_holidays:
          - '2021-08-31'
          - '2022-08-31'
          - '2023-08-31'
          - '2024-08-31'
          - '2025-08-31'
    ```
    </details>

# Installation

[Guida Installazione](https://hassiohelp.eu/2019/12/25/notifer/#Installazione)

# [File][package]

Nella cartella package, trovi tutti i file che servono per il corretto funzionamento del Centro Notifiche.

In the package folder, you will find all the files you need for the Notification Center to work properly.

## [Secret][Secret]

Come compilare il file secret per una corretta configurazione del package.
Il file '**secrets.yaml**' va creato dentro la cartella 'packages'.
Di seguito le voci corispondenti alle entità presenti nel package.

How to compile the secret file for proper package configuration.
The file '**secrets.yaml**' must be created in the folder 'packages'.
Here are the entries related to the entities present in the package.

<details>
<summary>Examples - Click to expand</summary>

- ### Section 1
  > In questa sezione ci sono le entità lette da Home Assistant
  >
  > In this section there are entities read by Home Assistant

  #### Gruppo `Device Tracker` or `Person`<br>
  > Serve per escludere il tts quando si è fuori casa.<br>
  > Inserisci i tuoi device_tracker o person con ENTITY_ID (Vedi note alla fine)<br>
  > (Es. entity_id = device_tracker.caio # Es. entity_id = person.caio)<br>

  > It’s to rule out TTS when you’re out of the house.
  > Enter your device_tracker or person with ENTITY_ID (See notes at the end)
  > (Ex. entity_id = device_tracker.caio # Ex. entity_id = person.caio)

  ```yaml
  # (Ref. group.location_tracker)
  location_tracker_hub:
    - person.caio
    - device_tracker.caio
  ```

  #### Input Select `Google` Media Player<br>
  > Media Player da usare come Default.<br>
  > Inserisci i tuoi dispositivi 'media_player' e/o 'group' e/o Sensor con il 'friandly_name'<br>
  > NB: Se non possiedi dispositivi Google, puoi eliminare il file hub_google.yaml ed il codice sottostante<br>

  ```yaml
  # (Ref. input_select.notification_media_player_google)
  notification_media_player_google_hub:
    - Red
    - Black
    - Black2
    - Gruppo Casa
    - Gruppo Google
    - Gruppo Google Notte
  ```

  #### Input Select `Alexa` Media Player<br>
  > Media Player Alexa da usare come Default.<br>
  > Inserisci i tuoi dispositivi 'media_player' e/o 'group' e/o Sensor con il 'friandly_name'<br>
  > NB: Se non possiedi dispositivi Alexa, puoi eliminare il file hub_alexa.yaml ed il codice sottostante

  ```yaml
  # (Ref. input_select.notification_media_player_alexa)
  notification_media_player_alexa_hub: 
    - Sala
    - Studio
    - Gruppo Alexa
    - Last Alexa
  ```

  #### Input Select `Notify`<br>
  > Per le notifiche testuali da usare come Default.<br>
  > Inserisci i tuoi servizi di notifica testo con NOME_SERVIZO (`object_id` vedi note alla fine)
  > Es. notify.nome_del_notificatore sarà "nome del notificatore" oppure "Nome del Notificatore"
  >     notify.geronimo sarà "Geronimo", notify.famiglia sarà "Famiglia", notify.telegram sarà "Telegram"
  >     motify.telegram_caio sarà "Telegram Caio" o "TELEGRAM CAIO" o "TELEGRAM Caio"...

  ```yaml
  # (Ref. input_select.text_notify)
  text_notify_hub:
    - Telegram
    - News
    - Pushover
    - Android
    - Pushbullet
    - Test Nome NOTIFICA
    - Mobile App Oneplus 5t
    - Mobile App Oneplus A5010
  ```

- ### Section 2
  > In questa sezione ci sono altri servizi letti dall'app Notifier
  > NB: Queste opzioni possono essere commentate, cancellate o impostate con `Null` se non si usano

  > I dati vanno inseriti con il seguente schema: <br>
  > SERVIZIO: NOME_SERVIZO (`object_id` vedi note alla fine) o PARAMETRO SERVIZIO <br>
  > Esempi: <br>
  > il servizio "tts.google_say" sarà impostato così **`tts_google: google_say `**<br>
  > il servizio "tts.google_translate_say" (_default_) **`tts_google: tts.google_translate_say`**<br>
  > Ogni servizio usa nomi e parametri differenti e in base alla tua configurazione in configuration.yaml<br>
  > Controlla i tuoi servizi, per ognuno ho inserito anche il link per la configurazione e/o informazioni<br>
  > [TTS Integration][TTS] - [Google Translate][GTranslate]

  ```yaml
  # Services 
  tts_google: google_translate_say # or google_say dipende da come hai chiamato il servizio.
  ```

  [First Addon by @AndBobsYourUncle][GAssistant1] <br>
  [Second Addon for amd64 machine by @marcelveldt][GAssistant2] <br>
  [Third Addon by @Apipa169][GAssistant3] <br>

  > ATTENZIONE, questo non è una notifica di testo!!! 
  >             Anche se si usa notify, non fa parte dei servizi per notifiche testo

  ```yaml
  notify_google: google_assistant
  ```

  [Dss Voip Notifier by @sdesalve][DssVoip]
  ```yaml
  sip_server_name: fritz.box:5060
  ```

- ### Section 3 (Optional)
  > In questa sezione ci sono altre entità lette da Home Assistant per Extra Feautures

  #### Group all media player Alexa
  ```yaml
  # (Ref. group.media_player_alexa)
  media_player_alexa:
    - media_player.sala
    - media_player.studio
  ```
  #### Group all media player Google

  ```yaml
  # (Ref group.media_player_google)
  media_player_google:
    - media_player.red
    - media_player.black
    - media_player.black2
    - media_player.vlc
  ```

- ### NOTE
  > entity_id - domain - [object_id][StateObj] - friendly_name

  > Ad esempio un device tracker del tipo `device_tracker.oneplus_a5010` è così suddiviso <br>
  > ```yaml
  > device_tracker.oneplus_a5010
  > \____________/.\___________/
  >       ^       ^       ^
  >       |       |       |
  >    domain +  dot  + object_id = entity_id (device_tracker.oneplus_a5010)
  > ```

  > Formato: `<domain>.<object_id>`. Esempio: light.cucina è un entity_id. Di norma il punto identifica un entity_id.
  > Spesso si fa confusione con il "nome" dell'entità `<object_id>` e il nome descrittivo `friendly_name`
  > Un nome descrittivo è qualcosa che un essere umano può facilmente leggere e ricordare ;O)
  > al posto di un codice o di un indirizzo e/o identificatore numerico.
  > Un entity_id che corrisponde a "`light.cucina`" può avere come nome descrittivo "`Lampadario Cucina`" 
  > e come nome dell'entity_id (meglio noto come ID dell'oggetto) "`cucina`".
  > l'entity_id va scritto sempre in minuscolo, con il sottotratto al posto dello spazio e il punto di divisione tra dominio e oggetto.

  Le liste possono essere scritte in uno dei seguenti modi:
  ```yaml
  # Modo 1
  notification_media_player_alexa_hub: [
    "Sala",
    "Studio",
    "Gruppo Alexa",
    "Last Alexa"
  ]

  # Modo 2
  notification_media_player_alexa_hub: 
    - Sala
    - Studio
    - Gruppo Alexa
    - Last Alexa
  ```
  </details>

## [Hub Main][HubMain]

Questo è il file principale, necessario per creare l'evento HUB tramite lo script my_notify.
Contiene numerose entities, dai sensori per calcolare il periodo del giorno, 
al sensore per il DND (Do Not Disturb), ai vari interruttori per controllare
priorità dei messaggi, testo e tts, vacanze, giorni festivi etc ect
e altro. 

<details>
<summary>To know all the package entities, use this jinja code in dev-tools templates - Click to expand</summary>

  ```yaml
  {% for state in states -%}
  {% if 'centro notifiche' in state.attributes.package|lower %}
  - {{ state.entity_id -}}
  {% endif %}
  {%- endfor %}
  ```
</details>

<details>
<summary>Jinja code to show all HubMain entities - Click to expand</summary>

```yaml
{% for state in states -%}
{% if 'centro notifiche' in state.attributes.package|lower 
  and 'main' in state.attributes.version|lower %}
- {{ state.entity_id -}}
{% endif %}
{%- endfor %}
```
</details>

## [Hub Alexa][HubGoogle]
Questo file contiene tutte le entities utilizzate per Alexa.
Se non hai nessun dispositivo Amazon Alexa, puoi eliminarlo, 
risparmiando inutili entities nel sistema.
<details>
<summary>Jinja code to show all HubAlexa entities - Click to expand</summary>

```yaml
{% for state in states -%}
{% if 'centro notifiche' in state.attributes.package|lower 
  and 'alexa' in state.attributes.version|lower %}
- {{ state.entity_id -}}
{% endif %}
{%- endfor %}
```
</details>

## [Hub Google][HubGoogle]
Questo file contiene tutte le entities utilizzate per Google.
Se non hai nessun dispositivo Google, puoi eliminarlo, 
risparmiando inutili entities nel sistema.

<details>
<summary>Jinja code to show all HubGoogle entities - Click to expand</summary>

```yaml
{% for state in states -%}
{% if 'centro notifiche' in state.attributes.package|lower 
  and 'google' in state.attributes.version|lower %}
- {{ state.entity_id -}}
{% endif %}
{%- endfor %}
```
</details>

## [Hub Build Message][HubBuild]

<details>
<summary>Examples - Click to expand</summary>

#### Credits for inspiration and mechanics

[Janet (The Good Place) (@Lentron)][Lentron]<br>
[Speech Engine (@CCOSTAN)][CCOSTAN]<br>
[Notifications (@mf-social)][mf-social]<br>
[Notification Center (@3vasi0n89)][3vasi0n89]<br>
[my-home-automation (@happyleavesaoc)][happyleavesaoc]<br>

</details>


## [Hub Extra][HubExtra] (Optional)

Questo file contiene una raccolta di altri binary sensor, automazioni e gruppi che uso con il package.
Ad esempio, un'automazione per regolare i volumi dei media player Alexa e Google, i gruppi dei media players
e il sensore presenza di persone in casa.

# Variables

> Ricordate sempre che queste opzioni sovrascrivono quelle impostate di default (UI)<br>
> Sotto `data:` andremo ad inserire tutti i parametri che riguardano la nostra notifica, compreso il messaggio vero e proprio, se non inseriamo nessun
> parametro ma soltanto il `message` il centro notifiche utilizzerà tutte le impostazioni di default che abbiamo settato nel frontend. Vi lascio una lista
> completa dei parametri `data` da noi previsti ed il loro funzionamento:

| Options               | Type      | Requirement   | Default   | Description |
| --------------------- | --------- | ------------- | --------- | ----------- |
| message | string  | Required    | | Messaggio da inviare. |
| title   | string  | Optional    | None | Titolo per le notifiche testuali |
| notify  | string<br>bool  | Optional    | input_select<br>text_notify | **0** / **False** / **Off** / **No** Non invia la notifica testuale.<br>**Nome del notify** invia notifica ad un dispositivo diverso da quello di default.
| caption  | string | Optional | Message | Testo diverso da message |
| file  | string | Optional | None | Link valido per invio di file. |
| url  | string | Optional | None |  Link valido per l'invio di immagini. |
| link  | string | Optional | None | Aggiunge il link nella notifica testuale [Esempio HassioHelp](https://hassiohelp.eu/). |
| called_number  | int | Optional | input_text<br>phone_called_number | Numero telefonico [DssVoip][DssVoip]<br>username o number [CallMeBot][Callmebot]<br>se diverso dal default. |
| priority  | bool | Optional | False | **1** / **True** / **On** / **Yes**<br>by-pass DND (do not disturb) e tutti gli switch. |
| no_show  | bool | Optional | False | **1** / **True** / **On** / **Yes**<br>disabilita la notifica persistente. |
| location  | string | Optional | All | **home**: invia notifica solo se in casa. <br> **not_home**: invia notifica solo se fuori casa. |
| alexa   | dict | Optional | None | [see below](#alexa) |
| google  | dict | Optional | None | [see below](#google) |

#### Alexa

| Options               | Type      | Requirement   | Default   | Description |
| --------------------- | --------- | -----------   | -------   | ----------- |
| mode                  | bool      | Required      | False  | **1** / **True** / **On** / **Yes**<br>Attiva Alexa senza parametri aggiuntivi e se message è valorizzato. |
| message_tts / message | string      | Optional      | message | Per alexa si può usare anche solo message<br>sovrascrive comunque il messaggio principale e non passa per il template build message. |
| media_player          | string      | Optional      | input_select<br>notification_media_player_alexa | **Entity**, **friendly_name**  o entrambi<br>per media player, sensore o gruppo.<br>(es. Last Alexa, Studio, media_player.sala) |
| volume                | float      | Optional    | None | Imposta il Volume con un valore compreso tra 0 e 1 (es. 0.3) |
| method                | string      | Optional      | input_select<br>default_alexa_method | all, speak |
| type                  | string      | Optional      | input_select<br>default_alexa_type | tts, announce, push, dropin, dropin_notification |
| title                 | string      | Optional      | None | Titolo per il servizio push (non valido per dropin notification)
| push                  | bool      | Optional      | False | **1** / **True** / **On** / **Yes**<br>Invia una notifica push oltre al messaggio tts |
| wait_time             | float      | Optional      | input_number<br>tts_wait_time | Tempo stimato per la conclusione del messaggio,<br>prima di passare al successivo.<br>Valore espresso in secondi (es. -2 o 8) |
| ssml_switch           | bool      | Optional      | input_boolean<br>alexa_ssml | **1** / **True** / **On** / **Yes**<br>By-pass switch SSML. Attiva o disattiva la modalità [SSML][SSML]|
| audio                 | string      | Optional      | None | File audio da riprodurre. [see below examples Alexa](#examples-alexa) |
| language              | string      | Optional      | input_select<br>language | Il formato è xx-XX (es. en-GB) vedi tabella lingue supportate |
| rate                  | float      | Optional      | input_number<br>alexa_prosody_rate | valore min **20** max **200** |
| pitch                 | float      | Optional      | input_number<br>alexa_prosody_pitch | valore min **-33.3** max **50** |
| ssml_volume           | float      | Optional      | input_number<br>alexa_prosody_volume | valore min **-50** max **4.08** |
| voice                 | string      | Optional      | input_select<br>alexa_voice | Vedi tabella voci supportate |
| whisper               | bool      | Optional      | False | **1** / **True** / **On** / **Yes**<br>parla sottovoce |
| notifier              | string      | Optional      | alexa_media | Services Alexa |
| media_content_id      | string      | Optional      | None | Es. amzn_sfx_doorbell_chime_01, Alexa.GoodMorning.Play |
| media_content_type    | string      | Optional      | None | sound, sequence, image, TUNEIN, AMAZON_MUSIC, SPOTIFY, APPLE_MUSIC ... |

#### Examples Alexa
<details>
<summary>How to use parameters - Click to expand</summary>

##### Activate alexa and send a custom message only for Alexa
```yaml
alexa:
  message_tts: Speak only Alexa
```
##### Activate Alexa and send the same message as the text notifications.
```yaml
message: Primary message for text notifications.
alexa:
  mode: True
```
##### If there is a primary message for notifications or a custom message for Alexa, you don't need to use mode.
```yaml
alexa:
  wait_time: 0
  push: true
  title: Segnale Orario
  message: >
    Cucù! Sono le {{now().strftime("%H:%M")}},  accipicchia! 
  audio: soundbank://soundlibrary/foley/amzn_sfx_clock_ticking_01
```
##### In this example, you need the [sensor.last_alexa](#Utility) and see [Amazon Sounds][AmazonSounds]
```yaml
alexa: 
  message_tts: "Attenzione! Allerta Temporali"
  media_player: Last Alexa
  audio: >
   <audio src="soundbank://soundlibrary/weather/thunder/thunder_01"/>
```
##### Send tts and push message at the same time
```yaml
alexa:
  message_tts: Alpha one-two, this is X-ray two-three, ROGER, OUT
  push: true
```
##### How to use language and voice-id
```yaml
alexa:
  message: "Houston, we have a problem! "
  language: en-US
  voice: Matthew
```
```yaml
alexa:
  message: "Houston, we have a problem, here!"
  language: en-US
  voice: Joey 
```
##### How to use prosody and whisper
```yaml
alexa:
  message: >
    Parlo piano e a bassa voce. Sono le 11 Buonanotte e sogni d'oro!
  whisper: true
  rate: 80
  ssml_volume: 4.1
  type: tts
  volume: 0.4
```
##### For now, the media content is out of the message queue. There is no way to know the duration or the end of the playback
```yaml
alexa:
  media_content_id: Alexa.GoodMorning.Play
  media_content_type: sequence
  media_player: studio, last alexa
```
```yaml
alexa:
  media_content_id: Alexa.FlashBriefing.Play
  media_content_type: sequence
  notifier: alexa_media_sala
```
</details>

#### Google

| Options               | Type      | Requirement   | Default   | Description |
| --------------------- | --------- | -----------   | -------   | ----------- |
| mode                  | bool      | Required      | Optional  | True per attivare Google senza parametri aggiuntivi |
| message_tts           | string      | Optional      | Message | Messagio alternativo a quello principale |
| volume                | float     | Optional      | None  | Volume con un valore compreso tra 0 a 1 (es. 0.9) |
| media_content_id      | float     | Optional      | None  | xxxxxxx |
| media_content_type    | string      | Optional      | None | xxxxxxx |

#### Examples Google
<details>
<summary>How to use parameters - Click to expand</summary>

</details>

# [Lovelace][lovelace]

# Utility

Qui trovi altri sensori non strettamente correlati con il package, me che utilizzo in alcune automazioni di esempio.

<details>
<summary>Click to expand</summary>

#### Sensor Home Assistant Start

```yaml
sensor:
  - platform: command_line
    name: HA Start
    command: grep -m1 'Home Assistant initialized' home-assistant.log | awk '{ print $6, $7, $8, $9, $10 }'
############################################################################
## In order to use sensor.ha_start, set the info logs in this way
############################################################################
logger:
  default: warn
  logs:
    homeassistant.bootstrap: info
```

#### Altro... hacs?

```yaml
binary_sensor:
  # Binary sensor People at Home based on the group.location_tracker
```

#### [Sensor Last Alexa][LastAlexa]

```yaml
  # Old and Classic Last Alexa sensor
  - platform: template
    sensors:
      last_alexa:
        value_template: >
          {{ states.media_player | selectattr('attributes.last_called','eq',True) | map(attribute='entity_id') | first }}

  # Sensor Last Alexa based on the group.media_player_alexa (see hub extra)
  - platform: template
    sensors:
      last_alexa:
        value_template: >
          {{ expand(states.group.media_player_alexa) | selectattr('attributes.last_called','eq',True) | map(attribute='entity_id') | first }}
```

#### altro...

```yaml
test test
```
</details>


# [Automations Examples][Automation]

<details>
<summary>Click to expand</summary>

```yaml
  #----------------------------------------------------------------------------------------------------#
  # Home Assistant Start/Final Write/Close/Stop/Restart
  #----------------------------------------------------------------------------------------------------#
  - alias: Notifica di avvio
    description: 'notifiche Home Assistant_hub'
    initial_state: true
    mode: queued
    max_exceeded: silent
    trigger:
    - platform: homeassistant
      event: start
    - platform: homeassistant
      event: shutdown
    - platform: event
      event_type: homeassistant_final_write
    - platform: event
      event_type: homeassistant_close
    - platform: event
      event_type: call_service
      event_data:
        domain: homeassistant
        service: restart
    variables:
      notification_service: "{{states('input_select.text_notify')|lower}}"
    action:
    - variables:
        title: '{{trigger.description|regex_replace(find="\W|_|event", replace=" ")|trim|capitalize}}'
        time: "{{(now().time()|string)[:-4]}}"
        icon: >
          {% if 'stop' in title %}🛑
          {% elif 'final' in title %}🛡️
          {% elif 'close' in title %}⛔
          {% elif 'start' in title %}👍
          {% else %}📞
          {% endif %}
    - choose:
      - conditions: "{{title is defined}}"
        sequence:
          - service: "notify.{{notification_service}}"
            data:
              title: "{{icon}} {{title}}"
              message: |
                ➡️ {{time}}
          - choose:
            - conditions: "{{'start' in title}}"
              sequence:
                - service: homeassistant.update_entity
                  entity_id: sensor.ha_start
                - wait_for_trigger:
                    - platform: state
                      entity_id: sensor.centro_notifiche
                      to: 'on'
                  timeout: 60
                  continue_on_timeout: true
                - service: script.my_notify
                  data:
                    title: "HomeAssistant Start!"
                    notify: "{{notification_service}}"
                    message: |
                      Centro Notifiche operativo! 👍
                      {{states('sensor.ha_start')}}
                    alexa:
                      message_tts: >-
                        Il sistema è operativo!.
                      voice: Giorgio
                      type: tts
                    google: 
                      media_content_id: https://actions.google.com/sounds/v1/cartoon/cartoon_boing.ogg
                      # Examples sound library https://developers.google.com/assistant/tools/sound-library
```
```yaml
  #----------------------------------------------------------------------------------------------------#
  # Accesso Fallito # Banned IP persistent_notification.ip_ban title: Banning IP address
  # message: Too many login attempts from xxx.xxx.xxx.xxx
  #----------------------------------------------------------------------------------------------------#
  - alias: "Accesso fallito"
    mode: queued
    initial_state: true
    trigger:
      - platform: state
        entity_id: persistent_notification.http_login
    condition: "{{trigger.to_state.state != 'None' and trigger.to_state.entity_id is defined}}"
    action:
      - service: script.my_notify
        data:
          title: "⛔ Home Assistant Accesso Fallito. "
          message_tts: &tts_login "Attenzione. Accesso Fallito"
          message: "Tentativo di accesso o richiesta con autenticazione non valida."
          link: >-
            {% set message = state_attr('persistent_notification.http_login','message') %}
            {{'http://www.ip-tracker.org/locator/ip-lookup.php?ip=' ~ message.split('from ')[1] if message }}
          notify: alert
          priority: 1
          alexa:
            message_tts: *tts_login
          google:
            message_tts: *tts_login
```
```yaml
notify: False
alexa:
  message: "Houston, we have a problem! "
  language: en-US
  voice: Matthew
```
```yaml
alexa:
  message: "Houston, we have a problem, here!"
  language: en-US
  voice: Joey 
```
</details>


# Todos

 - Write MORE MORE AND MORE :O)
 - Add xx Mode

# FAQ

1. How can I quickly try sending notifications?<br>
    From dev tools see picture
2. I get the messages, but Alexa or google don't work<br>

License
----

MIT

[![N|Solid](https://avatars1.githubusercontent.com/u/24454580?s=400&u=4d6b36443980882e973bccdc4e1a280f7afdffda&v=4)](https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/wiki)

**Free Software**

<!-- AppDaemon Reference -->
[Notifier]: <https://github.com/jumping2000/notifier>
[AppDaemon]: <https://appdaemon.readthedocs.io/en/stable/index.html>
[Addon-AD]: <https://github.com/hassio-addons/repository>

<!-- Centro Notifiche Reference -->
[package]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/>
[Secret]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/secrets.yaml>
[HubMain]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/centro_notifiche/hub_main.yaml>
[HubAlexa]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/centro_notifiche/hub_alexa.yaml>
[HubGoogle]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/centro_notifiche/hub_google.yaml>
[HubBuild]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/centro_notifiche/hub_build_message.yml>
[HubExtra]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/packages/centro_notifiche/hub_extra.yaml>
[Automation]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/examples/hub_automations.yaml>
[lovelace]: <https://github.com/caiosweet/Package-Notification-HUB-AppDaemon/tree/master/lovelace/>

<!-- Amazon Alexa Reference -->
[AmazonSounds]: <https://developer.amazon.com/it-IT/docs/alexa/custom-skills/ask-soundlibrary.html>
[SSML]: <https://developer.amazon.com/it-IT/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#about-ssml>

<!-- Home Assistant Reference -->
[TimeDate]: <https://www.home-assistant.io/integrations/time_date/>
[Workday]: <https://www.home-assistant.io/integrations/workday/>
[TTS]: <https://www.home-assistant.io/integrations/tts/>
[GTranslate]: <https://www.home-assistant.io/integrations/google_translate/>
[StateObj]: <https://www.home-assistant.io/docs/configuration/state_object/>

<!-- Alexa Media Reference -->
[LastAlexa]: <https://github.com/custom-components/alexa_media_player/wiki#creating-sensorlast_alexa>

<!-- Addons -->
[GAssistant1]: <https://github.com/AndBobsYourUncle/hassio-addons>
[GAssistant2]: <https://github.com/marcelveldt/hassio-addons-repo/tree/master/google-assistant-webserver>
[GAssistant3]: <https://github.com/Apipa169/Assistant-Relay-for-Hassio>
[DssVoip]: <https://github.com/sdesalve/hassio-addons/tree/master/dss_voip>

<!-- Others -->
[Callmebot]: <https://www.callmebot.com/telegram-call-api/>

<!-- Template -->
[Lentron]: <https://community.home-assistant.io/t/janet-the-good-place/38904>
[CCOSTAN]: <https://github.com/CCOSTAN/Home-AssistantConfig/blob/master/config/script/speech_engine.yaml>
[mf-social]: <https://github.com/mf-social/Home-Assistant/blob/master/homeassistant/packages/interactive/notifications.yaml>
[3vasi0n89]: <https://github.com/3vasi0n89/home-assistant-config-files/blob/master/packages/notification_center.yaml>
[happyleavesaoc]: <https://github.com/happyleavesaoc/my-home-automation/blob/master/homeassistant/packages/briefings.yaml>
