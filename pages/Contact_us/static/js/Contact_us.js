// function validate(phone) {
// var i,y, valid=true;
// y= document.getElementsByClassName("input");
// for(i=0; i<y.length;i++){
//         if (y[i].value == ""){
//
//             y[i].className += " Invalid";
//             valid=false;
//
//         }
//
// }
//     if (valid==true)
//         phonenumber(phone)
//
// }
//
// function  phonenumber(phone){
//     let newphone =/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im
//     if(phone.value.match(newphone)){
//        let match=false
//         submitpage(match)
//         return true;
//
//     }
//     else {
//         alert("you need to put a currect number phone")
//         return false;
//     }
//
//
// }
//
// function submitpage(match){
//     if (match==false){
//         document.getElementById("input_form").submit();
//         document.getElementById("input_form").reset();
//     }
// }





function validate() {


    var firstname = document.getElementById("first_name");
    var lastName = document.getElementById("last_name");
    var phone = document.getElementById("phone");
    var email = document.getElementById("email");
    var subject = document.getElementById("subject");
    var message = document.getElementById("comment");
    var error_message = document.getElementById("error_message");



    error_message.style.padding = "20px";

    var text;

if (firstname.value =="") {
    alert(lastName)
    text = "Please Enter valid firstname";
    error_message.innerHTML = text;
    return false;
}
    if (lastName.value =="") {
        text = "Please Enter Correct lastName";
        error_message.innerHTML = text;
        return false;
    }
    if (email.indexOf("@") == -1 || email.length < 6) {
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
    }
    if (subject.length < 5) {
        text = "Please Enter Correct subject";
        error_message.innerHTML = text;
        return false;
    }
    if (isNaN(phone) || phone.length != 10) {
        text = "Please Enter valid Phone Number";
        error_message.innerHTML = text;
        return false;
    }

    if (message.length <= 20) {
        text = "Please Enter More Than 140 Characters";
        error_message.innerHTML = text;
        return false;
    }
     // document.getElementById("contactform").submit();
    alert("Form Submitted Successfully!");
    return true;
}

function getupdate(){
    return true
}

function getinsert(){
    return false
}