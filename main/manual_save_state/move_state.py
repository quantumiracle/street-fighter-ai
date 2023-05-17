import shutil
import os
import retro

def print_game_lib_folder():
    retro_directory = os.path.dirname(retro.__file__)
    game_dir = "data/stable/StreetFighterIISpecialChampionEdition-Genesis"
    retro_state_path = os.path.join(retro_directory, game_dir)
    return retro_state_path


def copy_move_file(name):
    # specify the path of the file to be copied
    source_path = name

    # specify the path where the file will be copied to
    destination_path = print_game_lib_folder()

    # copy the file from source to destination
    shutil.copy(source_path, destination_path)



if __name__ == "__main__":
    copy_move_file('Champion.Level1.RyuVsRyu.2Player-3.state')