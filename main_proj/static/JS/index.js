let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
  menu.classList.toggle('bx-x');
  navbar.classList.toggle('open');
}

var counter = 1;
setInterval(function () {
  document.getElementById('radio' + counter).checked = true;
  counter++;

  if (counter > 7) {
    counter = 1;
  }
}, 4000);



function previewImage() {
  const fileInput = document.getElementById('productImage');
  const imagePreview = document.getElementById('imagePreview');
  const uploadButton = document.getElementById('uploadButton');
  const changeButton = document.getElementById('changeButton');

  imagePreview.innerHTML = '';

  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const img = document.createElement('img');
      img.src = e.target.result;
      img.alt = 'Preview';
      img.style.maxWidth = '200px';
      imagePreview.appendChild(img);
      changeButton.style.display = 'inline-block';
      uploadButton.style.display = 'none';
    }
    reader.readAsDataURL(file);
  }
}



// animations

window.addEventListener('scroll', reveal);

function reveal() {
  var reveals = document.querySelectorAll('.reveal');

  for (var i = 0; i < reveals.length; i++) {
    var windowheight = window.innerHeight;
    var revealtop = reveals[i].getBoundingClientRect().top;
    var revealpoint = 100;

    if (revealtop < windowheight - revealpoint) {
      reveals[i].classList.add('active');
    }
    else {
      reveals[i].classList.remove('active');
    }
  }
}


// Ratting with 5 star

let ratting = 0;

function rate(stars) {
  ratting = stars;
  let allStars = document.querySelectorAll('.star');
  for (let i = 0; i < allStars.length; i++) {
    if (i < stars) {
      allStars[i].classList.add('gold');
    } else {
      allStars[i].classList.remove('gold');
    }
  }
}

document.querySelectorAll('.star')[3].addEventListener('click', function () {
  rate(4);
});



function togglePopup() {
  var popup = document.getElementById("popup");
  if (popup.style.display === "none" || popup.style.display === "") {
    popup.style.display = "block";
  } else {
    popup.style.display = "none";
  }
}

var is_visible = false;
        function see() {
            var input = document.getElementById('pass');
            var see = document.getElementById('see');

            if (is_visible) {
                input.type = 'password';
                is_visible = false;
                see.style.color = 'gray';
            } else {
                input.type = 'text';
                is_visible = true;
                see.style.color = '#262626';
            }
        }


        function checkForm() {
            var isValid = true;
 
            var password = document.getElementById("pass").value;
        
            if (password.length < 5) {
                document.getElementById('check1').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('check1').style.display = 'none';
            }
        
            if (!password.match(/[0-9]/)) {
                document.getElementById('check2').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('check2').style.display = 'none';
            }
        
            if (!password.match(/[^A-Za-z0-9-'']/)) {
                document.getElementById('check3').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('check3').style.display = 'none';
            }
        
            if (!password.match(/[A-Z]/)) {
                document.getElementById('check4').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('check4').style.display = 'none';
            }
        
            if (password.includes(' ')) {
                document.getElementById('check5').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('check5').style.display = 'none';
            }
        
            return isValid;
        }


        function search(){
          let filter = document.getElementById('find').value.toUpperCase();
          let item = document.querySelectorAll('.product');
          let l = document.getElementsByTagName('h2');
  
          for(var i=0 ; i<=l.length ; i++){
              let a = item[i].getElementsByTagName('h2')[0];
  
              let value = a.innerHTML || a.innerText || a.textContent;
  
              if(value.toUpperCase().indexOf(filter) > -1){
                  item[i].style.display='';
              }else{
                  item[i].style.display='none';
                  
              }
          }
      }

      document.getElementById("searchBox").addEventListener("click", function() {
          var input = this.querySelector("input");
          if (input.style.width === "0") {
              input.style.width = "300px";
          } else {
              input.style.width = "300px";
          }
      });



// navbar dropdown

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.style.display === "block") {
        openDropdown.style.display = "none";
      }
    }
  }
}
