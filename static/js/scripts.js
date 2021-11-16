$("textarea").keyup(function () {
  var characterCount = $(this).val().length,
    current = $("#current"),
    maximum = $("#maximum"),
    theCount = $("#the-count");

  current.text(characterCount);

  /*This isn't entirely necessary, just playin around*/
  if (characterCount < 143) {
    current.css("color", "#666");
  }
  if (characterCount > 142 && characterCount < 285) {
    current.css("color", "#6d5555");
  }
  if (characterCount > 284 && characterCount < 427) {
    current.css("color", "#793535");
  }
  if (characterCount > 426 && characterCount < 569) {
    current.css("color", "#841c1c");
  }
  if (characterCount > 568 && characterCount < 713) {
    current.css("color", "#8f0001");
  }

  if (characterCount >= 713) {
    maximum.css("color", "#8f0001");
    current.css("color", "#8f0001");
    theCount.css("font-weight", "bold");
  } else {
    maximum.css("color", "#666");
    theCount.css("font-weight", "normal");
  }
});
