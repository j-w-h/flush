$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});



// Initialize app and store it to myApp variable for futher access to its methods
var myApp = new Framework7(
    fastClicks = true,
    activeState = true
    // activeStateElemets = 'a, button, label, span'
  );
 
// We need to use custom DOM library, let's save it to $$ variable:
var $$ = Dom7;

// Add view
var mainView = myApp.addView('.view-main', {
  // Because we want to use dynamic navbar, we need to enable it for this view:
  dynamicNavbar: true
});
 
// Now we need to run the code that will be executed only for About page.
 
// Option 1. Using page callback for page (for "about" page in this case) (recommended way):
// myApp.onPageInit('about', function (page) {
//   // Do something here for "about" page
//   console.log("about!!!!");
// })

myApp.onPageInit('building_detail', function (page) {
  // console.log("building_detail!!!!");
})

myApp.onPageInit('bathroom_detail', function (page) {

  var myMessagebar = myApp.messagebar('.messagebar', {
    maxHeight: 200
  });   
    
  $("#bottom-toolbar").addClass("toolbar-hidden");
  $("#bathroom-back").click(function() { mainView.showToolbar(); })

  // document.getElementById("new-comment-textarea").onclick = function() {
  //   console.log("yooooo");
  //   window.scrollTo(0,document.body.scrollHeight);
  // }

  bathroom = $("#bathroom-detail-page").attr("bath-url")

  $("#add-comment").click(function(){

    console.log(bathroom);

    comment_text = $("#new-comment-textarea").val();

    if (comment_text !== ""){

      $("#new-comment-textarea").val("");
      $("#comment-holder").prepend("<div class='card'><div class='card-content'><div class='card-content-inner'><div class='card-content-left'>" + comment_text + "</div><div class='card-content-right'><i class='fa fa-angle-up'></i><span class='comment-votes'>18</span><i class='fa fa-angle-down'></i></div></div><div class='card-content-bottom'><span class='footer-text'>ayooo</span></div></div></div>")

      $.ajax({
        type: 'POST',
        url: "add_comment/",
        data: {
          data: JSON.stringify({
                bathroom: bathroom,
                comment: comment_text
            })
        },
        error: function(e) {
          return console.log(e);
        },
        success: function(result) {
          console.log("success");
          console.log(result);
        }
      });

    }


  })


  // $.ajax({
  //   type: 'POST',
  //   url: "get_comments/" + bathroom + "/",
  //   error: function(e) {
  //     return console.log(e);
  //   },
  //   success: function(result) {
  //     console.log("success");
  //     console.log(result);
  //   }
  // });


                    // #data:
                    //     #data: JSON.stringify({
                    //         #project: itm.closest("tr").data().row
                    //         #val: value
                    //         #stat: itm.closest("td").data().key
                    //     #})

})

// Option 2. Using one 'pageInit' event handler for all pages:
// $$(document).on('pageInit', function (e) {
//   // Get page data from event data
//   var page = e.detail.page;
  
//   if (page.name === 'about') {
//     console.log("hey!!!!");
//     // Following code will be executed for page with data-page attribute equal to "about"
//     myApp.alert('Here comes About page');
//   }
// })
 
// Option 2. Using live 'pageInit' event handlers for each page
// $$(document).on('pageInit', '.page[data-page="about"]', function (e) {
//   // Following code will be executed for page with data-page attribute equal to "about"
//   // myApp.alert('Here comes About page!!!');
// })

// $$(document).on('pageInit', '.page[data-page="deeper"]', function (e) {
//   // Following code will be executed for page with data-page attribute equal to "about"
//   // myApp.alert('Here comes About page!!!');
// })