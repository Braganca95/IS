from xml.dom.minidom import parse 
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("C:\\xampp\\htdocs\\IS_TP1_PHP\\REST\\DOM\\files\\books.xml")
livros = DOMTree.documentElement

livro = getElementsByTagName("book")

nlivro = 1
for obra in livro:
    print("LIVRO nº: ",nlivro)
    nlivro = nlivro + 1
    if obra.hasAttribute("author"):
        print("Autor: %s" % obra.getAttribute("author"))
    titulo = obra.getAttribute("title")[0]
    print("titulo: %s" % titulo.childNodes[0].data)
    genero = obra.getAttribute("genre")[0]
    print("género: %s" % genero.childNodes[0].data)
    preco = obra.getAttribute("price")[0]
    print("preço: %s" % preco.childNodes[0].data)
    data = obra.getAttribute("publish_date")[0]
    print("data: %s" % data.childNodes[0].data)
    descr = obra.getAttribute("description")[0]
    print("descrição: %s" % descr.childNodes[0].data)
