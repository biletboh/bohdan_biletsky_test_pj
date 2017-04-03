(function() {

  /******** Widget function ********/
  function main() { 
    $(function() {

      /******* Load HTML *******/
      var jsonp_url = "http://cryptic-oasis-86413.herokuapp.com/widget/";
      console.log(jsonp_url);
      $.getJSON(jsonp_url, function(data) {
        data = JSON.parse(data);
        var random_note = data[Math.floor(Math.random() * data.length)];
        $('#notes-widget-container').html(

          '<div class="notes"><div class="row"> <div class="col-md-12"><h3><strong>'+ random_note.fields.name +'</strong></h3></div> </div> <hr> <div class="row"> <div class="col-md-12"> <p>'+ random_note.fields.body +'</p></div></div></div>'

          );
      });
    });
  }
  main();
})();
