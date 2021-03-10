
$(document).ready(() => {

  $("#likes-count").click(function(e) {
    var post_id = $("#post_id").val();
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/api/article/posts/" + post_id + "/like/",
      data: JSON.stringify({
          'post_id': parseInt(post_id)
      }),
      contentType: 'application/json',
      success: function (data){
        $("#likes-count").html("Like " + data["like_count"])
      }
  });

  })

  $("form").submit(function(e) {

      var author = $("#author").val();
      var body = $("#body").val();
      var post_id = $("#post_id").val();

      e.preventDefault();

      $.ajax({
          type: "POST",
          url: "http://127.0.0.1:8000/api/article/posts/" + post_id + "/comments/",
          data: JSON.stringify({
              'post_id': parseInt(post_id),
              'author_comment': author,
              'body': body,
          }),
          contentType: 'application/json',
      });
  });
});