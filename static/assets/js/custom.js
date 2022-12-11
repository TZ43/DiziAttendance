$(document).ready(function()
 {
  $("button#add_guest").click(function()
  {
    var html='';
    var currentDate=GetCurrerntDate();
    var gustNumber= parseInt($("#numberofGust").val());
    if(gustNumber>0)
    {
        $(".Guest_details").show();
        for (let i = 1; i <= gustNumber; i++) 
        {
            html +='<tr> <td class="tddate">'+currentDate+'</td> <td class="tdname"><input id="text'+i+'" name="text'+i+'" type="text"/></td> <td class="tdcheck"><input id="check'+i+'" name="check'+i+'" type="checkbox"/></td> </tr>';
        }
        $('tbody#tblgust').empty();
        $('tbody#tblgust').append(html);
    }
    else
    {
        $(".Guest_details").hide();
    }

 });

function GetCurrerntDate()
{
    var d = new Date();
    var month = d.getMonth()+1;
    var day = d.getDate();
    var output =  (day<10 ? '0' : '') + day+'/'+(month<10 ? '0' : '') + month + '/' +d.getFullYear();
    return output;
}

});