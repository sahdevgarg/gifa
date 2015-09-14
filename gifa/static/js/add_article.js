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
    if (img_width > '400' && img_height > '200' )
    {
       image_upload = true
    }
    else
    {
      $('#myImg').attr('src', no_image_src);
      alert("Please upload the image with minimum dimension 400 X 200")

    }
};

function validateForm(){
    var title = $("#textinput").val();
    var content_words = parseInt($("#mceu_33").text().replace("Words: ",""));
    var title_count = parseInt($("#count").text());
    var team1 = $("#team1").val();
    var team2 = $("#team2").val();
    if (title.length < 20)
    {
      alert(" Minimum title length should be 20")
      return false
    }
    else if (title.length > 140)
    {
      alert(" Maximum title length should be 140")
      return false
    }
    else
    {
      if(content_words< 20)
      {
        alert("News article should have atleast 20 words")
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
          if(!team1)
          {
            alert("please select a team")
            return false
          }
          else if (team1 == team2)
          {
            alert("Please select different teams")
            return false
          }
          else
          {
            return true
          }
        }
      }
    }
  }
  $(document).ready(function() {
  $(".select_box").select2();
  tinymce_init()
});
