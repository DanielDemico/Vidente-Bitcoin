const desc = document.querySelectorAll(".descricao");
function mostrarDesc(num){
    
    if (num == 0){
        desc[0].style.display = "block";
    } else if ( num == 1 ){
        desc[1].style.display = "block";
    } else if ( num == 2 ){
        desc[2].style.display = "block";
    } else if ( num == 3 ){
        desc[3].style.display = "block";
    }
}
function tirarDesc(num){
    if (num == 0){
        desc[0].style.display = "none";
    } else if ( num == 1 ){
        desc[1].style.display = "none";
    } else if ( num == 2 ){
        desc[2].style.display = "none";
    } else if ( num == 3 ){
        desc[3].style.display = "none";
    }
}