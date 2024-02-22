const alarmButton = document.getElementById("notice_hidden")
const alarm = document.getElementById("alarm")
function alarm_hide(event){
    if(event.currentTarget.checked){
        alarm.classList.add("hidden")
    }else{
        alarm.classList.remove("hidden")
    }
    
}
alarmButton.addEventListener("click" ,alarm_hide)