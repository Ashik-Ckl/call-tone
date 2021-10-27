
function btnPlus(productId,b){
    
    quantity = $("#quantityId"+productId).val()
    qty = ''
    if (quantity == null){
        qty = 1
    }
    else{
        qty = parseInt(quantity) + parseInt(1)
    }
    // $(quantity).val(qty)
    $("#quantityId"+productId).val(qty)
    // var $qty = $(b).closest('.quantity').find(".qty");
   
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    data = {
        'id':'1',
        'product_id':productId,
        'quantity':qty,
        csrfmiddlewaretoken:csrftoken
    }
    $.ajax({
        url: 'http://127.0.0.1:8000/core/update_cart/',
        type:'POST',
        data:data,
        dataType: "json",
        cache: false,
        success: function(response){ 
            updateTotal = response['quantity'] * response['price']
            $("#subTotalPrice"+productId).html('SAR.'+updateTotal+'.00')
            $("#subTotalH6Id").html('SAR.'+response['sub_total']+'.00')

        }
    });
}



function btnLess(productId,b){

    quantity = $("#quantityId"+productId).val()
    qty = ''
    if (quantity == ''){
        qty = 1
    }
    else{
        qty = parseInt(quantity) - parseInt(1)
    }
    $("#quantityId"+productId).val(qty)
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    data = {
        'id':'0',
        'product_id':productId,
        'quantity':qty,
        csrfmiddlewaretoken:csrftoken
    }
    $.ajax({
        url: 'http://127.0.0.1:8000/core/update_cart/',
        type:'POST',
        data:data,
        dataType: "json",
        cache: false,
        success: function(response){            
            updateTotal = response['quantity'] * response['price']
            $("#subTotalPrice"+productId).html('SAR.'+updateTotal+'.00')
            $("#subTotalH6Id").html('SAR.'+response['sub_total']+'.00')

        }
    });
}



function deleteProduct (productId,df){

    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    data = {
        // 'id':'81456',
        'product_id':productId,
        csrfmiddlewaretoken:csrftoken
    }
    $.ajax({
        url: 'http://127.0.0.1:8000/core/delete_cart/',
        type:'POST',
        data:data,
        dataType: "json",
        cache: false,
        success: function(response){
            console.log(response['length']) 
            $("#cartDataCountVal").html(response['length'])
            var subTotal = $("#subTotalInputId").val();
            finalSubTotal = parseInt(subTotal) - parseInt(response['price'])
            $("#subTotalH6Id").html('SAR.'+finalSubTotal+'.00')
            $(df).closest("li").remove(); 

            if(response['length'] == '0'){
                $("#subTotalH6Id").html('SAR.'+'0'+'.00')


            }
        }
    });

};