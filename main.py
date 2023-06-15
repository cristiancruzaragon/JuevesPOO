from cosas import Libro,Autor,Alumno


def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Cristian","Cruz"), 1980)
    print(l1)
    #el codigo para cambiar el pseudocodigo
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("-----------Herencia-----------")
    al2 = Alumno("Jose",19,312234,"ICO",9)
    al2.nombre = "PEPE"
    print(vars(al2))

main()