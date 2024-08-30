import webbrowser

def search_for_person_in_txt_file(*txt_files: tuple[str, ...]) -> None:
    for file in txt_files:
        # Use with statement to ensure the file is properly closed
        with open(file, "r") as f:
            # Iterate over each line in the file
            for line in f:
                # Strip leading/trailing whitespace from the line
                name = line.strip()
                
                if name:  # Check if the line is not empty
                    # Construct a search URL
                    query = f"https://www.google.com/search?q=linkedin+{name.replace(' ', '+')}"
                    # Open the search query in a new browser tab
                    webbrowser.open_new_tab(query)

# place the script along with the files
# specify file names
search_for_person_in_txt_file("<file name>.txt", "<file name>.txt")
# don't forget to pray for your RAM
