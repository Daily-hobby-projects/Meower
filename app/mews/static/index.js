const form=document.querySelector('form');
const loading_spinner=document.querySelector('.loading');
const API_URL='/mews'


loading_spinner.style.display='';

document.onload=()=>{
    listAllMews();
}

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
})


function listAllMews(){
    fetch(API_URI)
    .then(response=>response.json())
    .then(mews=>{
        console.log(mews);
    })
}