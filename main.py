def process_line(line):
    # Eliminamos espacios en blanco al inicio y final
    line = line.strip()
    if not line:
        return 0

    valid_chars = "0123456789.-"
    cleaned = "".join(c for c in line if c in valid_chars)
    
    # Manejo de casos donde queda un string vacío o solo símbolos
    if not cleaned or cleaned == "." or cleaned == "-" or cleaned == ".-":
        return 0
    
    try:
        # Truncamos a entero como pide el reto
        return int(float(cleaned))
    except ValueError:
        return 0