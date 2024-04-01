/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
function convertEnterToTab() {
    if(event.keyCode==13) {
        event.keyCode = 9;
    }
}

function formataData(Campo, teclapres){
    var tecla = teclapres.keyCode;
    var vr = new String(Campo.value);
    vr = vr.replace("/", "");
    vr = vr.replace("/", "");
    tam = vr.length + 1;

    if (tecla==8 || tecla==9 || tecla==16 || tecla==46) {
        return;
    }else if (tecla>=35 && tecla<=40){
        return;
    }

    if (tecla != 9 && tecla != 8){
        if (tam > 2 && tam < 5)
            Campo.value = vr.substr(0, 2) + '/' + vr.substr(2, tam);
        if (tam >= 5 && tam <=10)
            Campo.value = vr.substr(0,2) + '/' + vr.substr(2,2) + '/' + vr.substr(4,4);
    }
}

function dateMask(inputData, e){
    if(document.all) // Internet Explorer
        var tecla = event.keyCode;
    else //Outros Browsers
        var tecla = e.which;

    if(tecla >= 47 && tecla < 58){ // numeros de 0 a 9 e "/"
        var data = inputData.value;
        if (data.length == 2 || data.length == 5){
            data += '/';
            inputData.value = data;
        }
    }else if(tecla == 8 || tecla == 0) // Backspace, Delete e setas direcionais(para mover o cursor, apenas para FF)
        return true;
    else
        return false;
}

/*jQuery(function() {
    jQuery("div.button > a").each(function() {
        jQuery(this).mouseenter(function() {
            jQuery(this).parent().find("span.hint").fadeIn('fast');
        });

        jQuery(this).mouseleave(function() {
            jQuery(this).parent().find("span.hint").fadeOut('fast');
        });
    });
});*/

function filterOnEnter(widgetVar){
    jQuery(widgetVar.jqId).find('th .ui-column-filter').each(function(idx) {
        var element = jQuery(this);
        element.unbind('keydown');
        element.unbind('keyup');
        element.removeAttr('onkeyup');
        // replaces keydown for enter
        element.keydown(function(event) {
            var e = (window.event) ? window.event : event;
            if(e.keyCode == 13) {
                event.preventDefault();
                widgetVar.filter();
            }
        })
    });
}


function spreadTable(id, columns, highlight){
        var $table = jQuery("input[id ^= "+(id.replace(/:/g,"\\:")+"]:first")).closest("table");
        var $td = $table.find("tr td");
        var inner = "";
        var total = 0;
        jQuery.each($td, function(i, element) {
            if(total == 0){
                inner = inner+"<tr>";
            }
            var checkbox = jQuery(element).find("input[type=checkbox],input[type=radio]");
            if(highlight && checkbox[0].checked == true){
                inner = inner+"<td class='ui-state-highlight' style='border: 0;'>";
            }else{
                inner = inner+"<td>";   
            }
            inner = inner+element.innerHTML+"</td>";
            if(total == columns-1){
                inner = inner+"</tr>";
                total = 0;
            }else{
                total++;
            }
        });
        $table.html(inner);
        if(highlight == true){
            $table.find("input[type=checkbox],input[type=radio]").click(function() {
                var $td = jQuery(this).closest("td");
                $td.css("border", 0);
                if($(this).attr("type") == "radio"){
                    $table.find("td").removeClass("ui-state-highlight");
                }
                if(this.checked){
                    $td.addClass("ui-state-highlight");
                }else{
                    $td.removeClass("ui-state-highlight");
                }
            });
        }
    }