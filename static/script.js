// $(function () {
//     $("td[colspan=2]").find("holder").hide();
//     $("table").click(function (event) {
//         event.stopPropagation();
//         var $target = $(event.target);
//         if ($target.closest("td").attr("colspan") > 1) {
//             $target.slideUp();
//         } else {
//             $target.closest("tr").next().find("tr").slideToggle();
//         }
//     })
// });

// $(document).ready(function () {
//     debugger;
//     $('.hideTr').slideUp(600);
//     $('[data-toggle="toggle"]').click(function () {
//         if ($(this).parents().next(".hideTr").is(':visible')) {
//             $(this).parents().next('.hideTr').slideUp(600);
//             $(".plusminus" + $(this).children().children().attr("id")).text('+');
//             $(this).css('background-color', 'white');
//         }
//         else {
//             $(this).parents().next('.hideTr').slideDown(600);
//             $(".plusminus" + $(this).children().children().attr("id")).text('- ');
//             $(this).css('background-color', '#c1eaff ');
//         }
//     });
// });  