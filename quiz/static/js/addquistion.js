var q=0

function addQuestion(){
    console.log("add new question feild")

    let selected = document.getElementById("selectType")
    let val = selected.options[selected.selectedIndex].value;
    console.log(val)
    var adddiv = document.getElementById("add");
    var addQuizForm = document.getElementById("addQuizForm");
    
    // create row
    // add qustion label 
    // add input for the qusition
    let div=document.createElement('div')
    div.setAttribute("value","1")
    let label=document.createElement('label')
    let inpput=document.createElement('input')
    div.className='row borderr'
    label.innerText="question"
    inpput.type="text"
    inpput.placeholder="Enter the question"
    q++
    inpput.id="qustion"+q
    inpput.required = true;
    inpput.name="q-"+q
    div.id="q"+q
    // div.classList.("borderr");

    // create answer for t or f and mcq
    let label2=document.createElement('label')
    let answer=document.createElement('input')
    let select=document.createElement('select')
    
    label2.innerText="Answer"

    if (val == "true") {
        // create  answer for T or F
        let tr=document.createElement('option')
        let fa=document.createElement('option')
        tr.value = true
        tr.text="true"
        fa.value = false
        fa.text="false"
        select.id="q-"+q+"-answer"
        select.name="q-"+q+"-answer"
        select.appendChild(tr)
        select.appendChild(fa)
        div.setAttribute("type-value","0")
        inpput.name+="$$TorF"
    }else{
    // create  answer for mcq
    answer.type="text"
    answer.required = true;
    answer.placeholder="Enter the Answer"
    answer.id="q"+q+"-answer"
    answer.name="q-"+q+"-answer"
    div.setAttribute("type-value","1")
    }

    // create button add choice
    // create button delete choice
    let add_choice=document.createElement('button')
    add_choice.setAttribute("onclick","addChoice(this)");
    add_choice.id="addch"
    add_choice.type="button"
    add_choice.innerText="Add Choice"
    add_choice.classList.add("btn-add")
    

    let delete_choice=document.createElement('button')
    delete_choice.id="delete"
    delete_choice.type="button"
    delete_choice.innerText="Delete Choice"
    delete_choice.classList.add("btn-add")
    delete_choice.setAttribute("onclick","deleteChoice(this)");

    let delete_question=document.createElement('button')
    delete_question.id="delete"
    delete_question.type="button"
    delete_question.innerText="Delete Question"
    delete_question.classList.add("btn-add")
    delete_question.setAttribute("onclick","deleteQuestion(this)");
    
    if (val == "true") {
        console.log("inside")
        div.appendChild(label)
        div.appendChild(inpput)
        div.appendChild(label2)
        div.appendChild(select)
        div.appendChild(delete_question)
    }else{
        div.appendChild(label)
        div.appendChild(inpput)
        div.appendChild(label2)
        div.appendChild(answer)
        div.appendChild(add_choice)
        div.appendChild(delete_choice)
        div.appendChild(delete_question)
    }
    
    addQuizForm.insertBefore(div,adddiv);

}

 function deleteQuestion(e){
    console.log("delete quistion")
    let parent = e.parentNode
    // let type=parent.getAttribute('type-value')
    // console.log(parent.getAttribute('type-value'))
    parent.remove()
 }

 function deleteChoice(e){
    console.log("delete quistion")
    let parent = e.parentNode
    let type=parent.getAttribute('type-value')
    // console.log(parent.getAttribute('type-value'))
    if (type == "0") {
        console.log("you can't delete")
    }else{

        let value = parent.getAttribute("value")
        let s=".ch"+value
        let el = parent.querySelector(s)
        el.remove()
        let n = parseInt(value)
        n--
        parent.setAttribute("value",""+n)
    }
 }

let addChoice = function addChoicee(e){
    console.log("add new choice feild")
    let parent = e.parentNode
    let addch = parent.querySelector("#addch")
    let question_id = parent.querySelector("input")
    value = parseInt(parent.getAttribute('value'))
    value++
    console.log(value)
    parent.setAttribute("value",""+value)
    // create choice
    let inpput=document.createElement('input')
    inpput.type="text"
    inpput.required = true;
    inpput.className="ch"+value
    inpput.name="ch-"+value
    inpput.placeholder="Enter the choice"
    
    parent.insertBefore(inpput,addch);
    // console.log(e.parentNode.id)
}