let deductions =document.querySelector('.deductions');
let deduction=document.querySelector('.deductions .deduction');
let gobutton=document.querySelector("#deductiongo");
let numofdeductions=document.querySelector("#numDeductions");
let value=0;

gobutton.addEventListener("click",()=>{
    value=numofdeductions.value;
    function removeChildrenDeduction(){
        var deductiontemp=document.querySelectorAll('.deductions .deduction');
        deductiontemp.forEach(element => {
            deductions.removeChild(element);
        });
    }
    removeChildrenDeduction();
    for(let i=0;i<value;i++){ 
        let deductionclone=deduction.cloneNode(true);
        deductionclone.children[0].innerHTML=`${i+1}:-`;
        deductionclone.children[1].children[1].setAttribute("name",`damt${i+1}`);
        deductionclone.children[2].children[1].setAttribute("name",`dcategory${i+1}`);
        deductions.appendChild(deductionclone);
    }
})
function salaryval(){
    numofdeductions.value=value;
    return true;
}
