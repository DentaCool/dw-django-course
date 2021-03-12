function load_comments() {
  var post_id = $("#post_id").val();

  $("#comments").html(`<div class="spinner-border" role="status">
    <span class="sr-only">Loading...</span>
  </div>`)
  $.ajax({
      type: "GET",
      url: `/api/article/posts/${post_id}/comments/?page=1`,
      success: function(data) {

          $("#comments").html("")
          data.results.forEach((comment_data) => {
              const putHtmlData = `
    <div class="card p-1">
    <div class="card-header">
      ${comment_data["author_comment"]}
    </div>
    <div class="card-body">
      <p class="card-text">
      <p>${comment_data["body"]}</p>
      </p>
    </div>
    
    <h6 class="card-subtitle mb-2 text-muted">${comment_data["created"]}</h6>
  </div>`

              $("#comments").append(putHtmlData)
          })


      }
  });
}


function lazy_load_comments(data, page) {
  console.log(data)
  if (data.next) {
      console.log(data["next"])
      link.data('page', page + 1);
      data.results.forEach((comment_data) => {
          const putHtmlData = `
                      <div class="card p-1">
                      <div class="card-header">
                        ${comment_data["author_comment"]}
                      </div>
                      <div class="card-body">
                        <p class="card-text">
                        <p>${comment_data["body"]}</p>
                        </p>
                      </div>
                      
                      <h6 class="card-subtitle mb-2 text-muted">${comment_data["created"]}</h6>
                    </div>`

          $("#comments").append(putHtmlData)
      })
  }

  $(document).ready(() => {
          load_comments()

          $('#lazy-comments').on('click', function() {
                  var link = $(this);
                  var page = link.data('page');
                  var post_id = $("#post_id").val();

                  $.ajax({
                          type: 'get',
                          url: `/api/article/posts/${post_id}/comments?page=${page}`,
                          data: {
                              'post_id': post_id,
                          },
                          success: function(data) {

                          } else {
                              link.hide();
                          }
                      },
                      error: function(xhr, status, error) {}
                  });
          });

      $(window).scroll(function() {
          if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
              alert("near bottom!");
          }
      });

      $("#likes-count").click(function(e) {
          var post_id = $("#post_id").val();
          // var csrf = $("[name=csrfmiddlewaretoken]").val();
          $.ajax({
              type: "POST",
              url: "/api/article/posts/" + post_id + "/like/",
              data: JSON.stringify({
                  'post_id': parseInt(post_id)
              }),

              contentType: 'application/json',
              success: function(data) {
                  $("#likes-count").html("Like " + data["like_count"])
              }
          });
      })

      $("#comment").click(function(e) {
          $("#comment-form").toggleClass("d-none");
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