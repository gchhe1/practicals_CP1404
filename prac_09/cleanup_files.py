import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # No solution is provided, but you may want to consider the patterns to look out for and fix
    # E.g. a lowercase letter followed by a capital, like "tN" should become "t_N"
    # Try doing this on paper first and then see if you can systematise it
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    characters = list(filename)
    if "_" not in new_name:
        for index, character in enumerate(characters):
            # TODO: rewrite to avoid repeated "and"
            if character.isupper() and characters[index-1].isalpha() and index > 0:
                characters.insert(index, "_")
    else:
        for index, character in enumerate(characters):
            if character == "_":
                characters[index+1] = characters[index+1].upper()
    filename = "".join(characters)
    new_name = filename
    return new_name


main()
