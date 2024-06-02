
let add_new_btn = document.querySelector('.add-new-btn')


const add_new_sec = document.querySelector('.add-new-sec')
function togglefunc() {
    add_new_sec.classList.toggle('d-none');
}

$(document).ready(function(){
    $("#search").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#table tbody tr").filter(function() {
        $(this).toggle($(this).children('td').eq(2).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  