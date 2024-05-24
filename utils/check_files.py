# Import librarie

from shutil import move

# OBS: Jogos mais atuais geralmente vem em .iso ou em formatos diferentes

def check_type_game(emulators_dir,game):
    match (game.suffix):
        case ".gb":
            file = emulators_dir / "GameBoy" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".gba" | ".GBA":
            file =  emulators_dir / "GBA" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".gbc" | ".GBC":
            file =  emulators_dir / "GBColor" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".nes":
            file = emulators_dir /"NES" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".smc" | ".sfc":
            file = emulators_dir /"SNES" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".z64" | ".n64":
            file =  emulators_dir / "N64" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".a26":
            file =  emulators_dir / "Atari/Atari 2600" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".a52":
            file =  emulators_dir / "Atari/Atari 5200" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".a78":
            file =  emulators_dir / "Atari/Atari 7800" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".wbfs" | ".rvz" | ".gcz":
            file =  emulators_dir / "Wii" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".md":
            file =  emulators_dir / "Genesis" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".nds":
            file =  emulators_dir / "Nintendo DS" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
        case ".3ds":
            file =  emulators_dir / "Nintendo 3DS" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)            
        case ".wux":
            file =  emulators_dir / "Wii U" / game.name
            print(f"Moving - {game} -> {file}")
            move(game,file)
