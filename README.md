# Emulator-Organizer

Oi! Eu sou o Xury ou Victor para os mais íntimos, e vim explicar como funciona o Emulator Organizer que criei. O Emulator Organizer foi concebido com a ideia de organizar os meus jogos de emulador. Ele não é muito complexo, então será bem rápido de explicar.

Vamos por tópicos:

## Criação de pastas

Quando você baixa o Emu-Or pela primeira vez, ele solicita que você escolha um diretório. Esse diretório será onde ele criará duas pastas: "/Game" e "/Emulators". A pasta "/Game" será onde alguns jogos ficarão após serem extraídos, e a pasta "/Emulators" será onde os emuladores serão armazenados. Ao escolher um diretório, o Emu-Or criará várias pastas de acordo com os diretórios listados no arquivo "folders.txt". 

Exemplo:

![image](https://github.com/ryuxinn/Emulator-Organizer/assets/82833077/7775b711-4741-43e3-a4f2-8139b233897c)


![image](https://github.com/ryuxinn/Emulator-Organizer/assets/82833077/d16ddb4c-f7f8-45dc-8610-0f556e1c681c)


## Extração de arquivos

Como mencionado no primeiro tópico, a extração de arquivos funciona da seguinte maneira: após as pastas "/Game" e "/Emulators" serem criadas, os jogos serão extraídos na pasta "/Game", o arquivo zip será apagado e, em seguida, movidos para suas respectivas pastas.

Exemplo: 

![image](https://github.com/ryuxinn/Emulator-Organizer/assets/82833077/3c3385bc-e2ee-4769-be41-fd29d3185dcc)


## Compatibilidade

O Emu-Or foi escrito em Python, utilizando a biblioteca pathlib e outros módulos. O pathlib é capaz de identificar diretórios tanto em sistemas Linux quanto Windows sem problemas, o que significa que tanto Linux quanto Windows podem executar o Emu-or sem dificuldades.

