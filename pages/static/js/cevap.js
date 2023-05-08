const text=document.getElementById('cevap_text')
const info_text=document.querySelector('.info_text')
const btn=document.getElementById('cevap_btn')

text.addEventListener('keyup',function(e){
    text.style.outline="none"
    if(e.target.value.length>5){
        text.setAttribute('class','basarli')
        btn.disabled=false
        info_text.classList.add('d-none')
    }
    else{
        text.setAttribute('class','hatali')
        btn.disabled=true
        info_text.classList.remove('d-none')
    }
})