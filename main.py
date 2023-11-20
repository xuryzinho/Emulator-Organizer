from shutil import unpack_archive,move
from pathlib import Path
from utils.check_files import check_type_game
from time import sleep
from rarfile import RarFile
import py7zr


class Organizer:
    def __init__(self):
        self.inp_dir = Path(str(Path("./dirs/directory.txt").read_text()).rstrip()) # Retornando o diretorio do arquivo ./dirs/directory.txt e quebrando as linhas do mesmo
        self.download_dir = Path().home() / "Downloads"

    def checkDir(self):
        # Checando se diretorio passado em ./dirs/directory.txt existe
        while True:
            if str(self.inp_dir) == "." or not self.inp_dir.exists():
                new_dir = input("Digite um diretorio: ")
                
                print(Path(new_dir))

                if not Path(new_dir).is_dir() or not Path(new_dir).exists():
                    print("Ocorreu um erro, digite novamente.")

                else:
                    WRITE_DIRECTORY = Path(__file__).parents[0] / "dirs/directory.txt"
                    WRITE_DIRECTORY.write_text(new_dir)
                    break
            else:
                break

    def creatingFolders(self):        
        with open("./dirs/folders.txt","r") as file:
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
            if ".part" in game.suffix and game.exists():
                print(f"{game} in download")
                sleep(10)   

            elif ".zip" in game.suffix:
                print(f"unpack - {game}")
                unpack_archive(game,self.inp_dir / "Games")

                game.unlink()
                print(f"delete - {game}")
            
            elif ".rar" in game.suffix:
                print(f"unpack - {game}")

                rf = RarFile(game)
                rf.extractall(self.inp_dir / "Games")
                rf.close()
                    
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
    o = Organizer()
    o.checkDir()
    o.creatingFolders()

    while True:
        o.unzip_game()
        o.move_games()

        sleep(3)

if __name__ == "__main__":
    run()
