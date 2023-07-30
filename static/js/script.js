$(document).ready(function()
{
   var form = $('#form_buying_product');
   console.log(form);
   console.log('123');

   function basket_updating(product_id, nmb, is_delete) {
      var data = {};
      data.product_id = product_id;
      data.nmb = nmb;
      var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
      data["csrfmiddlewaretoken"] = csrf_token;
      var url = form.attr("action");

      if (is_delete){
         data['is_delete'] = true;
      }

      console.log(data)
      $.ajax({
         url: url,
         type: 'POST',
         data: data,
         cache: true,
         success: function (data) {
            console.log("OK");
            console.log(data.products_total_nmb);
            if (data.products_total_nmb || data.products_total_nmb == 0){
               $('#basket-total-nmb').text('('+data.products_total_nmb+')');
               console.log(data.products);
               $('.basket-item ul').html("");
               $.each(data.products, function (k, v){

                  $('.basket-item table tbody').append('<tr> <td>'+v.name+'</td> <td>'+ v.nmb + '</td> <td>' + v.price_per_item +'</td><td>'+
                  '<a class="delete-item" href="" data-product_id = "'+v.id+'">x</a>'+
                  '</td> </tr>');
               })
            }
         },
         error: function (){
            console.log("error")
         }
      })}





   $("#submit-btn-product").click(function(e) {
      e.preventDefault();
      console.log('14');
      var nmb = $('#quanty').val();
      console.log(nmb);
      var submit_btn = $('#submit-btn-product');
      var product_id = submit_btn.data("product-id");
      var product_name = submit_btn.data("product-name");
      var product_price = submit_btn.data("product-price");
      var product_img = submit_btn.data("product-img");
      console.log(product_id);
      console.log(product_name);
      console.log(product_price);
      console.log(product_img);



      basket_updating(product_id, nmb, is_delete = false);

   })

   function del_class(){
      $('.basket-item').removeClass ('invisible');
   };

   $('.basket-container').on('click ',function (e) {
      e.preventDefault();
      del_class();
   });

   $('.basket-container').on('mouseover ',function (e) {
      e.preventDefault();
      del_class();
   });

   // $('.basket-container').on('mouseout ',function (e) {
   //    e.preventDefault();
   //    del_class();
   // })

   $(document).on('click',('.delete-item'),function (e) {
      e.preventDefault();
      product_id = $(this).data("product_id");
      nmb=0;
      basket_updating( product_id, nmb,is_delete=true);
   })



      $(document).on('change',".product-in-basket-nmb",function () {
      var current_nmb = $(this).val();
      var current_tr = $(this).closest('tr');
      var current_price = parseFloat((current_tr).find('.product-price').text()).toFixed(2);
      var total_amount = parseFloat(current_nmb * current_price).toFixed(2);
      current_tr.find('.total-product-in-basket-amount').text(total_amount)
      calculatingBasketAmount()
   })


});
