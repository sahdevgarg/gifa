function validateForm(){
    var title = $("#textinput").val();
    var message = $("#messageinput").val();
    var email = $("#emailinput").val();
    if (title.length < 0)
    {
      alert(" Please enter the title")
      return false
    }
    else
    {
      if(message.length < 0)
      {
        alert("Please enter the message")
        return false
      }
      else
      {
        var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
            if (reg.test(email) == false) 
            {
                alert('Invalid Email Address');
                return false
            }
            else
              {
                $("#image").show()
                $(".bs-component").hide()
                return true
              }

      }
    }
    }