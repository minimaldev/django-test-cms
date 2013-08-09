(function($) 
{ 
  $(function() 
  {
	  $(window).load(function()
	  {
	    //$( ".resizeme" ).aeImageResize({ height: 250, width: 250 });
	    $(".selectItem").on('click',cancelpress)
	     function cancelpress(event)
	    {
	    	event.preventDefault();

	    	window.opener.$("input#id_"+window.opener.selector_id).val($(this).attr('href'));
	    	window.close();
	    }
	    $("#selectitem").on('click',upload_item)
	    function upload_item(event)
	    {
	    	event.preventDefault();
	    	$('#uploadfile').focus().trigger('click');
	    }
	  });	
  });
})(jQuery);