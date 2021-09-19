$(document).ready(function(){
   // close btn
   $('#btn').click(function(){
      if(this.className == 'on'){
         this.classList.remove('on');
      }else{
         this.classList.add('on');
      }

      $('.nav').toggle('slide');
   });
   
   
   $('.storeCatUpdate').click(function(){
      window.open('updatePageShort.html', '_self');
      // var col1 = $(this).parents('td').siblings().eq(0).text();
      // var col2 = $(this).parents('td').siblings().eq(1).text();
      // var col3 = $(this).parents('td').siblings().eq(2).find('img').attr('src');

      // $('#updateCateg').val(col1);
      // $('#updateDesc').val(col2);
      // $('#updateIMG').attr('src', col3);
   });

   // Store Upadate button
   $('.storeUpdate').click(function(){
      window.open('updatePageLong.html', '_self');
   });

   // Store Delete button
   $('.storeDelete').click(function(){
      $(this).closest('tr').remove();
   });

   // Store Product button
   $('.storeProduct').click(function(){
      window.open('product-categories.html', '_self');
   });


   // Product-categories Update button
   $('.productUpdate').click(function(){
      window.open('updatePageShort.html', '_self');
   });

   // Resturant-categories update button
   $('.resturantUpdate').click(function(){
      window.open('updatePageShort.html', '_self');
   });

   // Resturants update button
   $('.restUpdate').click(function(){
      window.open('updatePageLong.html', '_self');
   })

   // Resturants food button
   $('.restFood').click(function(){
      window.open('food-categories.html', '_self')
   });

   // Food categories update button
   $('.foodUpdate').click(function(){
      window.open('updatePageShort.html', '_selef');
   });


   // Add more products
   $('.add-more').click(function(){
      $('.inputs-wrapper').append('<div class="inputs-wrapper"><div class="name-field"><label for="name">Name: </label><input type="text" name="name"></div><div class="desc-field"><label for="desc">Description: </label><input type="text" name="desc"></div><div class="img-field"><label for="image">Image: </label><input type="file" name="image"></div></div>');
   });


   $('.addMoreToStoreButton').click(function(){
      $('.storesInputsWrapper').append('<div class="storesInputsWrapper"> <div class="uname-field"> <label for="u-name">Username: </label> <input type="text" name="u-name"> </div> <div class="fname-field"> <label for="f-name">First Name: </label> <input type="text" name="f-name"> </div> <div class="lname-field"> <label for="l-name">Last Name: </label> <input type="text" name="l-name"> </div> <div class="email-field"> <label for="email">Email: </label> <input type="email" name="email"> </div> <div class="password-field"> <label for="pwd">Password: </label> <input type="password" name="pwd"> </div> <div class="mobile-field"> <label for="mobile">Mobile: </label> <input type="text" name="mobile"> </div> <div class="sname-field"> <label for="sname">Store Name: </label> <input type="text" name="sname"> </div> <div class="city-field"> <label for="city">City: </label> <input type="text" name="city"> </div> <div class="state-field"> <label for="state">State: </label> <input type="text" name="state"> </div> <div class="zip-field"> <label for="zip">Zip code: </label> <input type="text" name="zip"> </div> <div class="address-field"> <label for="address">Address: </label> <input type="text" name="address"> </div> <div class="img-field"> <label for="image">Store Image_1: </label> <input type="file" name="image"> </div> <div class="img-field"> <label for="image">Store Image_2: </label> <input type="file" name="image"> </div> <div class="options-field"> <label for="category">Category: </label> <select name="category" class="category"> <option value="">Options 1</option> <option value="">Options 2</option> <option value="">Options 3</option> <option value="">Options 4</option> </select> </div> </div>');
   });


   $('.addMoreToProduct').click(function(){
      $('.productInputsWrapper').append('<div class="inputs-wrapper"><div class="name-field"><label for="name">Name: </label><input type="text" name="name"></div><div class="desc-field"><label for="desc">Description: </label><input type="text" name="desc"></div><div class="img-field"><label for="image">Image: </label><input type="file" name="image"></div></div>');
   });


   $('.addMoreToRest').click(function(){
      $('.restInputsWrapper').append('<div class="inputs-wrapper"><div class="name-field"><label for="name">Name: </label><input type="text" name="name"></div><div class="desc-field"><label for="desc">Description: </label><input type="text" name="desc"></div><div class="img-field"><label for="image">Image: </label><input type="file" name="image"></div></div>');
   });

   $('.addMoreResturants').click(function(){
      $('.resturantsInputsWrapper').append('<div class="storesInputsWrapper"> <div class="uname-field"> <label for="u-name">Username: </label> <input type="text" name="u-name"> </div> <div class="fname-field"> <label for="f-name">First Name: </label> <input type="text" name="f-name"> </div> <div class="lname-field"> <label for="l-name">Last Name: </label> <input type="text" name="l-name"> </div> <div class="email-field"> <label for="email">Email: </label> <input type="email" name="email"> </div> <div class="password-field"> <label for="pwd">Password: </label> <input type="password" name="pwd"> </div> <div class="mobile-field"> <label for="mobile">Mobile: </label> <input type="text" name="mobile"> </div> <div class="sname-field"> <label for="sname">Resturant Name: </label> <input type="text" name="sname"> </div> <div class="city-field"> <label for="city">City: </label> <input type="text" name="city"> </div> <div class="state-field"> <label for="state">State: </label> <input type="text" name="state"> </div> <div class="zip-field"> <label for="zip">Zip code: </label> <input type="text" name="zip"> </div> <div class="address-field"> <label for="address">Address: </label> <input type="text" name="address"> </div> <div class="img-field"> <label for="image">Store Image_1: </label> <input type="file" name="image"> </div> <div class="img-field"> <label for="image">Store Image_2: </label> <input type="file" name="image"> </div> <div class="options-field"> <label for="category">Category: </label> <select name="category" class="category"> <option value="">Options 1</option> <option value="">Options 2</option> <option value="">Options 3</option> <option value="">Options 4</option> </select> </div> </div>');
   });

   $('.addMoreToFood').click(function(){
      $('.foodInputsWrapper').append('<div class="inputs-wrapper"><div class="name-field"><label for="name">Name: </label><input type="text" name="name"></div><div class="desc-field"><label for="desc">Description: </label><input type="text" name="desc"></div><div class="img-field"><label for="image">Image: </label><input type="file" name="image"></div></div>');
   });

   $('#closeBtn').click(function(){
      $('.sidebar').css('left', '0')
   });
  
});