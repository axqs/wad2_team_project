
function create_review(){
	setTimeout(function(){ window.location.reload() }, 100);
	console.log("Review form has been sumitted!");

}

function hide_show_one(){
    		$(document).ready(function(){
			$(".btn1").click(function(){
				$("p").hide();
			});
			$(".btn2").click(function(){
				$("p").show();
			});
		});
    
}

function hide_show_two(){
    		$(document).ready(function(){
			$(".btn3").click(function(){
				$("p1").hide();
			});
			$(".btn4").click(function(){
				$("p1").show();
			});
		});
    
}