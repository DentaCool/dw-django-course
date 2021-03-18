

var page = 2

function lazy_load_posts(data) {
    console.log(data)
        data.results.forEach((post) => {
            const putHtmlData = `
            <div class="card col-12 col-md-5 mb-4 m-1">
                <div class="card-body">
                    <h2 class="card-title">${ post.title}</h2>
                    <p class="card-text text-muted h6">${ post.author } | ${ post.created} </p>
                    ${post.body.slice(0,200)}
                    <p class="card-text"></p>
                    <a href="/post_detail${post.slug}'" class="btn btn-primary">Read More &rarr;</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>`
  
            $("#row").append(putHtmlData)
        })
    }

$(document).ready(() => {
    $(window).scroll(function() {
        if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
            var post_id = $("#post_id").val();
            
            
            if (page!=null&&already_loading==false) {
                already_loading=true
                $.ajax({
                    type: 'get',
                    url: `/api/posts/?page=${page}`,
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

})