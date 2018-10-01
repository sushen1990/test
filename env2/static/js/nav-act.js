$(document).ready(function(){
	$('.nav-tabs li').each(function(){
		$(this).removeClass('active')
		var hidd=$('p').text()
		var cur=$(this).text()
		if (hidd==cur ) {
			$(this).addClass('active')
		};				
	});
});