
(function($) { 
  $(function() {
	  $(window).load(function(){
	  	$('.selectmediaItem').click(openpopup)
		 function openpopup(event)
		 {
		 	
		 	event.preventDefault();
		 	var selector=$(this);
		 	window.selector_id=$(this).attr('id');
		 	
	  		var popup = window.open(selector.attr('href') ,"Una", "scrollbars=1,resizable=0,height=300,width=450");
	  		
	  		popup.focus();

	  	}	 
	  })		
  });
})(django.jQuery);