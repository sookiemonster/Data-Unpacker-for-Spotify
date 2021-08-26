$(document).ready(function () {

  // Track Name Chart ID

  $(".track-chart-container").each(function(index) {
    $(this).children("canvas").attr("id", "track-chart-" + index);
  });

  // Chart Time Selectors

  $(".time-selector span").click(function() {
    $(this).siblings("span").removeClass("active-time");
    $(this).addClass("active-time");
  });

  // List Counters

  var longest_counter = $(".popular-item").each(function(index) {
    $(this).prepend('<span class="list-count"><span class="bullet">#</span>' + (index + 1) + "</span>");
  }).last().children(".list-count");

  // Equalize Counter Width

  $(".popular-item .list-count").width(longest_counter.width());

  // Artist Top Song Counter

  $(".popular-expanded").each(function() {
    console.log($(this));
    $(this).find(".list-count").each(function(index) {
      $(this).text(index + 1);
    });
  });

  // Truncate-Text via Adjusting Width

  // $(window).on("resize", function() {
  //   $(".clip-container").each(function(index) {
  //     $(this).width($(".popular-description").width());
  //   });
  // }).resize();

  // Track & Artist Toggle

  $(".artist").hide();

  $("#icon-image").filter(function() {
    return $(this).attr('src')==='';
  }).hide();

  $("#no-icon").filter(function() {
    return $("#icon-image").attr('src')!='';
  }).hide();

  $("#artist-select").click(function() {

    $(".song").hide();
    $(".artist").show();

    $("#artist-select").addClass("active-button");
    $("#song-select").removeClass("active-button");

    $("#popular-header").html("Your Favorite Artists");

    $(".time-selector-track .over-week:visible").click();
  });

  $("#song-select").click(function() {

    $(".artist").hide();
    $(".song").show();

    $("#song-select").addClass("active-button");
    $("#artist-select").removeClass("active-button");

    $("#popular-header").html("Your Favorite Songs");

    $(".time-selector-track .over-week:visible").click();
  });

  // Toggle Track Information
    
    $(".top-item").click(function(event) {
        var $target = $(event.target);
        if (!$("#popularity").is(':animated')) {
          if (!$(this).hasClass("expanded")) {
            
            // Expand info 
            $(this).addClass("expanded").children(".popular-expanded").css("display", "grid").hide().fadeIn(200);

          } else if (!$target.hasClass("clickable") && !$target.closest(".clickable").length) {

            // Close Info
            $(this).removeClass("expanded").children(".popular-expanded").hide();    
          }
        }
      });
  
  // Toggle Album Link

  $(".album-link").each(function() {
    if ($(this).attr("href") == "" || value == undefined) {
      $(this).hide();
    }
  });

  // $(".top-item").click(function() {
  //   if (!$("#popularity").is(':animated')) {
  //       var card = $(this).children(".track-card");
  //       var img;
    
  //       if (card.is(":hidden")) {
  //         $(".track-card").hide();
  //         card.css("display", "flex").hide().fadeIn(200);
  //         if ($("#song-select").hasClass("active-button")) {
  //           card.find(".track-count").show();
  //           img = card.children(".track-img")[0];
    
  //           // Update Charts
  //           card.find(".active-time")[0].onclick();
  //         } else {
  //           card.find(".artist-count").show();
  //           img = card.children(".artist-img")[0];
    
  //           // Update Charts
  //           card.find(".active-time")[0].onclick();
  //         }
  //         // Style Track Card Background
  //         // Color-Thief: https://github.com/lokesh/color-thief
          
  //         var col;
    
  //         if (img.complete) {
  //           const colorThief = new ColorThief();
  //           col = colorThief.getColor(img);
  //           $("html").attr("style", "--card-bg: rgba(" + 
  //             col[0] + ", " + col[1] + ", " + col[2] + ", 1)");
  //         } 
  //         else {
  //           img.addEventListener('load', function() {
  //             col = colorThief.getColor(img);
  //             $("html").attr("style", "--card-bg: rgba(" + 
  //               col[0] + ", " + col[1] + ", " + col[2] + ", 1");
  //           });
  //         }
    
  //       }
  //     }
  //   });

});
