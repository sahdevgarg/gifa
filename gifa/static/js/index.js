// This is called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      testAPI();
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

  window.fbAsyncInit = function() {
  FB.init({
    appId      : '1439528452994485',
    cookie     : true,  // enable cookies to allow the server to access 
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.2' // use version 2.2
  });


  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // Here we run a very simple test of the Graph API after login is
  // successful.  See statusChangeCallback() for when this call is made.
  function testAPI() {
    FB.api('/me', function(response) {
      tinymce_init()
      document.getElementById('status').innerHTML =
        'Thanks for logging in, ' + response.name + '!';
    });
  }
function tinymce_init(){
    $("#my_editor").show();
    tinymce.init({
    selector: "#my_editor",
    theme: "modern",
    height : 300,
    plugins: [
        "advlist autolink lists link image charmap preview anchor pagebreak",
        "searchreplace wordcount visualblocks visualchars code fullscreen",
        "insertdatetime media nonbreaking save table directionality",
        " template paste textcolor colorpicker textpattern imagetools image"
    ],
    menubar: false,
    toolbar1: "undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | ",
    toolbar2: "preview | insertfile link image media | forecolor backcolor",
    image_advtab: true,
    theme_advanced_path : false,
    file_browser_callback: function(field_name, url, type, win) {
        if(type=='image') $('#my_form input').click();
    },
    templates: [
        {title: 'Test template 1', content: 'Test 1'},
        {title: 'Test template 2', content: 'Test 2'}
    ],

});

}

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
    $('#myImg').attr('src', e.target.result);
    img_width = $('#myImg').width();
    img_height = $('#myImg').height();
    console.log(img_width,img_height)
    if (img_width > '600' && img_height > '400' )
    {
       $('#myImg').attr('src', e.target.result);
    }
    else
    {
      alert("Please upload the image with minimum dimension 600 X 400")
    }
};

function getImageSizeInBytes(imgURL) {
    var request = new XMLHttpRequest();
    request.open("HEAD", imgURL, false);
    request.send(null);
    var headerText = request.getAllResponseHeaders();
    var re = /Content\-Length\s*:\s*(\d+)/i;
    console.log(headerText)
    re.exec(headerText);
    return parseInt(RegExp.$1);
}
function savedata(){
    var url = "http://localhost:8000/api/save_data"
    var title = $("#textinput").val();
    var content = tinyMCE.activeEditor.getContent();
    var title_count = parseInt($("#count").text())
    if (title.length < 70)
    {
      alert(" Minimum title length should be 70")
    }
    else
    {
      if(content.length < 100)
      {
        alert("News article cannot be blank")
      }
    }
    console.log(content)
  //   $.ajax({
  // type: "POST",
  // url: url,
  // data: "data",
  // success: "success",
  // dataType: "json"
  //   });
}