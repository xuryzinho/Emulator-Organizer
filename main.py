from shutil import unpack_archive,move
from pathlib import Path
from time import sleep
from rarfile import RarFile
import py7zr

class Organizer:
    def __init__(self,inp_dir):
        self.inp_dir = Path(inp_dir)
        self.download_dir = Path().home() / "Downloads"

    def creatingFolders(self):        
        with open("./folders.txt","r") as file:
            # Removendo o "\n"

            for lineb in file:
                line = lineb.rstrip()
                new_folder = self.inp_dir / line 
                
                if not Path.exists(new_folder):
                    new_folder.mkdir(parents=True,exist_ok=False)
                    print(new_folder)

    def unzip_game(self):
        for game in self.download_dir.iterdir():
            while True:
                if ".part" in game.suffix and game.exists():
                    print(".part in download")
                    print(game)
                    sleep(10)
                else:
                    break

        for game in self.download_dir.iterdir():
            if ".part" in game.suffix:
                while True:
                    print(".part in download")
                    print(game)
                    sleep(10)

            elif ".zip" in game.suffix:
                unpack_archive(game,self.inp_dir / "Games")
                print(f"unpack - {game}")

                game.unlink()
                print(f"delete - {game}")
            
            elif ".rar" in game.suffix:
                print(game)
                rf = RarFile(game)
                rf.extractall(self.inp_dir / "Games")
                rf.close()
                print(f"unpack - {game}")
                    
                game.unlink()
                print(f"delete - {game}")

            elif ".7z" in game.suffix:
                print(f"unpack - {game}")

                file7z = py7zr.SevenZipFile(game,mode="r")
                file7z.extractall(self.inp_dir / "Games") 

                game.unlink()
                print(f"delete - {game}")

    def move_games(self):
        games_dir = self.inp_dir / "Games"
        emulators_dir = self.inp_dir / "Emulators"

        for game in games_dir.iterdir():
            match (game.suffix):
                case ".gb":
                    file = emulators_dir / "GameBoy" / game.name
                    print(f"Moving {game} -> {file}") # mover para /gameboy
                    move(game,file)
                case ".gba" | ".GBA":
                    file =  emulators_dir / "GBA" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Atari/Atari 2600
                    move(game,file)         
                case ".gbc" | ".GBC":
                    file =  emulators_dir / "GBColor" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Atari/Atari 2600
                    move(game,file)
                case ".nes":
                    file = emulators_dir /"NES" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /nes
                    move(game,file)                    
                case ".smc" | ".sfc":
                    file = emulators_dir /"SNES" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /snes
                    move(game,file)
                case ".z64" | ".n64":
                    file =  emulators_dir / "N64" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /N64
                    move(game,file)
                case ".a26":
                    file =  emulators_dir / "Atari/Atari 2600" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Atari/Atari 2600
                    move(game,file)
                case ".a52":
                    file =  emulators_dir / "Atari/Atari 5200" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Atari/Atari 5200
                    move(game,file)
                case ".a78":
                    file =  emulators_dir / "Atari/Atari 7800" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Atari/Atari 7800
                    move(game,file)
                case ".wbfs":
                    file =  emulators_dir / "Wii" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Wii
                    move(game,file)
                case ".md":
                    file =  emulators_dir / "Genesis" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Genesis
                    move(game,file)
                case ".nds":
                    file =  emulators_dir / "Nintendo DS" / game.name
                    print(f"Moving - {game} -> {file}") # mover para /Nintendo DS
                    move(game,file)

def run():
    o = Organizer("/data/sata/IKONOS")

    while True:
        o.creatingFolders()
        o.unzip_game()
        o.move_games()

        sleep(3)

run()