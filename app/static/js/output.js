$(document).ready(function () {

  // List Counters

  $("li").each(function(index) {
    $(this).prepend('<span class="list-count"><span class="bullet">#</span>' + (index + 1) + "</span>");
  });

  $(".card-list-count").each(function(index) {
    $(this).append(index + 1);
  });

  // Track & Artist Toggle

  $(".artist, .artist-img, .artist-count").hide();

  $("#icon-image").filter(function() {
    return $(this).attr('src')==='';
  }).hide();

  $("#no-icon").filter(function() {
    return $("#icon-image").attr('src')!='';
  }).hide();

  $("#artist-select").click(function() {
    if($(window).width() > 500){
      $(".artist-count").show();
    }  

    $(".song-title, .song-artist, .track-img, .track-count, .clip-container").hide();
    $(".artist, .artist-img").show();
    $("#popular-header").html("Your Favorite Artists");
    $("#artist-select").addClass("active-button");
    $("#song-select").removeClass("active-button");
  });

  $("#song-select").click(function() {
    if($(window).width() > 500){
      $(".track-count").show();
    }

    $(".artist, .artist-count, .artist-img").hide();
    $(".song-title, .song-artist, .track-img, .clip-container").show();
    $("#popular-header").html("Your Favorite Songs");
    $("#song-select").addClass("active-button");
    $("#artist-select").removeClass("active-button");
  });

  // Track Count Toggle
  
  $(window).on("resize",function() {  
    if($(window).width() <= 500) {
      $(".popular item .track-count").hide();
      $(".popular item .artist-count").hide();
    } else {
      if ($("#song-select").hasClass("active-button")) {
        $(".track-count").show();
      } else {
        $(".artist-count").show();
      }
    }
  });

  // Track Card Open

  $("ol li").click(function() {
    var card = $(this).children(".track-card");
    var img;

    if (card.is(":hidden")) {
      $(".track-card").hide();
      card.css("display", "flex").hide().fadeIn(200);
      if ($("#song-select").hasClass("active-button")) {
        card.find(".track-count").show();
        img = card.children(".track-img")[0];
      } else {
        card.find(".artist-count").show();
        img = card.children(".artist-img")[0];
      }
      // Style Track Card Background
      // Color-Thief: https://github.com/lokesh/color-thief
      
      var col;

      if (img.complete) {
        const colorThief = new ColorThief();
        col = colorThief.getColor(img);
        console.log(col);
        $("html").attr("style", "--card-bg: rgba(" + 
          col[0] + ", " + col[1] + ", " + col[2] + ", 1)");
      } 
      else {
        img.addEventListener('load', function() {
          col = colorThief.getColor(img);
          $("html").attr("style", "--card-bg: rgba(" + 
            col[0] + ", " + col[1] + ", " + col[2] + ", 1");
        });
      }

    }
  });

  // Track Card Close

  $(document).click(function(event) { 
    var $target = $(event.target);
    if(!$target.closest("li").length && 
      $(".track-card").is(":visible")) {
        $(".track-card").fadeOut(200);
      }        
  });


});
