var App = (function($){
	var form = $('form.sale-form');
	var tableList = $('.table-sales');

	function _deleteSale(){
		$(this).siblings('.modal').first().modal();
	}

	function _addSale(){
		window.location = "/sales/";
	}

	function _confirmModal(){
		$(this).parents("form").first().submit();
	}

	function _denyModal(e){
		e.preventDefault();
	}

	function _addEvents(){
		tableList.on("click",".delete-sale",_deleteSale);
		$('body').on("click",".add-sale",_addSale);
		$('body').on("click",".deny-modal",_denyModal);
		$('body').on("click",".confirm-modal",_confirmModal);
	}

	function _handleMessages(){
		$('.alert').show("fade");
		var id = setInterval(function(){
			$('.alert').hide("slow");
			clearInterval(id)
		}, 2000);
	}

	function init(){
		_addEvents();
		_handleMessages();
	}
	return {
		init: init
	}
})(jQuery);