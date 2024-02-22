const imgButton = document.getElementById("imgButton")
const imgModal  = document.getElementById("showModal")
const buttonCloseModal = document.getElementById("close_modal");

function showModal(){
    imgModal.style.display = "flex";
    document.body.style.overflow = "hidden";
}

function closeModal(){
    imgModal.style.display = "none";
    document.body.style.overflow = "visible";
}

imgButton.addEventListener("click", showModal)
buttonCloseModal.addEventListener("click", closeModal)
