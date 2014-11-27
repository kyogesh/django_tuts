 $(document).ready(function(){
    $('#add').click(function() {
    var new_input = document.createElement("input");
    new_input.type = "text";
    new_input.name = "choice-"+(jQuery("div#choices input").length+1);
    new_input.id = new_input.name;
    var div=$('#choices');
    $("div").append("</br>Choice "+(jQuery("div#choices input").length+1))
    //div.append("</br>");
    div.append(new_input);
    });
}); 