const form=document.querySelector('form');
const loading_spinner=document.querySelector('.loading');
const API_URL='/mews';
const mew_section=document.querySelector('.mews');
const submitButton=document.querySelector('.button-primary');


window.onload=function(){listAllMews();}

function listAllMews(){
    fetch(API_URL)
    .then(response=>response.json())
    .then(response=>{
        for(i of response.mews){
            let html=`
                <div class="mew">
                <h4>${i.name}</h4>
                <p>${i.content}</p>
                </div>
                <br>
                `
            mew_section.innerHTML+=html;
        }
        console.log(response);
})




form.addEventListener('submit',(event)=>{
    let form_data=new FormData(form);

    let name=form_data.get('name');
    let content=form_data.get('content');

    form.style.display="none";
    loading_spinner.style.display='';


    let new_mew={
        'name':name,
        'content':content
        
    }

    fetch(API_URL,{
                method:"POST",
                body:JSON.stringify(new_mew),
                headers:{
                    'content-type':'application/json'
                }
            }
    ).then(response=>response.json())
    .then(response=>{
        console.log("Hello");
        form.style.display="";
        loading_spinner.style.display="none";

        form.reset();

        
    })
    event.preventDefault();
})}


submitButton.addEventListener('click',function(){
    listAllMews();
})



