console.log('Hi Mona');

const url =window.location.href
console.log(url);


$.ajax({
    type: 'Get',
    url: `${url}data`,
    success: function(response){
        console.log(response);
    },
    error: function (error){
        console.log(error);
    }

})