buttonRemoveClass = document.getElementById('button-AC');

buttonRemoveClass.addEventListener('click', function (){
    setTimeout(function(){
        table = document.querySelector('.dataframe');
        table.classList.remove('dataframe');
        table.classList.add('table-fixed')
    }, 1000);
});
