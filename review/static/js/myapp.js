 $(document).ready(function(){
    $(".icon-plus-sign").click(function() {
        $(this).class = "icon-remove-circle";
        var new_input = document.createElement("input");
        new_input.type = "text";
        new_input.name = "choice-"+(jQuery("div#choices input").length+1);
        new_input.id = new_input.name;
        insert_after = $("#choices input:last");
        //$("</br>").insertAfter(insert_after);
        $(new_input).insertAfter(insert_after);
        insert_after.after("</br>Choice "+(jQuery("div#choices input").length));
    });
    $(".icon-remove-circle").hover(function(){
        $(this).class = "icon-remove-sign";
    });
}); 