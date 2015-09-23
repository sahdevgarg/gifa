window.onload = function() {
var i = document.getElementById("textinput");
var c = document.getElementById("count");
c.innerHTML = 0
i.addEventListener("keydown",count);
function count(e){
    var len =  i.value.length;
       c.innerHTML = len;
}
}
$(function () {
    $(":file").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = imageIsLoaded;
            reader.readAsDataURL(this.files[0]);
        }
    });
});

function imageIsLoaded(e) {
    no_image_src = $('#myImg').attr('src')
    $('#myImg').attr('src', e.target.result);
    img_width = $('#myImg').width();
    img_height = $('#myImg').height();
    var fsize = $("#image-file")[0].files[0].size / 1024

    if (img_width > '200' && img_height > '100')
    {
      if (fsize < 1000)
      {
       image_upload = true
      }
      else
      {
        $("#image-file").val('')
        $('#myImg').attr('src', no_image_src);
        alert("Please upload the image of maximum file size upto 1mb")
      }
      
    }
    else
    {
      $("#image-file").val('')
      $('#myImg').attr('src', no_image_src);
      alert("Please upload the image with minimum dimension 200 X 100")

    }
}

function validateForm(){
    var title = $("#textinput").val();
    var content_words = parseInt($("#mceu_33").text().replace("Words: ",""));
    var title_count = parseInt($("#count").text());
    var team1 = $("#team1").val();
    var team2 = $("#team2").val();
    if (title.length < 10)
    {
      alert(" Minimum title length should be 10")
      return false
    }
    else if (title.length > 255)
    {
      alert(" Maximum title length should be 255")
      return false
    }
    else
    {
        if (!image_upload)
        {
          alert("Please upload the cover image");
          return false
        }
        else
        {
            return true
        }
      }
  }

 $(document).ready(function() {
  $(".select_box").select2();
//   $('#i_submit').click( function() {
//     //check whether browser fully supports all File API
//     if (window.File && window.FileReader && window.FileList && window.Blob)
//     {
//         //get the file size and file type from file input field
//         var fsize = $('#i_file')[0].files[0].size;
        
//         if(fsize>1048576) //do something if file size more than 1 mb (1048576)
//         {
//             alert(fsize +" bites\nToo big!");
//         }else{
//             alert(fsize +" bites\nYou are good to go!");
//         }
//     }else{
//         alert("Please upgrade your browser, because your current browser lacks some new features we need!");
//     }
// });
});