import os, shutil, random, json, sys, getopt

user_path = os.path.expanduser('~')
working_dir = os.path.abspath('.')
destination_dir = os.path.join(user_path, 'Podcasts', 'Phone')
quantity = 5
allowed_formats = ('.mp3', '.mp4')
savefile = 'pickrandom.json'

def load_args():
    global working_dir
    global destination_dir
    global quantity

    try:
        options, args = getopt.getopt(sys.argv[1:],'hn:i:d:')
    except getopt.GetoptError as err:
        print(err)
        print('Usage: PickRandom [-h] [-n quantity] [-i "/input/dir"] [-d "/destination/dir"]')
        sys.exit(2)

    for option, arg in options:
        if option == '-h':
            print('Usage: PickRandom [-h] [-n quantity] [-i "/input/dir"] [-d "/destination/dir"]')
            sys.exit()
        elif option == '-n':
            quantity = int(arg)
        elif option == '-i':
            if arg != '.':
                working_dir = arg
            else:
                working_dir = os.path.abspath('.')
        elif option == '-d':
            if arg != '.':
                destination_dir = arg
            else:
                destination_dir = os.path.abspath('.')

def pick_files(filelist, last_picks, quantity):
    picked_files = []
    count = 0

    while count < quantity:
        random_int = random.randint(0, len(filelist) - 1)
        file = filelist[random_int]
        picked_before = False

        if file.endswith(allowed_formats):
            if len(last_picks) > 0:
                for item in last_picks:
                    if item == file:
                        picked_before = True
                        break

            if len(picked_files) > 0:
                for item in picked_files:
                    if item == file:
                        picked_before = True
                        break

            if not picked_before:
                print(f'{file} was picked!')
                picked_files.append(file)
                count += 1

    return picked_files

def copy_files(filelist):
    for file in filelist:
        print(f'Copying {file} to {destination_dir}')
        filepath = os.path.join(working_dir, file)
        shutil.copy(filepath, destination_dir)
    print('\nDone!')

def save_data(picked_files):
    with open(savefile, 'w') as file:
        file.write(json.dumps(picked_files))

    print('Save successful!')

def load_data():
    if os.path.isfile(savefile):
        print(f"Savedata found!")
        with open(savefile, 'r') as file:
            last_picked_files = json.load(file)

        return last_picked_files

    print("No savedata found...")
    return []

def main():
    load_args()
    filelist = os.listdir(working_dir)

    if len(filelist) - 2 >= quantity:
        last_picks = load_data()
        valid_files = (len(filelist) - 2) - len(last_picks)
        if valid_files >= quantity:
            picked_files = pick_files(filelist, last_picks, quantity)
            copy_files(picked_files)

            save_data(picked_files)
        else:
            print(f"Not enough files to pick in the directory, try asking for {valid_files} file(s).")
    else:
        print("Not enough files to pick in the directory...")

main()
