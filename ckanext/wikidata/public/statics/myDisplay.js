let req = new XMLHttpRequest();
let url = document.getElementById("ajax_url").value;
let form_data = new FormData();
let package = document.getElementById("package_id").value
form_data.set('pkg_id', document.getElementById("package_id").value);

req.onreadystatechange = function() {
    if (req.readyState == XMLHttpRequest.DONE && req.status == 200 ){
        //document.getElementById('hero').innerHTML = package
        get_response($('#display_wiki_info'),url);
    }
    else {
        console.info(this.status)
    }

};
  req.open("POST", url, true);
  req.send(form_data);

function get_response(target,url){
    $.ajax({
        url: url,
        cache:true,
        dataType: 'json',
        type: "GET",
        success: function(result){
            if(result !== 0){
                let block = '';
                block += building(result);
                $(target).replaceWith(block);
            }
            else{
            $(target).replaceWith("No WikiData Information Link Available")
            }
            }
    });
}

function building(value){
    console.log('YES')
    return "<p> WikiData Information to this molecule is available <a href=' " + value + "' target='_blank'> here </a> </p>"
}





