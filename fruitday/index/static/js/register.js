$(function () {
    $('frmList').submit(function(){
        var zphone = $('[name = zphone]').val();
        var zpwd = $('[name = zpwd]').val();
        var zpwd1 = $('[name = zpwd1]').val();
        var zname = $('[name = zname]').val();
        var zemail = $('[name = zemail]').val();
       if(zphone.length==0 ||zpwd.length==0 ||zpwd1.length==0 ||zname.length==0 ||zemail.length==0 ){
           return false;

       }
       return true;
    });
});