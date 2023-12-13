const initSlider = () => {
    const slideButtons=document.querySelectorAll(".slider-wrapper .slide-button");
    const imageList=document.querySelector(".slider-wrapper .image-list");

    slideButtons.forEach(button=>{
        button.addEventListener("click", () => {
           const direction= button.id === "prev-slide" ? -1 : 1;
           const scrollAmount= 360*direction;

           imageList.scrollBy({ left: scrollAmount, behavior: "smooth" });
           console.log(imageList.scrollLeft);
           if(imageList.scrollLeft >= imageList.clientWidth-360)
             imageList.scrollLeft=0;
           
           });
    });
    setTimeout(MetotStart,1000)
    
    
    
    function MetotStart(){
        imageList.scrollBy({ left: 360, behavior: "smooth" });
        console.log(imageList.scrollLeft);
       
        if(imageList.scrollLeft >= imageList.clientWidth-360)
            imageList.scrollLeft=0;
        setTimeout(MetotStart,3000)
    }

}
window.addEventListener("load", initSlider);
    
