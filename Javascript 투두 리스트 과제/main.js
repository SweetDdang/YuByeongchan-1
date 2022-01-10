
document.getElementById('add-btn').addEventListener('click', addList); 
document.getElementById('delete-all').addEventListener('click', del_all); 
document.getElementById('delete-last').addEventListener('click', del_last); 
document.getElementById('delete-selected').addEventListener('click', del_sel); 

function addList() {
    const contents = document.querySelector('.text-box');
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><input type="checkbox" class="check-btn"></td><td class="td-text">${contents.value}</td>`;
    document.querySelector(".nth-col").append(tr);
    document.querySelector(".add-text input").value = '';
}

function del_all() {
    const nth_col = document.querySelector(".nth-col");
  while (nth_col.hasChildNodes()) {
    nth_col.removeChild(nth_col.firstChild);
  }
}

function del_sel() {
    const nth_col = document.querySelector(".nth-col");
    var check_btn = document.querySelectorAll(".nth-col .check-btn"); 
    for (var i in check_btn) 
    {   if (check_btn[i].checked)
        {   
            nth_col.removeChild(check_btn[i].parentNode.parentNode); 
        }
    }
}
        
function del_last() {
    const last_nth_col = document.querySelector(".nth-col tr:last-child");
    last_nth_col.remove()
}
