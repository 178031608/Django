$(function(){
   $('#frmlogin').submit(function(){
       var phone=$('[name=uphone]').val();
       var pwd=$('[name=upwd]').val();
       var t=1;
       if(phone.length ==0){
           t=0;
           $('[name=uphone]').append('<p>手机号码未输入</p>')
       }
       if(pwd.length !=0){
            t=0;
            $('[name=upwd]').append('<p></p>')
       }
       if(t == 0 ){
           return false;
       }
       return true;
   });
});