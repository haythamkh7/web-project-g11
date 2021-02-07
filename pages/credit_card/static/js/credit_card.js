
function credit_card_validate(){
    alert("Form Submitted Successfully!");

    const form = document.forms["input_form"];
    const donation_type = form["donation_type"].value;
    const cost = form["cost"].value;
    const firstname = form["firstname"].value;
    const lastName = form["lastName"].value;
    const email = form["email"].value;
    const phone = form["phone"].value;
    const creditcard = form["creditcard"].value;
    const id = form["id"].value;
    const myname = form["myname"].value;
    const ccv = form["ccv"].value;
    var error_message = document.getElementById("error_message");
    error_message.style.padding = "10px";

    var text;

    if(isNaN(cost) ){
        alert("Sss");
      text = "Please Enter valid cost Number";
      error_message.innerHTML = text;
      return false;
    }

   if (donation_type === "") {
        text = "Please insert the donation_type";
        error_message.innerHTML = text;
        return false;
    }

    if(firstname.length << 1){
      text= "Please Enter valid firstname";
      error_message.innerHTML = text;
      return false;
    }

    if(lastName.length << 1){
      text = "Please Enter Correct lastName";
      error_message.innerHTML = text;
      return false;
    }

    if(email.indexOf("@") === -1 || email.length < 6){
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
      }

    if(isNaN(phone) || phone.length !== 10){
      text = "Please Enter valid Phone Number";
      error_message.innerHTML = text;
      return false;
    }

    if(myname.length < 1){
        text = "Please Enter Correct Name";
        error_message.innerHTML = text;
        return false;
      }

    if(isNaN(creditcard) || creditcard.length !== 16){
        text = "Please Enter valid creditcard Number";
        error_message.innerHTML = text;
        return false;
      }

    if(isNaN(ccv) || ccv.length !== 3){
        text = "Please Enter valid ccv Number";
        error_message.innerHTML = text;
        return false;
      }

    if(isNaN(id) || id.length !== 9){
        text = "Please Enter valid id Number";
        error_message.innerHTML = text;
        return false;
      }
    alert("Form Submitted Successfully!");
    return true;
  }