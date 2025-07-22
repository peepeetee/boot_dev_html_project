

def extract_title(markdown):
    for line in markdown:
        if line.startswith(("# ")):
            return 