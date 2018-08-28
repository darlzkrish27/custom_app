$(document).ready(function() {
				var numitems =  $("#myList li").length;

				$("ul#myList").css("column-count",Math.round(numitems/4));
				});