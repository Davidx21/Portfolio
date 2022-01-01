AOS.init();
var url = String(window.location); //Covertir Object a String

function urlActual(){
    if (url.includes("about")){
        document.getElementById("aboutLink").style.borderBottom = "solid 2px"
    }
    else if (url.includes("work")){
        document.getElementById("workLink").style.borderBottom = "solid 2px"
    }
    else if (url.includes("contact")){
        document.getElementById("contactLink").style.borderBottom = "solid 2px"
    }
    else if (url.includes("art")){
        document.getElementById("artLink").style.borderBottom = "solid 2px"
    }
    else{
        document.getElementById("homeLink").style.borderBottom = "solid 2px"
    }
}

urlActual()