from shutil import unpack_archive,move
from pathlib import Path
from utils.check_files import check_type_game
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
        # Checando se possui algum arquivo download.part
        for game in self.download_dir.iterdir():
            while True:
                if ".part" in game.suffix and game.exists():
                    print(f"{game} in download")
                    sleep(10)
                else:
                    break
        
        for game in self.download_dir.iterdir():
            if ".zip" in game.suffix:
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
            check_type_game(emulators_dir,game)

def run():
    o = Organizer("/data/sata/IKONOS")

    while True:
        o.creatingFolders()
        o.unzip_game()
        o.move_games()

        sleep(3)

run()