def snake_case(string: str):
    string = string.lower()
    string = string.replace('.', '')
    string = string.replace(' ', '_')
    return string