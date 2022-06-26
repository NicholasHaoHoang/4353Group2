let profileForm = document.querySelector("#profilemanagement");
let zipcodeValid = false;
let zipcodeWidget = document.querySelector("#zipcode");
profileForm.addEventListener("submit", checkForm);
zipcodeWidget.addEventListener("input", checkZipcode);

//checks validity of Zipcode
function checkZipcode() {
   let zip = zipcodeWidget.value;
   zip = zip.trim();
   zipcodeValid = (zip.length == 5||zip.length==9) && !isNaN(zip);
   if(zipcodeValid){
    profileForm.zipcode.style.backgroundColor = "rgb(204, 255, 204)";
   }else{
    profileForm.zipcode.style.backgroundColor = "rgb(255, 153, 153)";
   }
}


//checks if there are any errors in the Profile Management form.
function checkForm(event) {
    if (!zipcodeValid) {
       event.preventDefault();
       profileForm.zipcode.style.backgroundColor = rgb(255, 153, 153);
       alert("Please enter a valid Zipcode");
    }
 }

//
//
//
 let fuelForm = document.querySelector("#fuelquote");
 let gallons = document.querySelector("#gallonsreq");
 let deldate = document.querySelector("#deliverydate");
 fuelForm.addEventListener("submit", );//add check form method on submit 
 gallons.addEventListener("input", updateValues); //add check validity of inputs
 deldate.addEventListener("input", minDate);

//For validation and update of Fuel Quote Form
function updateValues(){
    //TODO: Pull pricing from pricing module
    let pricepergallon = 1;
    document.querySelector("#pricepergallon").setAttribute('value',pricepergallon);
    let total = pricepergallon*gallons;
    document.getElementById("totalamount").setAttribute('value',total);

}
//Get Today's date, set as min for deliverydate
function minDate(){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1;
    var yyyy = today.getFullYear();
    if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 

    today = yyyy+'-'+mm+'-'+dd;
    document.getElementById("deliverydate").setAttribute("min", today);
}
//Set Delivery Address to the address from profile management
function updateAddress(){
    //TODO: Add functionality to pull client's address from database
}
