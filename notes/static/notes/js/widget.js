(function() {

  /******** Widget function ********/
  function main() { 
    $(function() {

      /******* Load HTML *******/
      var jsonp_url = "https://cryptic-oasis-86413.herokuapp.com/widget/";
      console.log(jsonp_url);
      $.getJSON(jsonp_url, function(data) {
        random_note = JSON.parse(data);
        $('#notes-widget-container').html(

          '<div class="notes"><div class="row"> <div class="col-md-12"><h3><strong>'+ random_note[0].fields.name +'</strong></h3></div> </div> <hr> <div class="row"> <div class="col-md-12"> <p>'+ random_note[0].fields.body +'</p></div></div></div>'

          );
        $('.notes').css({'background': '#DFDEDE', 'border-radius': '4px', 'box-shadow': '0 1px 2px rgba(0, 0, 0, 0.05), 0 0 0 1px rgba(63, 63, 68, 0.1)', 'padding': '10px', 'margin': '20px 5px'});
      });
    });
  }
  main();
})();
