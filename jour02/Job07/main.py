def langage(programming):
    match programming:
        case "javascript":
            print("Tu es un développeur web")
        case "python":
            print("Tu es un développeur IA")
        case "java":
            print("Tu es un développeur logiciel")
        case "reactjs":
            print("Tu es un développeur mobile")
        case _:
            print("Un jour,je serai le meilleur développeur...")

langage("javascript")
langage("python")
langage("java")
langage("reactjs")
langage("scratch")