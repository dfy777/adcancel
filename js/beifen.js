$(document).ready(function(){
    try{
        //alert("start");
        var ad_class = document.getElementsByClassName("jjjjasdasd");
        var len = ad_class.length;

        for (var i = 0; i < len; i++) {
            ad_class[i].style.display="none";
        }
    }catch(e){
        //alert(e);
    }

    try{
        var ad_id = document.getElementById("HMRichBox");
        ad_id.style.display="none";
    } catch(e){
        
    }
});