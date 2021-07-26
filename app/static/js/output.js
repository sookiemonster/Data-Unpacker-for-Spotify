$(document).ready(function () {

  $("li").each(function(index) {
    $(this).prepend('<span class="list-count"><span class="bullet">#</span>' + (index + 1) + "</span>");
  });

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

  $("ol li").click(function() {
    if ($(this).children(".track-card").is(":hidden")) {
      $(".track-card").hide();
      $(this).children(".track-card").css("display", "flex").hide().fadeIn(200);
      if ($("#song-select").hasClass("active-button")) {
        $(this).children(".track-card").find(".track-count").show();
      } else {
        $(this).children(".track-card").find(".artist-count").show();
      }
    }
  });

  $(document).click(function(event) { 
    var $target = $(event.target);
    if(!$target.closest("li").length && 
      $(".track-card").is(":visible")) {
        $(".track-card").fadeOut(200);
      }        
  });



});
