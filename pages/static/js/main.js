const form=document.querySelector('.hizmet')
form.numb.addEventListener('keyup',function (e) {
    desen=/^[0-9 ]{9,20}$/
    form.numb.style.outline='none'
    if(desen.test(e.target.value)){
        form.numb.setAttribute('class','basarli')
        console.log("dogry");
    }
    else{
        form.numb.setAttribute('class','hatali')
        console.log("yanliş");
    }
})