function checkPswd2(obj){
    const pswd1 = document.getElementById("pswd1")
    const pswd2 = document.getElementById("pswd2")
    const pswd_help = document.getElementById("pswd_help")
    const pswd2_text = obj.value
    if(pswd2_text!== pswd1.value)
    {   
        pswd_help.classList.remove("hidden")
    }else{
        pswd_help.classList.add("hidden")
    }
}