function delete_sale(){
	var form = $('.delet_form');
	var res = confirm("Tem certeza que deseja exluir essa venda?");
	if(res){
		form.submit();
	}
}
$(document).ready(function(){
	$('body').on("click",".addSale",function(){
		$('.formSale').show("fast",function(){
			var top = $(this).offset().top;
			$('body').scrollTop(top)
		})
	});
});