# Emulator-Organizer

Oi! Eu sou o Xury ou Victor para os mais íntimos, e vim explicar como funciona o Emulator Organizer que criei. O Emulator Organizer foi concebido com a ideia de organizar os meus jogos de emulador. Ele não é muito complexo, então será bem rápido de explicar.

Vamos por tópicos:

## Criação de pastas

Quando você baixa o Emu-Or pela primeira vez, ele solicita que você escolha um diretório. Esse diretório será onde ele criará duas pastas: "/Game" e "/Emulators". A pasta "/Game" será onde alguns jogos ficarão após serem extraídos, e a pasta "/Emulators" será onde os emuladores serão armazenados. Ao escolher um diretório, o Emu-Or criará várias pastas de acordo com os diretórios listados no arquivo "folders.txt". 

Exemplo:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b1ece91-e147-4146-8e5c-3c5d151fb553/60825d17-6239-487d-b061-6aa6a4ac983f/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b1ece91-e147-4146-8e5c-3c5d151fb553/0938e408-4966-4fa7-81dd-c4d7afefb54d/Untitled.png)

## Extração de arquivos

Como mencionado no primeiro tópico, a extração de arquivos funciona da seguinte maneira: após as pastas "/Game" e "/Emulators" serem criadas, os jogos serão extraídos na pasta "/Game", o arquivo zip será apagado e, em seguida, movidos para suas respectivas pastas.

Exemplo: 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b1ece91-e147-4146-8e5c-3c5d151fb553/f5e27b3e-897a-45aa-a569-e132f37cb7ac/Untitled.png)

## Compatibilidade

O Emu-Or foi escrito em Python, utilizando a biblioteca pathlib e outros módulos. O pathlib é capaz de identificar diretórios tanto em sistemas Linux quanto Windows sem problemas, o que significa que tanto Linux quanto Windows podem executar o Emu-or sem dificuldades.

