function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$('.js-article-like').on('click', function() {
  var $btn = #(this),
    article_id = $btn.data('id'),
    csrftoken = getCookie('csrftoken');
  $.ajax({
    method: "POST",
    url: "/like/",
    data: {
      "article_id" : article_id
      "csrfmiddlewaretoken": csrftoken,
    },
    dataType: 'json'
  })
  .done(function( data ) {
    console.log(data);
    alert(data.count);
    $('#article_count-' + article_id).text(data.count)
    window.location.reload()
  })

  return false;
});
