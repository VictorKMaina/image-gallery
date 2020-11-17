$(document).ready(function(){
    $(".grid-image").click(function(){
        $("#imageModal").modal('toggle')
    })

    $(".grid-image").click(function(){
        $(".alert#copied").hide()
        $("button#copy-link").click(function(){
            let imageLink = $("input#image-link");
            imageLink.select();
            document.execCommand("copy");
            $(".alert#copied").show()
        })
    })
})