noopt = ("dom/base", "dom/html", "dom/events", "docshell")

if RELATIVEDIR.startswith(noopt):
    COMPILE_FLAGS["OPTIMIZE"] = []
