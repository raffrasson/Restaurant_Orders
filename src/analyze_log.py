def analyze_log(path_to_file):
    try:
        open(path_to_file, encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
