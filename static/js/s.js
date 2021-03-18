var page = 2
var already_loading = false

function load_comments() {
    var post_id = $("#post_id").val();

    $("#comments").html(`<div class="d-flex justify-content-center">
    <div class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
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


function lazy_load_comments(data) {
    console.log(data)
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
    $(window).scroll(function() {
        if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
            var post_id = $("#post_id").val();
            
            
            if (page!=null&&already_loading==false) {
                already_loading=true
                $.ajax({
                    type: 'get',
                    url: `/api/article/posts/${post_id}/comments?page=${page}`,
                    data: {
                        'post_id': post_id,
                    },
                    success: function(data) {
                        lazy_load_comments(data)
                        page++
                        already_loading=false
                    },
                    error: function(xhr, status, error) {page = null}
                });
            }
        }
    });

    $("#likes-count").click(function(e) {
        var post_id = $("#post_id").val();
        var csrf = $("[name=csrfmiddlewaretoken]").val();
        var head = {}
        if (csrf) {
            head["X-CSRFToken"] = csrf;
        }
        $.ajax({
            type: "POST",
            url: "/api/article/posts/" + post_id + "/like/",
            data: JSON.stringify({
                'post_id': parseInt(post_id)
            }),
            headers: head,

            contentType: 'application/json',
            success: function(data) {
                $("#likes-count").html("Like " + data["like_count"])
            }
        });
    })

    // $("#comment").click(function(e) {
    //     $("#comment-form").toggleClass("d-none");
    // })

    $("#comment-form").submit(function(e) {

        var author = $("#author").val();
        var body = $("#body").val();
        var post_id = $("#post_id").val();

        e.preventDefault();

        var csrf = $("[name=csrfmiddlewaretoken]").val();
        var head = {}
        if (csrf) {
            head["X-CSRFToken"] = csrf;
        }
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/api/article/posts/" + post_id + "/comments/",
            data: JSON.stringify({
                'post_id': parseInt(post_id),
                'author_comment': author,
                'body': body,
            }),
            headers: head,
            contentType: 'application/json',
        });
    });
});