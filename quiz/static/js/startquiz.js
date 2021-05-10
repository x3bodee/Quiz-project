console.log('Hi Mona');

const url =window.location.href

const quizBox =document.getElementById('quiz-box')

$.ajax({
    type: 'Get',
    url: `${url}data`,
    success: function(response){
  //console.log(response) 
        data=response.data
        data.forEach(el=>{
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML+=`
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
            }
        });
    },
    error: function (error){
        console.log(error);
    }

})