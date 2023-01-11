$(document).ready(function(){

		//Query All input fields
		let form_fields = $('input');
		form_fields[6].placeholder='Choisissez votre mot de passe...';
		form_fields[7].placeholder='Confirmez votre mot de passe...';

		for (let field in form_fields){
			form_fields[field].className += ' form-control'
    }
    $('li').on('click',function(){
        $('li').removeClass('active');
        $('li').removeClass('secondary-active');
        $(this).addClass('active');
        $(this).addClass('secondary-active');
        $(this).prevAll().addClass('secondary-active');
    })
});



