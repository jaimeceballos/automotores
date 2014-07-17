
$(document).ready(function() {
   $('#id_unidad_regional').change(function(event){
   		var id = $('#id_unidad_regional').val();
   		var toLoad = '../../obtener_dependencias/'+id+'/';
   		$.get(toLoad, function(data){
 			var options = '<option value=""></option>';
	        for (var i = 0; i < data.length; i++){
	        	options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["descripcion"] +'</option>'
	        }
            $('#id_dependencia').html(options)
            $("#id_dependencia option:first").attr('selected', 'selected');
        }, "json");

   	});
   $('#table').dataTable( {
          "aaSorting": [[ 1, "desc" ]]
    } );
 });