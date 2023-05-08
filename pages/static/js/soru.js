const text=document.getElementById('content')
const buton=document.getElementById('sorag')
const info_text=document.querySelector('.info-text')
console.log(info_text)
text.addEventListener('keyup',function(e){
     girilen=e.target.value
     text.style.outline='none'
     
     console.log(girilen.length)
     if(girilen.length>5){
       text.setAttribute('class','basarli')
       buton.disabled=false
       info_text.classList.add('d-none')

     }
     else{
        text.setAttribute('class','hatali')
        buton.disabled=true
        info_text.classList.remove('d-none')
     }
})