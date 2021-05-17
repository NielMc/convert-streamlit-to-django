let pwidth = document.getElementById("pwidth");
let swidth = document.getElementById("swidth");
let plength = document.getElementById("plength");
let slength = document.getElementById("slength");
let widthp = document.getElementById("widthp");
let widths = document.getElementById("widths");
let lengthp = document.getElementById("lengthp");
let lengths = document.getElementById("lengths");
widthp.innerHTML = pwidth.value; 
widths.innerHTML = swidth.value; 
lengthp.innerHTML = plength.value; 
lengths.innerHTML = slength.value; 
// Update the current slider value (each time you drag the slider handle)
pwidth.oninput = function() {
  widthp.innerHTML = this.value;
}
swidth.oninput = function() {
    widths.innerHTML = this.value;
  }
plength.oninput = function() {
    lengthp.innerHTML = this.value;
  }
slength.oninput = function() {
    lengths.innerHTML = this.value;
  }