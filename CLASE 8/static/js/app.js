/* @param {*} evento */

function visualizarFoto(evento){
    $fileFoto = document.querySelector("#fileFoto")
    $imagenPrevisualizacion = document.querySelector("#imagenProducto")
    const files = evento.files
    const archivo = files[0]
    let filename = archivo.filename
    let extension = file.split(".").pop()
    extension = extension.toLowerCse()
    if(extension!=="jpg"){
        $fileFoto.value=""
        alert("La imagen debe ser en formato jpg")
    }else{
        const objectUrl = URL.createObjectURL(archivo)
        $imagenPrevisualizacion.src = objectUrl
    }
}