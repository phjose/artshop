/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// NAVBAR
window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        const navbarBordable = document.body.querySelector('#innerContainer');

        if (!navbarCollapsible) {
            return;
        }

        if (window.scrollY === 0) {
            if (window.outerWidth <= 1200) {
                navbarCollapsible.classList.add('navbar-shrink')
                //navbarBordable.classList.remove('border-bottom')
            } else {
                navbarCollapsible.classList.remove('navbar-shrink')
                //navbarBordable.classList.add('border-bottom')
            }
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
            //navbarBordable.classList.remove('border-bottom')
        }
    };

    // Shrink the navbar
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

// NAVBAR

// MASONRY
const $grid = $('.grid').imagesLoaded(() => {
    //Activate Masonry grid
    $('.grid').masonry({
        //Select items
        itemSelector: '.grid-item',
        //Set Width
        columnWidth: '.grid-item',
        percentPosition: true,
        gutter: 10,
        originLeft: true,
    })
});
// MASONRY

// IMAGE ZOOM SL
$(document).ready(function(){
  $("#zoom").imagezoomsl({
    loadopacity: 0.1,
    loadbackground:'#878787',
    disablewheel:false,
    stepzoom: 0.5,
    zoomrange: [3, 3],
    zoomstart: 2
  }
  );
});
// IMAGE ZOOM SL

// COOKIE MANAGE
setCookie = (cName, cValue, expDays) => {
  let date = new Date();
  date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
  const expires = "expires=" + date.toUTCString();
  document.cookie = cName + "=" + cValue + ";" + expires + "; path=/";
}

getCookie = (cName) => {
  const name = cName + "=";
  const cDecoded = decodeURIComponent(document.cookie);
  const cArr = cDecoded.split("; ")
  let value;
  cArr.forEach(val => {
    if (val.indexOf(name) === 0) value = val.substring(name.length);
  })
  return value;
}

document.querySelector("#cookies-btn").addEventListener("click", () => {
  document.querySelector("#cookies").style.display = "none";
  setCookie("cookie", true, 30);
})

cookieMessage = () => {
  if(!getCookie("cookie"))
    document.querySelector("#cookies").style.display = "block";
}

window.addEventListener("load", cookieMessage);

// COOKIE MANAGE


// CART
$(document).ready(function(){

  $("#addCart").on("click", function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url: url_add,
      data: {
        product_id: $("#addCart").attr('data-painting-id'),
        csrfmiddlewaretoken: csrftoken,
        action: 'post',
      },
      success: function(json){
        console.log(json);
        $("#cartQuantity").text(json.qty);
      },

      error: function(xhr, errmsg, err){
        console.log(errmsg);
      }
    });
  });

  $(".delete-product").on("click", function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url: url_delete,
      data: {
        product_id: $(this).attr('data-product-id'),
        //product_id: $(this).data('index'), //Esto es así porque es un boton, de ser un link sería como en add_cart arriba
        csrfmiddlewaretoken: csrftoken,
        action: 'post',
      },
      success: function(json){
        console.log(json);
        location.reload();
      },

      error: function(xhr, errmsg, err){
        console.log(errmsg);
      }
    })
  })
});
// CART

// DELETE PAINTINGS
$(document).ready(function(){
    const deleteModal = document.getElementById('deleteModal')
    if (deleteModal) {
      deleteModal.addEventListener('show.bs.modal', event => {
        // Button that triggered the modal
        const button = event.relatedTarget
        // Extract info from data-bs-* attributes
        const redirectTo = button.getAttribute('data-bs-whatever')
        // If necessary, you could initiate an Ajax request here
        // and then do the updating in a callback.

        // Update the modal's content.
        const modalHref = deleteModal.querySelector('.delete-href')

        modalHref.href = redirectTo
      })
    }
})
// DELETE PAINTINGS



