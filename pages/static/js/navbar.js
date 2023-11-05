//Düzenle sayfasi
const duzenlebtn=document.querySelector(".edtitProf")
const openpage=document.getElementById('id01')

const imgbox=document.querySelector('.imgbox')
const image=document.getElementById('myFile')
proiletext=document.querySelector('.profiltext')

if(duzenlebtn!=null){
    duzenlebtn.addEventListener("click", function () {
    
    openpage.style.display="block"
  })
}

//Kayit ol sayfasi
const yazil=document.querySelector('.yazil')
const kayitSayfa=document.getElementById('id02')
const kayitForm=document.getElementById('post-form')
const fname=document.getElementById('fname')
const lname=document.getElementById('lname')
const uname=document.getElementById('uname')
const psw=document.getElementById('psw')
const psw_confirim=document.getElementById('psw_confirim')
const csrf=document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

if(yazil!=null){
    yazil.addEventListener('click', function() {
        kayitSayfa.style.display="block"

        
        image.addEventListener('change',()=>{
            const image_date=image.files[0]
            const url=URL.createObjectURL(image_date)
            imgbox.innerHTML=`<img src="${url}" width=150px>`
            proiletext.style.display="none"
        })
        kayitForm.addEventListener('submit', function (e) {
            e.preventDefault()
            console.log("tiklandi")
           const fd=new FormData()
           fd.append('csrfmiddlewaretoken',csrf[0].value)
           fd.append('fname',fname.value)
           fd.append('lname',lname.value)
           fd.append('uname',uname.value)
           fd.append('psw',psw.value)
           fd.append('psw_confirim',psw_confirim.value)
           fd.append('image',image.files[0])
           console.log(fd)
           $.ajax({
                type:'POST',
                url:'/yazil',
                enctype:'multipart/form-data',
                data: fd,
                success: function (response){
                 console.log(response)
                },
                error: function(error){
                    console.log(error);
                },
                caches: false,
                contentType: false,
                processDate: false,
            })
        })
    })
}


