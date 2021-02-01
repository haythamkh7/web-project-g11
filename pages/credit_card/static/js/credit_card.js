function validate(){
    var cost = document.getElementById("cost").value;
    var firstname = document.getElementById("firstname").value;
    var lastName = document.getElementById("lastName").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var myname = document.getElementById("myname").value;
    var creditcard = document.getElementById("creditcard").value;
    var id = document.getElementById("id").value;
    var ccv = document.getElementById("ccv").value;

    var error_message = document.getElementById("error_message");

    error_message.style.padding = "10px";

    var text;

    if(isNaN(cost) ){
      text = "Please Enter valid cost Number";
      error_message.innerHTML = text;
      return false;
    }

    if(firstname.length < 1){
      text= "Please Enter valid firstname";
      error_message.innerHTML = text;
      return false;
    }
    if(lastName.length < 1){
      text = "Please Enter Correct lastName";
      error_message.innerHTML = text;
      return false;
    }
    if(email.indexOf("@") == -1 || email.length < 6){
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
      }

    if(isNaN(phone) || phone.length != 10){
      text = "Please Enter valid Phone Number";
      error_message.innerHTML = text;
      return false;
    }

    if(myname.length < 1){
        text = "Please Enter Correct Name";
        error_message.innerHTML = text;
        return false;
      }
      if(isNaN(creditcard) || creditcard.length != 16){
        text = "Please Enter valid creditcard Number";
        error_message.innerHTML = text;
        return false;
      }
      if(isNaN(ccv) || ccv.length != 3){
        text = "Please Enter valid ccv Number";
        error_message.innerHTML = text;
        return false;
      }
      if(isNaN(id) || id.length != 9){
        text = "Please Enter valid id Number";
        error_message.innerHTML = text;
        return false;
      }
    alert("Form Submitted Successfully!");
    return true;
  }