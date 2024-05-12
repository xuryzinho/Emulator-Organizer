# Import librarie

from shutil import move

# OBS: Jogos mais atuais geralmente vem em .iso ou em formatos diferentes

def check_type_game(emulators_dir,game):
    match (game.suffix):
        case ".gb":
            file = emulators_dir / "GameBoy" / game.name
        case ".gba" | ".GBA":
            file =  emulators_dir / "GBA" / game.name
        case ".gbc" | ".GBC":
            file =  emulators_dir / "GBColor" / game.name
        case ".nes":
            file = emulators_dir /"NES" / game.name
        case ".smc" | ".sfc":
            file = emulators_dir /"SNES" / game.name
        case ".z64" | ".n64":
            file =  emulators_dir / "N64" / game.name
        case ".a26":
            file =  emulators_dir / "Atari/Atari 2600" / game.name
        case ".a52":
            file =  emulators_dir / "Atari/Atari 5200" / game.name
        case ".a78":
            file =  emulators_dir / "Atari/Atari 7800" / game.name
        case ".wbfs" | ".rvz" | ".gcz":
            file =  emulators_dir / "Wii" / game.name
        case ".md":
            file =  emulators_dir / "Genesis" / game.name
        case ".nds":
            file =  emulators_dir / "Nintendo DS" / game.name
        case ".3ds":
            file =  emulators_dir / "Nintendo 3DS" / game.name
        case ".wux":
            file =  emulators_dir / "Wii U" / game.name
            
    print(f"Moving - {game} -> {file}") # mover para /Wii U
    move(game,file)
