



function validate(){

    const form1 = document.forms["input_form"];
    const firstname = form1["first_name"].value;
    const lastName = form1["last_name"].value;
    const phone = form1["phone"].value;
    const email = form1["email"].value;
    const subject = form1["subject"].value;
    const gender = form1["gender"].value;
    const question = form1["question"].value;
    var error_message = document.getElementById("error_message");

    error_message.style.padding = "10px";
    var text;
    if(firstname.length < 1){
      text = "Please Enter valid firstname";
      error_message.innerHTML = text;
      return false;
    }
    if(lastName.length < 1){
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
    if (subject.length < 5) {
        text = "Please Enter Correct subject";
        error_message.innerHTML = text;
        return false;
    }
    if (gender === "") {
        text = "Please select your gender";
        error_message.innerHTML = text;
        return false;
    }
    if (question === "") {
        text = "Please Answer the question";
        error_message.innerHTML = text;
        return false;
    }
    alert("Form Submitted Successfully!");
    return true;
  }