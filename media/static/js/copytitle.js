(function($) { 
  $(function() {
	  $(document).ready(function(){
		function ActualizarTitulo(valor){
			$("input[name=metatitle]").val(valor)	
		}
	    $("input[name=title],input[name=name]").keyup(function(){	 
			 ActualizarTitulo($(this).val())
		 })
		  $("input[name=title],input[name=name]").change(function(){	 
			ActualizarTitulo($(this).val()) 
		 })
	  })		
  });
})(django.jQuery);