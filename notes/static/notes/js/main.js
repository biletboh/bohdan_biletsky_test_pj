$(function() {

  // File form field
  initUploadFields($('#notes-form'));
  $('#notes-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // check
    create_post();
  });

  // Ajax for posting 
  function create_post() {
    console.log("create note is working!"); // check
    console.log($('#id_body').val());
    $.ajax({
      url : window.location.href, // the endpoint
      type : "POST", // http method
      data : { name: $('#id_name').val(),
        body: $('#id_body').val() }, // data sent with the post request

      // handle a successful response
      success : function(json) {
        $('#id_name').val(''); // remove the value from the input
        $('#id_body').val(''); // remove the value from the input
        $('#messages').html("<div class='alert alert-success'>The note was created!</div>"); // add the error to the dom


        console.log("success"); // another sanity check
      },
      // handle a non-successful response
      error : function(xhr,errmsg,err) {
        $('#messages').html("<div class='alert alert-danger'>Oops! We have encountered an error: "+errmsg+
          " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
      
    });
  };

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
      (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
      !(/^(\/\/|http:|https:).*/.test(url));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
        // Send the token to same-origin, relative URLs only.
        // Send the token only if the method warrants CSRF protection
        // Using the CSRFToken value acquired earlier
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

});
